from manim import *
import numpy as np


# --- КЛАСИ АЛГОРИТМУ ---

class Edge:
    def __init__(self, to, cap, rev, max_cap=None):
        self.to = to
        self.cap = cap  # Залишкова ємність
        self.rev = rev  # Індекс зворотнього ребра
        self.max_cap = max_cap if max_cap is not None else cap  # Початкова ємність


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.ptr = [0] * n
        self.animation_steps = []

    def add_edge(self, u, v, cap):
        # Пряме ребро: має max_cap > 0
        forward = Edge(v, cap, len(self.graph[v]), max_cap=cap)
        # Зворотнє ребро: має max_cap = 0
        backward = Edge(u, 0, len(self.graph[u]), max_cap=0)

        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for edge in self.graph[u]:
                if self.level[edge.to] == -1 and edge.cap > 0:
                    self.level[edge.to] = self.level[u] + 1
                    queue.append(edge.to)
        return self.level[t] != -1

    def dfs(self, u, t, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed

        while self.ptr[u] < len(self.graph[u]):
            edge = self.graph[u][self.ptr[u]]

            if self.level[edge.to] == self.level[u] + 1 and edge.cap > 0:
                tr = self.dfs(edge.to, t, min(pushed, edge.cap))
                if tr > 0:
                    # Оновлюємо залишкові ємності
                    edge.cap -= tr
                    self.graph[edge.to][edge.rev].cap += tr

                    # --- ВИПРАВЛЕНА ЛОГІКА ДЛЯ MANIM ---

                    # Визначаємо, це пряме ребро чи зворотнє
                    if edge.max_cap > 0:
                        # Це пряме ребро (u -> v)
                        visual_u, visual_v = u, edge.to
                        forward_edge = edge
                    else:
                        # Це зворотнє ребро (u -> v), отже візуально це (v -> u)
                        visual_u, visual_v = edge.to, u
                        # Знаходимо відповідне пряме ребро, щоб дізнатися його стан
                        forward_edge = self.graph[edge.to][edge.rev]

                    # Обчислюємо поточний потік на прямому ребрі
                    current_flow = forward_edge.max_cap - forward_edge.cap

                    self.animation_steps.append({
                        "type": "flow_update",
                        "u": visual_u,  # Завжди використовуємо координати прямого ребра
                        "v": visual_v,
                        "text": f"{current_flow}/{forward_edge.max_cap}"
                    })

                    return tr
            self.ptr[u] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed
        return flow


# --- ВІЗУАЛІЗАЦІЯ ---

class DinicVisualizer(Scene):
    def construct(self):
        # 1. Ініціалізація
        dinic_solver = Dinic(7)

        edges_data = [
            (0, 1, 12), (0, 2, 27), (0, 3, 5),
            (1, 4, 15), (1, 5, 8),
            (2, 4, 10), (2, 6, 9),
            (3, 2, 14), (3, 5, 6),
            (4, 6, 13),
            (5, 6, 20)
        ]

        for u, v, cap in edges_data:
            dinic_solver.add_edge(u, v, cap)

        # 2. Розрахунок (збір кроків)
        max_flow_value = dinic_solver.max_flow(0, 6)

        # 3. Графічне відображення
        # Позиції для вершин (S=0 зліва, T=6 справа)
        node_positions = {
            0: LEFT * 5,
            1: LEFT * 2 + UP * 2,
            2: LEFT * 2,
            3: LEFT * 2 + DOWN * 2,
            4: RIGHT * 2 + UP * 1.5,
            5: RIGHT * 2 + DOWN * 1.5,
            6: RIGHT * 5
        }

        # Побудова графа
        vertices = [0, 1, 2, 3, 4, 5, 6]
        edges = [(u, v) for u, v, cap in edges_data]

        graph = DiGraph(
            vertices,
            edges,
            layout=node_positions,
            labels=True,
            vertex_config={"radius": 0.4, "color": BLUE, "fill_opacity": 0.8},
            edge_config={"color": GREY, "stroke_width": 2}
        )

        # Створення міток 0/Cap
        edge_labels = {}
        for u, v, cap in edges_data:
            # Обчислення позиції тексту (трохи зсунуто від центру ребра)
            p1 = node_positions[u]
            p2 = node_positions[v]
            center = (p1 + p2) / 2
            direction = p2 - p1
            # Вектор перпендикулярний до ребра
            perp = np.array([-direction[1], direction[0], 0])
            norm = np.linalg.norm(perp)
            if norm != 0:
                perp = perp / norm * 0.4

            label = Text(f"0/{cap}", font_size=18, color=WHITE).move_to(center + perp)
            edge_labels[(u, v)] = label

        # 4. Анімація сцени
        self.play(Create(graph), run_time=1.5)
        self.play(*[Write(l) for l in edge_labels.values()], run_time=1)

        title = Text(f"Dinic Algorithm Max Flow", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 5. Програвання записаних кроків
        flow_color = YELLOW

        for step in dinic_solver.animation_steps:
            if step["type"] == "flow_update":
                u, v = step["u"], step["v"]
                new_text_str = step["text"]

                # Ключ (u, v) тепер точно існує в edge_labels завдяки виправленню в dfs
                old_label = edge_labels[(u, v)]
                new_label = Text(new_text_str, font_size=18, color=flow_color)
                new_label.move_to(old_label.get_center())

                edge_mobject = graph.edges[(u, v)]

                self.play(
                    Transform(old_label, new_label),
                    Indicate(edge_mobject, color=flow_color, scale_factor=1.1),
                    run_time=0.4
                )

                # Оновлюємо посилання в словнику на новий об'єкт
                edge_labels[(u, v)] = new_label

        # Фінальний результат
        result_text = Text(f"Max Flow: {max_flow_value}", font_size=40, color=GREEN)
        result_text.next_to(title, DOWN)
        self.play(Write(result_text))
        self.wait(3)