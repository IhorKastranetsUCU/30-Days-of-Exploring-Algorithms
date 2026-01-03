from manim import *
import heapq


class DijkstraCitiesFinal(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        COLOR_NODE_DEFAULT = WHITE
        COLOR_NODE_VISITED = TEAL
        COLOR_EDGE_DEFAULT = GRAY_E
        COLOR_EDGE_CANDIDATE = YELLOW
        COLOR_EDGE_CHECKING = RED
        COLOR_EDGE_FINAL = TEAL

        font_name = "Arial"

        # 1. Graph Data
        nodes = ["A", "B", "C", "D", "E", "F"]

        # (u, v, weight_in_km)
        edge_list = [
            ("A", "B", 130),
            ("A", "D", 150),
            ("D", "E", 400),
            ("B", "C", 160),
            ("B", "F", 450),
            ("A", "C", 300),
            ("D", "C", 75),
            ("C", "E", 50),
            ("C", "F", 320),
            ("E", "F", 140)
        ]

        # 2. Layout
        layout = {
            "A": [-6, 0, 0],
            "D": [-3, 2, 0],
            "B": [-3, -2, 0],
            "C": [-0.5, 0, 0],
            "E": [1.5, 2, 0],
            "F": [1.5, -2, 0]
        }

        # --- GRAPH CREATION ---
        g = DiGraph(
            nodes,
            [(u, v) for u, v, w in edge_list],
            layout=layout,
            vertex_config={
                "radius": 0.35,
                "color": COLOR_NODE_DEFAULT,
                "fill_color": BLACK,
                "fill_opacity": 1,
                "stroke_width": 3
            },
            edge_config={"stroke_width": 4, "color": COLOR_EDGE_DEFAULT, "tip_config": {"tip_length": 0.2}},
            labels=False
        )

        # Labels
        node_labels = VGroup()
        for node in nodes:
            label = Text(node, font=font_name, font_size=24, color=WHITE).move_to(layout[node])
            node_labels.add(label)

        # --- Manual Edge Weight Positioning ---
        label_overrides = {
            ("A", "E"): {"alpha": 0.25, "shift": UP * 0.2},
            ("B", "E"): {"alpha": 0.8, "shift": DOWN * 0.3},
            ("E", "F"): {"alpha": 0.5, "shift": RIGHT * 0.4},
            ("D", "C"): {"alpha": 0.7, "shift": UP * 0.25},
            ("A", "B"): {"alpha": 0.5, "shift": DOWN * 0.3},
            ("A", "D"): {"alpha": 0.5, "shift": UP * 0.3},
            ("C", "E"): {"alpha": 0.5, "shift": UP * 0.2},
        }

        edge_weights = VGroup()
        for u, v, w in edge_list:
            edge_obj = g.edges[(u, v)]

            alpha = 0.5
            shift_vec = UP * 0.25

            if (u, v) in label_overrides:
                settings = label_overrides[(u, v)]
                alpha = settings.get("alpha", 0.5)
                shift_vec = settings.get("shift", UP * 0.2)

            pos = edge_obj.point_from_proportion(alpha)
            weight_lbl = Integer(w).scale(0.55).move_to(pos).shift(shift_vec)

            bg = BackgroundRectangle(weight_lbl, fill_opacity=1, buff=0.05, color=BLACK)
            edge_weights.add(VGroup(bg, weight_lbl))

        # --- UI (RIGHT SIDE) ---
        ui_group = VGroup()

        # Title
        title = Text("Dijkstra Algorithm", font=font_name, font_size=32).to_edge(UP)

        # Header Position
        header_y = 3.0
        col_x = [3.5, 4.8, 6.0]

        headers = VGroup(
            Text("City", font=font_name, font_size=24, color=GRAY).move_to([col_x[0], header_y, 0]),
            Text("Via", font=font_name, font_size=24, color=GRAY).move_to([col_x[1], header_y, 0]),
            Text("Cost", font=font_name, font_size=24, color=GRAY).move_to([col_x[2], header_y, 0])
        )

        # Table Rows
        table_rows = {}
        row_group = VGroup()
        row_group.add(headers)

        for i, node in enumerate(nodes):
            y_pos = header_y - 0.45 * (i + 1)

            t_node = Text(node, font=font_name, font_size=24, color=WHITE).move_to([col_x[0], y_pos, 0])
            t_via = Text("-", font=font_name, font_size=24, color=GRAY).move_to([col_x[1], y_pos, 0])
            t_cost = Text("∞", font=font_name, font_size=24, color=GRAY).move_to([col_x[2], y_pos, 0])

            row = VGroup(t_node, t_via, t_cost)
            table_rows[node] = {"via": t_via, "cost": t_cost}
            row_group.add(row)

        ui_group.add(row_group)

        # Queue
        pq_title = Text("Priority Queue:", font=font_name, font_size=24).next_to(row_group, DOWN,
                                                                                      buff=0.5).align_to(headers, LEFT)
        pq_list_display = VGroup().next_to(pq_title, DOWN)

        ui_group.add(pq_title, pq_list_display)

        # --- ANIMATION ---
        self.play(
            Create(g),
            Write(node_labels),
            FadeIn(edge_weights),
            Write(title),
            FadeIn(ui_group)
        )
        self.wait(0.5)

        # Logic
        start_node = "A"
        path_len = {v: float("inf") for v in nodes}
        path_len[start_node] = 0
        parents = {v: None for v in nodes}
        pq = [(0, start_node)]

        # FIX: Track nodes that are fully done to avoid un-highlighting them
        finalized_nodes = set()

        def update_table_visual(node, via_node, cost_val):
            row_data = table_rows[node]
            new_via = Text(str(via_node), font=font_name, font_size=24, color=YELLOW).move_to(row_data["via"])
            new_cost = Text(str(cost_val), font=font_name, font_size=24, color=YELLOW).move_to(row_data["cost"])
            self.play(
                Transform(row_data["via"], new_via),
                Transform(row_data["cost"], new_cost),
                run_time=0.4
            )

        def update_pq_display():
            new_display = VGroup()
            sorted_pq = sorted(pq)[:5]
            for cost, n in sorted_pq:
                entry = Text(f"{n}: {cost}", font=font_name, font_size=18, color=YELLOW)
                new_display.add(entry)
            if len(pq) > 5:
                new_display.add(Text("...", font=font_name, font_size=18, color=GRAY))

            new_display.arrange(DOWN, aligned_edge=LEFT).next_to(pq_title, DOWN)
            return new_display

        # Init A
        update_table_visual("A", "Start", 0)
        self.play(Transform(pq_list_display, update_pq_display()))
        self.wait(0.5)

        while pq:
            current_dist, u = heapq.heappop(pq)

            self.play(Transform(pq_list_display, update_pq_display()), run_time=0.4)

            # --- LOGIC FIX START ---
            # Якщо шлях застарілий:
            if current_dist > path_len[u]:
                # Скидаємо колір на сірий ТІЛЬКИ якщо місто ще не було "затверджено" (не було Teal)
                if u not in finalized_nodes:
                    self.play(g.vertices[u].animate.set_stroke(color=GRAY, width=3), run_time=0.3)
                else:
                    # Якщо місто вже затверджене, просто ігноруємо цей крок без візуальних змін
                    pass
                continue

            # Якщо шлях актуальний - "затверджуємо" місто
            finalized_nodes.add(u)
            self.play(
                g.vertices[u].animate.set_stroke(color=COLOR_NODE_VISITED, width=6),
                run_time=0.5
            )
            # --- LOGIC FIX END ---

            # Neighbors
            neighbors = []
            for (src, dst, w) in edge_list:
                if src == u:
                    neighbors.append((dst, w))

            for v, w in neighbors:
                # Skip checking neighbors if they are already finalized (optimization visual)
                if v in finalized_nodes:
                    continue

                edge_key = (u, v)

                # Check Edge
                self.play(
                    g.edges[edge_key].animate.set_color(COLOR_EDGE_CHECKING).set_stroke(width=6),
                    run_time=0.4
                )

                new_dist = current_dist + w
                if new_dist < path_len[v]:
                    path_len[v] = new_dist
                    parents[v] = u
                    heapq.heappush(pq, (new_dist, v))

                    update_table_visual(v, u, new_dist)
                    self.play(Transform(pq_list_display, update_pq_display()), run_time=0.4)

                    self.play(g.edges[edge_key].animate.set_color(COLOR_EDGE_CANDIDATE).set_stroke(width=4),
                              run_time=0.3)
                else:
                    self.play(g.edges[edge_key].animate.set_color(GRAY).set_stroke(width=2).set_opacity(0.3),
                              run_time=0.3)

            self.wait(0.3)

        # Final Path
        group_final = []
        for node, par in parents.items():
            if par:
                group_final.append(g.edges[(par, node)].animate.set_color(COLOR_EDGE_FINAL).set_stroke(width=6))

        if group_final:
            self.play(*group_final, run_time=1.5)

        self.wait(2)