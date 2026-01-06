from manim import *


class FordFulkersonFixed(Scene):
    def construct(self):
        # --- 1. CONFIGURATION ---

        node_positions = {
            'S': [-5, 0, 0],
            'A': [-2, 2.5, 0],
            'B': [-2, 0, 0],
            'C': [-2, -2.5, 0],
            'D': [2, 1.5, 0],
            'E': [2, -1.5, 0],
            'T': [5, 0, 0],
        }

        edges_config = [
            ('S', 'A', 12), ('S', 'B', 27), ('S', 'C', 5),
            ('A', 'D', 15), ('A', 'E', 8),
            ('B', 'D', 10), ('B', 'T', 9),
            ('C', 'B', 14), ('C', 'E', 6),
            ('D', 'T', 13),
            ('E', 'C', 11), ('E', 'T', 20)
        ]

        # --- MANUAL LABEL ADJUSTMENTS ---
        # Format: (u, v): [position_along_line (0-1), perpendicular_distance, angle_correction]
        # > position_along_line: 0.5 is middle. 0.3 is closer to start, 0.7 closer to end.
        # > perpendicular_distance: How far to push label away from line. Positive = Left/Up usually.
        layout_tweaks = {
            ('S', 'A'): [0.5, 0.4, 0],
            ('S', 'B'): [0.35, 0.4, 0],  # Move closer to S to avoid B-crowd
            ('S', 'C'): [0.5, -0.4, 0],

            ('A', 'D'): [0.5, 0.4, 0],
            ('A', 'E'): [0.25, 0.4, 0],  # CRITICAL: Move high up near A to avoid crossing B->D

            ('B', 'D'): [0.7, 0.3, 0],  # Move closer to D
            ('B', 'T'): [0.5, 0.3, 0],

            ('C', 'B'): [0.5, 0.4, 0],  # Vertical-ish edge
            ('C', 'E'): [0.6, -0.4, 0],  # Move closer to E

            ('D', 'T'): [0.5, 0.4, 0],

            ('E', 'T'): [0.5, -0.4, 0],
        }

        # --- 2. ALGORITHM LOGIC ---
        node_list = list(node_positions.keys())
        node_map = {name: i for i, name in enumerate(node_list)}
        inv_map = {i: name for name, i in node_map.items()}
        n = len(node_list)

        capacity = [[0] * n for _ in range(n)]
        for u, v, cap in edges_config:
            capacity[node_map[u]][node_map[v]] = cap

        r_graph = [row[:] for row in capacity]
        steps = []

        def bfs(s, t, parent):
            visited = [False] * n
            queue = [s]
            visited[s] = True
            parent[s] = -1
            while queue:
                u = queue.pop(0)
                for v in range(n):
                    if not visited[v] and r_graph[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == t: return True
            return False

        source, sink = node_map['S'], node_map['T']
        parent = [-1] * n
        total_flow = 0

        while bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, r_graph[parent[s]][s])
                s = parent[s]
            v = sink
            path_indices = [v]
            while v != source:
                u = parent[v]
                path_indices.append(u)
                r_graph[u][v] -= path_flow
                r_graph[v][u] += path_flow
                v = parent[v]
            steps.append((path_indices[::-1], path_flow))
            total_flow += path_flow

        # --- 3. DRAWING ---

        title = Text("Ford-Fulkerson Algorithm", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))

        # Scoreboard
        score_box = Rectangle(width=3.0, height=1.3, color=WHITE).to_corner(UL, buff=0.2).shift(DOWN * 0.6)
        flow_label = Text("Max Flow", font_size=20).move_to(score_box.get_top() + DOWN * 0.3)
        flow_val = Text("0", font_size=40, color=YELLOW).next_to(flow_label, DOWN, buff=0.1)
        scoreboard = VGroup(score_box, flow_label, flow_val)
        self.play(Create(scoreboard))

        nodes_dict = {}
        for name, pos in node_positions.items():
            circle = Circle(radius=0.4, color=BLUE, fill_opacity=0.5).move_to(pos)
            label = Text(name, font_size=24).move_to(pos)
            group = VGroup(circle, label)
            nodes_dict[name] = group

        edges_dict = {}
        labels_dict = {}
        current_flow_map = {(u, v): 0 for u, v, c in edges_config}

        for u, v, cap in edges_config:
            start = nodes_dict[u][0].get_center()
            end = nodes_dict[v][0].get_center()

            direction = end - start
            unit_vector = direction / np.linalg.norm(direction)
            start_point = start + unit_vector * 0.4
            end_point = end - unit_vector * 0.4

            line = Line(start_point, end_point, buff=0, color=GREY, stroke_width=2).add_tip(tip_length=0.2)

            # --- SMARTER LABEL POSITIONING ---
            tweak = layout_tweaks.get((u, v), [0.5, 0.4, 0])  # Default: Middle, 0.4 offset
            pos_alpha = tweak[0]
            perp_dist = tweak[1]

            # Point along the line
            base_pos = start_point + (end_point - start_point) * pos_alpha

            # Perpendicular vector
            angle = line.get_angle()
            offset_vec = np.array([-np.sin(angle), np.cos(angle), 0])

            # Some manual logic: if the line goes "backwards" or steep, flip offset
            # This ensures text is usually "above" or "left"
            if offset_vec[1] < 0 and abs(offset_vec[1]) > 0.1:
                offset_vec *= -1

            # Apply manual flip if perp_dist is negative
            if perp_dist < 0:
                offset_vec *= -1
                perp_dist = abs(perp_dist)

            label_pos = base_pos + offset_vec * perp_dist

            label_text = MathTex(f"0/{cap}", font_size=22)
            label_text.move_to(label_pos)

            # Background
            bg = BackgroundRectangle(label_text, color=BLACK, fill_opacity=0.85, buff=0.05)
            lbl_group = VGroup(bg, label_text)

            edges_dict[(u, v)] = line
            labels_dict[(u, v)] = lbl_group

        self.play(
            *[GrowFromCenter(n) for n in nodes_dict.values()],
            *[Create(e) for e in edges_dict.values()],
            run_time=1
        )
        self.play(*[FadeIn(l) for l in labels_dict.values()])

        # --- 4. ANIMATION LOOP ---

        accumulated_flow = 0

        for path_indices, bottleneck in steps:
            path_names = [inv_map[i] for i in path_indices]

            bn_text = Text(f"Bottleneck: {bottleneck}", font_size=28, color=ORANGE).next_to(title, DOWN)
            self.play(FadeIn(bn_text, shift=DOWN), run_time=0.5)

            # Highlight Path
            path_lines = []
            for i in range(len(path_names) - 1):
                u, v = path_names[i], path_names[i + 1]
                if (u, v) in edges_dict:
                    path_lines.append(edges_dict[(u, v)])
                elif (v, u) in edges_dict:
                    path_lines.append(edges_dict[(v, u)])

            self.play(
                *[e.animate.set_color(YELLOW).set_stroke(width=5) for e in path_lines],
                run_time=0.5
            )

            # Particles
            particles = VGroup()
            for _ in range(3):
                dot = Dot(radius=0.08, color=YELLOW)
                particles.add(dot)

            for i in range(len(path_names) - 1):
                u, v = path_names[i], path_names[i + 1]
                edge_obj = edges_dict.get((u, v)) or edges_dict.get((v, u))

                if edge_obj:
                    self.play(MoveAlongPath(particles[0], edge_obj), run_time=0.3, rate_func=linear)
                    node_circle = nodes_dict[v][0]
                    self.play(node_circle.animate.set_fill(YELLOW, opacity=0.8), run_time=0.1)
                    self.play(node_circle.animate.set_fill(BLUE, opacity=0.5), run_time=0.1)

            self.remove(particles)

            # Update Labels
            accumulated_flow += bottleneck
            label_anims = []

            for i in range(len(path_names) - 1):
                u, v = path_names[i], path_names[i + 1]

                if (u, v) in current_flow_map:
                    current_flow_map[(u, v)] += bottleneck
                    cap = 0
                    for eu, ev, c in edges_config:
                        if eu == u and ev == v: cap = c

                    new_txt = f"{current_flow_map[(u, v)]}/{cap}"
                    lbl_bg, lbl_txt = labels_dict[(u, v)]
                    new_lbl = MathTex(new_txt, font_size=22).move_to(lbl_txt)

                    if current_flow_map[(u, v)] == cap:
                        new_lbl.set_color(RED)

                    label_anims.append(Transform(lbl_txt, new_lbl))

                    # Thicken edge
                    ratio = current_flow_map[(u, v)] / cap
                    new_width = 2 + (ratio * 5)
                    label_anims.append(edges_dict[(u, v)].animate.set_stroke(width=new_width))

            # Update Scoreboard
            new_flow_val = Text(str(accumulated_flow), font_size=40, color=YELLOW).move_to(flow_val)
            label_anims.append(Transform(flow_val, new_flow_val))

            self.play(*label_anims)
            self.play(FadeOut(bn_text))

            self.play(
                *[e.animate.set_color(GREY) for e in path_lines],
                run_time=0.5
            )

        self.wait(1)
        final_rect = SurroundingRectangle(scoreboard, color=GREEN, buff=0.2)
        self.play(Create(final_rect))
        self.wait(2)