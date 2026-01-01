from manim import *
import heapq


class PrimImproved(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        # Colors
        COLOR_UNVISITED = WHITE
        COLOR_VISITED = TEAL
        COLOR_EDGE_DEFAULT = GRAY_E
        COLOR_EDGE_CANDIDATE = YELLOW
        COLOR_EDGE_CHECKING = RED
        COLOR_EDGE_MST = TEAL

        # Graph Data
        nodes = ["A", "B", "C", "D", "E", "G"]
        edge_list = [
            ("A", "B", 12), ("A", "D", 8), ("A", "E", 14),
            ("B", "C", 3), ("B", "E", 15), ("B", "G", 5),
            ("C", "D", 5), ("C", "E", 2), ("C", "G", 5),
            ("E", "G", 4)
        ]

        # Layout positions
        layout = {
            "A": [-4.5, 2, 0],
            "D": [-4.5, -2, 0],
            "B": [-1, 2.5, 0],
            "C": [-1, -2.5, 0],
            "E": [2, 0, 0],
            "G": [5, 0, 0]
        }

        # --- GRAPH CREATION ---
        g = Graph(
            nodes,
            [(u, v) for u, v, w in edge_list],
            layout=layout,
            vertex_config={"radius": 0.35, "color": COLOR_UNVISITED},
            edge_config={"stroke_width": 4, "color": COLOR_EDGE_DEFAULT},
            labels=True
        ).scale(0.8).to_edge(LEFT, buff=1)

        # Edge Weights
        edge_weights = VGroup()
        for u, v, w in edge_list:
            edge_obj = g.edges[tuple(sorted((u, v)))]
            weight_lbl = Integer(w).scale(0.6).move_to(edge_obj.get_center()).set_z_index(10)
            bg = BackgroundRectangle(weight_lbl, fill_opacity=1, buff=0.05, color=BLACK)
            edge_weights.add(VGroup(bg, weight_lbl))

        # --- UI (RIGHT SIDE) ---
        # Title
        title = Text("Prim's Algorithm", font_size=32).to_edge(UP)

        # Legend
        legend_dot_mst = Dot(color=COLOR_VISITED)
        legend_text_mst = Text("In MST", font_size=20).next_to(legend_dot_mst, RIGHT)
        legend_line_cand = Line(start=LEFT, end=RIGHT, color=COLOR_EDGE_CANDIDATE).scale(0.5)
        legend_text_cand = Text("In Queue", font_size=20).next_to(legend_line_cand, RIGHT)
        legend_line_curr = Line(start=LEFT, end=RIGHT, color=COLOR_EDGE_CHECKING).scale(0.5)
        legend_text_curr = Text("Checking", font_size=20).next_to(legend_line_curr, RIGHT)

        # ЗМІНА 1: buff=1.0 (було 0.5), щоб опустити легенду нижче
        legend = VGroup(
            VGroup(legend_dot_mst, legend_text_mst),
            VGroup(legend_line_cand, legend_text_cand),
            VGroup(legend_line_curr, legend_text_curr)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=1.0)

        # Status Bar (Bottom)
        status_box = Rectangle(width=12, height=1, color=WHITE).to_edge(DOWN)
        status_text = Text("Ready...", font_size=24).move_to(status_box)

        # Priority Queue Display
        # ЗМІНА 2: Додано .shift(DOWN * 1.5), щоб опустити список черги
        pq_title = Text("Queue (Min-Heap):", font_size=24).next_to(g, RIGHT, buff=1).align_to(g, UP).shift(DOWN * 1.5)
        pq_list_display = VGroup().next_to(pq_title, DOWN)

        self.play(Create(g), FadeIn(edge_weights), Write(title), FadeIn(legend), Create(status_box), Write(status_text))
        self.wait(0.5)

        # --- ALGORITHM LOGIC ---

        # Data Structures
        pq = []
        visited = set()
        mst_edges = []

        # Function to update PQ display
        def update_pq_display():
            new_display = VGroup()
            # Show only top 6 items
            sorted_pq = sorted(pq)[:6]
            for w, u, v in sorted_pq:
                entry = Text(f"{u}-{v}: {w}", font_size=20, color=YELLOW)
                new_display.add(entry)

            if len(pq) > 6:
                new_display.add(Text("...", font_size=20, color=GRAY))

            new_display.arrange(DOWN, aligned_edge=LEFT).next_to(pq_title, DOWN)
            return new_display

        self.play(Write(pq_title))
        self.wait(0.5)

        # Start with node A
        start_node = "A"

        # Raw Data for logic
        raw_graph_data = {
            "A": [("B", 12), ("D", 8), ("E", 14)],
            "B": [("A", 12), ("C", 3), ("E", 15), ("G", 5)],
            "C": [("B", 3), ("D", 5), ("E", 2), ("G", 5)],
            "D": [("A", 8), ("C", 5)],
            "E": [("A", 14), ("B", 15), ("C", 2), ("G", 4)],
            "G": [("B", 5), ("C", 5), ("E", 4)]
        }

        # Animation Start
        self.play(
            g.vertices[start_node].animate.set_color(COLOR_VISITED),
            Transform(status_text, Text(f"Starting with {start_node}", font_size=24).move_to(status_box))
        )
        self.wait(0.5)
        visited.add(start_node)

        # Helper to add neighbors
        def add_neighbors(node):
            added_any = False
            for neighbor, weight in raw_graph_data[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, node, neighbor))
                    # Highlight edge candidate
                    edge_key = tuple(sorted((node, neighbor)))
                    if edge_key in g.edges:
                        self.play(g.edges[edge_key].animate.set_color(COLOR_EDGE_CANDIDATE), run_time=0.2)
                    added_any = True

            if added_any:
                new_pq_viz = update_pq_display()
                self.play(Transform(pq_list_display, new_pq_viz), run_time=0.5)
                self.wait(0.5)

        add_neighbors(start_node)

        # WHILE LOOP
        while pq:
            # 1. Pop minimum
            w, u, v = heapq.heappop(pq)
            edge_key = tuple(sorted((u, v)))

            new_pq_viz = update_pq_display()

            # Animation "Checking"
            self.play(
                Transform(pq_list_display, new_pq_viz),
                g.edges[edge_key].animate.set_color(COLOR_EDGE_CHECKING).set_stroke(width=6),
                Transform(status_text,
                          Text(f"Checking {u}-{v} (weight {w})...", font_size=24, color=YELLOW).move_to(status_box)),
                run_time=0.8
            )
            self.wait(0.5)

            # 2. Logic
            if v in visited:
                # Cycle detected
                self.play(
                    Transform(status_text,
                              Text(f"Node {v} already visited. Skipping.", font_size=24, color=RED).move_to(
                                  status_box)),
                    g.edges[edge_key].animate.set_color(GRAY).set_stroke(width=2).set_opacity(0.3),
                    run_time=0.8
                )
                self.wait(0.5)
            else:
                # Add to MST
                visited.add(v)
                mst_edges.append(edge_key)

                self.play(
                    Transform(status_text, Text(f"Adding {v} to MST!", font_size=24, color=GREEN).move_to(status_box)),
                    g.edges[edge_key].animate.set_color(COLOR_EDGE_MST).set_stroke(width=6),
                    g.vertices[v].animate.set_color(COLOR_VISITED),
                    run_time=1
                )
                self.wait(0.5)

                # Add new neighbors
                self.play(
                    Transform(status_text, Text(f"Finding neighbors of {v}...", font_size=24).move_to(status_box)))
                add_neighbors(v)

            self.wait(0.2)

        # Final
        self.play(
            Transform(status_text, Text("MST built successfully!", font_size=24, color=TEAL).move_to(status_box)),
            run_time=2
        )
        self.wait(3)