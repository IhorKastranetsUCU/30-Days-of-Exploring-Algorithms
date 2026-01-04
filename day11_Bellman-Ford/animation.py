from manim import *


class BellmanFordCustomGraph(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        COLOR_NODE_DEFAULT = WHITE
        COLOR_NODE_UPDATED = TEAL
        COLOR_EDGE_DEFAULT = GRAY
        COLOR_EDGE_ACTIVE = YELLOW  # Зараз перевіряємо
        COLOR_EDGE_DONE = TEAL  # Вже перевірили в цій ітерації
        COLOR_TEXT_DEFAULT = GRAY  # Текст у списку

        font_name = "Arial"

        # 1. New Graph Data
        nodes = ["A", "B", "C", "D", "E", "F"]
        # [u, v, w]
        edges_data = [
            ["A", "B", 60],
            ["A", "C", 40],
            ["A", "D", 50],
            ["B", "E", -10],
            ["C", "B", -15],
            ["C", "E", 30],
            ["D", "C", -20],
            ["D", "F", -10],
            ["E", "F", 30]
        ]

        # 2. Compact Layout (Left aligned)
        # Shifted nodes to x < 2 to leave space for UI
        layout = {
            "A": [-6.0, 0, 0],
            "C": [-3.5, 2.0, 0],  # Top layer 1
            "B": [-3.5, -2.0, 0],  # Bottom layer 1
            "D": [-1.0, 2.0, 0],  # Top layer 2
            "E": [-1.0, -2.0, 0],  # Bottom layer 2
            "F": [1.5, 0, 0]  # End node
        }

        # --- GRAPH CREATION ---
        g = DiGraph(
            nodes,
            [(u, v) for u, v, w in edges_data],
            layout=layout,
            vertex_config={
                "radius": 0.30,  # Slightly smaller nodes
                "color": COLOR_NODE_DEFAULT,
                "fill_color": BLACK,
                "fill_opacity": 1,
                "stroke_width": 3
            },
            edge_config={"stroke_width": 3, "color": COLOR_EDGE_DEFAULT, "tip_config": {"tip_length": 0.15}},
            labels=False
        )

        # Labels
        node_labels = VGroup()
        for node in nodes:
            label = Text(node, font=font_name, font_size=20, color=WHITE).move_to(layout[node])
            node_labels.add(label)

        # --- Edge Weights Positioning ---
        # Adjusted for this specific topology
        label_overrides = {
            ("A", "C"): {"alpha": 0.5, "shift": UP * 0.25},
            ("A", "B"): {"alpha": 0.5, "shift": DOWN * 0.25},
            ("B", "C"): {"alpha": 0.5, "shift": RIGHT * 0.25},  # Vertical
            ("C", "D"): {"alpha": 0.5, "shift": UP * 0.2},  # Horizontal Top
            ("B", "D"): {"alpha": 0.7, "shift": RIGHT * 0.3},  # Cross up
            ("C", "E"): {"alpha": 0.3, "shift": RIGHT * 0.3},  # Cross down
            ("D", "E"): {"alpha": 0.5, "shift": LEFT * 0.25},  # Vertical
            ("D", "F"): {"alpha": 0.5, "shift": UP * 0.2},
            ("E", "F"): {"alpha": 0.5, "shift": DOWN * 0.25},
            ("F", "B"): {"alpha": 0.15, "shift": DOWN * 0.3},  # Long back edge (near F to be visible)
        }

        edge_weights = VGroup()
        for u, v, w in edges_data:
            edge_obj = g.edges[(u, v)]
            alpha = 0.5
            shift_vec = UP * 0.2

            if (u, v) in label_overrides:
                settings = label_overrides[(u, v)]
                alpha = settings.get("alpha", 0.5)
                shift_vec = settings.get("shift", UP * 0.2)

            pos = edge_obj.point_from_proportion(alpha)
            # Smaller text for weights
            weight_lbl = Integer(w).scale(0.5).move_to(pos).shift(shift_vec)
            bg = BackgroundRectangle(weight_lbl, fill_opacity=1, buff=0.05, color=BLACK)
            edge_weights.add(VGroup(bg, weight_lbl))

        # --- UI (RIGHT SIDE) ---
        ui_group = VGroup()

        # Title
        title = Text("Bellman-Ford Algorithm", font=font_name, font_size=32).to_edge(UP)

        # Table Position (Moved Up and Compacted)
        header_y = 3.5
        col_x = [3.0, 4.2, 5.4]  # Compact columns

        headers = VGroup(
            Text("Node", font=font_name, font_size=20, color=GRAY).move_to([col_x[0], header_y, 0]),
            Text("Via", font=font_name, font_size=20, color=GRAY).move_to([col_x[1], header_y, 0]),
            Text("Cost", font=font_name, font_size=20, color=GRAY).move_to([col_x[2], header_y, 0])
        )

        table_rows = {}
        row_group = VGroup()
        row_group.add(headers)

        for i, node in enumerate(nodes):
            y_pos = header_y - 0.4 * (i + 1)  # Tighter row spacing (0.4)
            t_node = Text(node, font=font_name, font_size=20, color=WHITE).move_to([col_x[0], y_pos, 0])
            t_via = Text("-", font=font_name, font_size=20, color=GRAY).move_to([col_x[1], y_pos, 0])
            t_cost = Text("∞", font=font_name, font_size=20, color=GRAY).move_to([col_x[2], y_pos, 0])

            row = VGroup(t_node, t_via, t_cost)
            table_rows[node] = {"via": t_via, "cost": t_cost}
            row_group.add(row)

        ui_group.add(row_group)

        # Edge List
        # Calculate start position based on table end
        table_bottom_y = header_y - 0.4 * len(nodes)

        list_title = Text("Edges Check List:", font=font_name, font_size=20).next_to(row_group, DOWN,
                                                                                     buff=0.4).align_to(headers, LEFT)
        iter_text = Text("Iter: 0", font=font_name, font_size=18, color=WHITE).next_to(list_title, RIGHT, buff=0.5)

        # Build List Items
        edge_text_items = []
        for u, v, w in edges_data:
            # Very compact font (16) to fit 10 items
            txt = Text(f"{u}->{v} ({w})", font=font_name, font_size=16, color=COLOR_TEXT_DEFAULT)
            edge_text_items.append(txt)

        # Tighter buffer (0.12)
        edge_list_group = VGroup(*edge_text_items).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(list_title, DOWN,
                                                                                                       buff=0.15).align_to(
            list_title, LEFT)

        ui_group.add(list_title, iter_text, edge_list_group)

        # Move UI slightly right to ensure no overlap
        ui_group.shift(RIGHT * 0.5)

        # --- ANIMATION ---
        self.play(
            Create(g),
            Write(node_labels),
            FadeIn(edge_weights),
            Write(title),
            FadeIn(ui_group)
        )
        self.wait(0.5)

        # --- LOGIC ---
        start_node = "A"
        cost = {v: float("inf") for v in nodes}
        cost[start_node] = 0
        predecessor = {v: None for v in nodes}

        def update_table_visual(node, via_node, cost_val):
            row_data = table_rows[node]
            new_via = Text(str(via_node), font=font_name, font_size=20, color=YELLOW).move_to(row_data["via"])
            new_cost = Text(str(cost_val), font=font_name, font_size=20, color=YELLOW).move_to(row_data["cost"])
            self.play(
                Transform(row_data["via"], new_via),
                Transform(row_data["cost"], new_cost),
                run_time=0.2
            )

        # Initialize A
        update_table_visual("A", "Start", 0)
        self.play(g.vertices["A"].animate.set_stroke(color=COLOR_NODE_UPDATED, width=6))

        total_nodes = len(nodes)

        # Run N-1 iterations
        for i in range(total_nodes - 1):
            new_iter_text = Text(f"Iter: {i + 1}", font=font_name, font_size=18, color=WHITE).move_to(
                iter_text.get_center()).align_to(iter_text, LEFT)

            # Reset visual state for new iteration
            self.play(
                Transform(iter_text, new_iter_text),
                edge_list_group.animate.set_color(COLOR_TEXT_DEFAULT),
                *[g.edges[(u, v)].animate.set_color(COLOR_EDGE_DEFAULT).set_opacity(1).set_stroke(width=3) for u, v, w
                  in edges_data],
                run_time=0.4
            )

            flag = False

            for idx, (u, v, weight) in enumerate(edges_data):
                edge_key = (u, v)

                # Active Highlight
                self.play(
                    edge_list_group[idx].animate.set_color(COLOR_EDGE_ACTIVE),
                    g.edges[edge_key].animate.set_color(COLOR_EDGE_ACTIVE).set_stroke(width=5),
                    run_time=0.15  # Faster animation for many edges
                )

                if cost[u] == float('inf'):
                    # Skip visual
                    self.play(
                        edge_list_group[idx].animate.set_color(COLOR_EDGE_DONE),
                        g.edges[edge_key].animate.set_color(COLOR_EDGE_DEFAULT).set_stroke(width=3).set_opacity(0.3),
                        run_time=0.15
                    )
                    continue

                # Relaxation
                if cost[u] != float('inf') and cost[u] + weight < cost[v]:
                    cost[v] = cost[u] + weight
                    predecessor[v] = u
                    flag = True

                    self.play(
                        g.vertices[v].animate.set_stroke(color=COLOR_NODE_UPDATED, width=6),
                        run_time=0.1
                    )
                    update_table_visual(v, u, cost[v])

                # Mark Done
                self.play(
                    edge_list_group[idx].animate.set_color(COLOR_EDGE_DONE),
                    g.edges[edge_key].animate.set_color(COLOR_EDGE_DEFAULT).set_stroke(width=3),
                    run_time=0.15
                )

            if not flag:
                break

        self.wait(3)