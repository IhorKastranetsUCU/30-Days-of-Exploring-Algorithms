from manim import *


# --- Клас DisjointSet (Логіка) ---
class DisjointSet():
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1, root2 = self.find(v1), self.find(v2)
        if root1 == root2:
            return False
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        return True


class KruskalVis(Scene):
    def construct(self):
        # --- 0. Константи та Стиль ---
        # Тепер заливка чорна, щоб ноди виглядали "порожніми"
        NODE_FILL_COLOR = BLACK
        NODE_STROKE_COLOR = "#7FFFD4"  # Аквамарин (початковий контур)
        TEXT_FONT = "Times New Roman"

        # --- 1. Заголовок ---
        main_title = Text("Kruskal's Algorithm", font=TEXT_FONT, font_size=48, color=TEAL)
        main_title.to_edge(UP, buff=0.5)
        self.add(main_title)

        # --- 2. Дані Графа ---
        graph_data = {
            "A": [("B", 12), ("D", 8), ("E", 14)],
            "B": [("A", 12), ("C", 3), ("E", 15), ("G", 5)],
            "C": [("B", 3), ("D", 5), ("E", 2), ("G", 5)],
            "D": [("A", 8), ("C", 5)],
            "E": [("A", 14), ("B", 15), ("C", 2), ("G", 4)],
            "G": [("B", 5), ("C", 5), ("E", 4)]
        }

        scale_factor = 1.3
        layout = {
            "A": [-3.5 * scale_factor, 2 * scale_factor, 0],
            "B": [-0.5 * scale_factor, 2 * scale_factor, 0],
            "D": [-3.5 * scale_factor, -1 * scale_factor, 0],
            "C": [-1 * scale_factor, -1 * scale_factor, 0],
            "E": [0, 0.5 * scale_factor, 0],
            "G": [2 * scale_factor, 0, 0],
        }

        vertices = list(graph_data.keys())
        edges_unsorted = []
        seen_edges = set()
        for u, neighbors in graph_data.items():
            for v, w in neighbors:
                edge_pair = tuple(sorted((u, v)))
                if edge_pair not in seen_edges:
                    edges_unsorted.append((u, v, w))
                    seen_edges.add(edge_pair)

        edges_sorted = sorted(edges_unsorted, key=lambda x: x[2])

        # --- 3. Створення Графа ---

        labels_dict = {}
        for v in vertices:
            labels_dict[v] = Text(v, font=TEXT_FONT, font_size=36, color=WHITE)

        g = Graph(
            vertices,
            [],
            layout=layout,
            vertex_config={
                "radius": 0.35,
                "color": NODE_STROKE_COLOR,  # Колір контуру
                "fill_color": NODE_FILL_COLOR,  # Чорна заливка
                "fill_opacity": 1,
                "stroke_width": 4  # Трохи товстіший контур, щоб було видно зміну кольору
            },
            labels=labels_dict
        )

        # Центрування
        g.shift(LEFT * 1.5 + DOWN * 1)

        self.play(FadeIn(g), run_time=0.7)

        # --- 4. Список Ребер ---

        list_x_pos = 4.5
        list_header_pos = UP * 2 + RIGHT * list_x_pos

        list_header = Text("Edges:", font_size=32, color=BLUE, font=TEXT_FONT).move_to(list_header_pos)
        self.play(Write(list_header), run_time=0.5)

        rows_dict = {}
        edges_visuals_dict = {}

        list_slots = []
        start_y = list_header.get_bottom()[1] - 0.4
        for i in range(len(edges_unsorted)):
            list_slots.append([list_x_pos, start_y - i * 0.45, 0])

        # --- 5. Поява ребер ---

        for i, (u, v, w) in enumerate(edges_unsorted):
            text_str = f"{u}-{v}: {w}"
            row_text = Text(text_str, font_size=24, font="Monospace", color=WHITE)
            row_text.move_to(list_slots[i])

            edge_key = tuple(sorted((u, v)))
            rows_dict[edge_key] = row_text

            edge_added = g.add_edges((u, v), edge_config={(u, v): {"stroke_color": GRAY, "stroke_width": 5}})
            edge_line = g.edges[(u, v)]

            weight_label = Text(str(w), font_size=20, font=TEXT_FONT, color=YELLOW).add_background_rectangle(opacity=1,
                                                                                                             buff=0.05,
                                                                                                             color=BLACK)
            weight_label.move_to(edge_line.get_center())

            edges_visuals_dict[edge_key] = VGroup(edge_line, weight_label)

            self.play(
                Create(edge_line),
                FadeIn(weight_label),
                Write(row_text),
                run_time=0.25
            )

        self.wait(0.5)

        # --- 6. Сортування ---

        sort_info = Text("Sort edges by weight", color=YELLOW, font_size=28, font=TEXT_FONT)
        sort_info.next_to(list_header, UP, buff=0.2)
        self.play(Write(sort_info))
        self.wait(0.5)

        animations = []
        for index, (u, v, w) in enumerate(edges_sorted):
            edge_key = tuple(sorted((u, v)))
            row_obj = rows_dict[edge_key]
            target_pos = list_slots[index]
            animations.append(row_obj.animate.move_to(target_pos))

        self.play(*animations, run_time=1.5)
        self.play(FadeOut(sort_info))
        self.wait(0.5)

        # --- 7. Алгоритм ---

        dsu = DisjointSet(vertices)

        arrow = Arrow(start=LEFT, end=RIGHT, color=YELLOW, buff=0.1, tip_length=0.15).scale(0.6)
        first_key = tuple(sorted((edges_sorted[0][0], edges_sorted[0][1])))
        arrow.next_to(rows_dict[first_key], LEFT)
        self.add(arrow)

        mst_edges_count = 0
        total_vertices = len(vertices)

        for i, (u, v, w) in enumerate(edges_sorted):
            edge_key = tuple(sorted((u, v)))
            row = rows_dict[edge_key]
            visual_edge = edges_visuals_dict[edge_key]
            line, label = visual_edge[0], visual_edge[1]

            # Вибір
            self.play(
                arrow.animate.next_to(row, LEFT),
                row.animate.set_color(YELLOW),
                line.animate.set_color(YELLOW).set_stroke(width=8),
                label.animate.set_color(YELLOW),
                run_time=0.5
            )

            # Перевірка DSU
            if dsu.union(u, v):
                mst_edges_count += 1
                self.play(
                    row.animate.set_color(GREEN),
                    line.animate.set_color(GREEN),
                    # Змінюємо ТІЛЬКИ контур (stroke) на зелений
                    g.vertices[u].animate.set_stroke(color=GREEN),
                    g.vertices[v].animate.set_stroke(color=GREEN),
                    run_time=0.5
                )
            else:
                self.play(
                    row.animate.set_color(RED),
                    line.animate.set_color(RED),
                    run_time=0.5
                )
                self.play(
                    row.animate.set_opacity(0.3).set_color(GRAY),
                    line.animate.set_opacity(0.2).set_color(GRAY).set_stroke(width=2),
                    label.animate.set_opacity(0.2),
                    run_time=0.5
                )

            if mst_edges_count == total_vertices - 1:
                remaining_anims = []
                for j in range(i + 1, len(edges_sorted)):
                    nk = tuple(sorted((edges_sorted[j][0], edges_sorted[j][1])))
                    remaining_anims.append(rows_dict[nk].animate.set_opacity(0.2))

                if remaining_anims:
                    self.play(*remaining_anims, run_time=1)
                break

        self.play(FadeOut(arrow))
        self.wait(2)