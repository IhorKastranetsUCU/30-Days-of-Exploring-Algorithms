from manim import *
import numpy as np


class HeapSortVisual(Scene):
    def construct(self):
        # --- Вхідні дані ---
        self.data_values = [18, 15, 6, 14, 3, 16, 19, 9, 7]

        # --- Налаштування вигляду ---
        self.node_radius = 0.35
        self.array_buff = 0.1

        # ЗМІНА 1: Опускаємо граф нижче (було 3.2, стало 2.2)
        self.tree_y_start = 2.2
        self.level_height = 1.2

        # --- Створення об'єктів ---

        # ЗМІНА 2: Тільки напис Heap Sort
        title = Text("Heap Sort", font_size=48).to_edge(UP)
        self.add(title)

        # 1. Створення візуального масиву (внизу)
        self.array_group = VGroup()
        for i, val in enumerate(self.data_values):
            square = Square(side_length=0.7)
            text = Integer(val).scale(0.8)
            cell = VGroup(square, text)
            self.array_group.add(cell)

        self.array_group.arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.5)

        # Індекси під масивом
        indices = VGroup()
        for i, cell in enumerate(self.array_group):
            idx = Integer(i, font_size=18, color=GRAY).next_to(cell, DOWN, buff=0.1)
            indices.add(idx)

        self.add(self.array_group, indices)

        # 2. Створення візуального дерева
        self.node_mobjects = [None] * len(self.data_values)
        self.tree_edges = VGroup()

        self.node_positions = self.get_tree_positions(len(self.data_values))

        # Малюємо ребра
        for i in range(len(self.data_values)):
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len(self.data_values):
                line = Line(self.node_positions[i], self.node_positions[l], color=GRAY, stroke_width=2)
                self.tree_edges.add(line)
            if r < len(self.data_values):
                line = Line(self.node_positions[i], self.node_positions[r], color=GRAY, stroke_width=2)
                self.tree_edges.add(line)
        self.add(self.tree_edges)

        # Малюємо вузли
        for i, val in enumerate(self.data_values):
            circle = Circle(radius=self.node_radius, color=WHITE, fill_color=BLACK, fill_opacity=1)
            text = Integer(val).scale(0.7)
            text.move_to(circle.get_center())
            node = VGroup(circle, text)
            node.move_to(self.node_positions[i])
            self.node_mobjects[i] = node
            self.add(node)

        self.wait(1)

        # --- Запуск Алгоритму ---

        # ЗМІНА 3: Прибрали всі зайві написи про статус

        n = len(self.data_values)
        for i in range(n // 2 - 1, -1, -1):
            self.visual_heapify(n, i)

        self.wait(1)

        for i in range(n - 1, 0, -1):
            self.visual_swap(0, i)

            self.play(
                self.node_mobjects[i][0].animate.set_stroke(color=GREEN),
                self.array_group[i][0].animate.set_stroke(color=GREEN),
                run_time=0.3
            )

            self.visual_heapify(i, 0)

        self.play(
            self.node_mobjects[0][0].animate.set_stroke(color=GREEN),
            self.array_group[0][0].animate.set_stroke(color=GREEN),
            run_time=0.5
        )

        self.wait(2)

    def get_tree_positions(self, n):
        positions = {}
        level_width = 12

        for i in range(n):
            level = int(np.log2(i + 1))
            items_in_level = 2 ** level
            pos_in_level = i - (items_in_level - 1)

            width_chunk = level_width / (items_in_level + 1)
            x = - (level_width / 2) + (pos_in_level + 1) * width_chunk

            # Використовуємо self.tree_y_start, який ми опустили
            y = self.tree_y_start - (level * self.level_height)

            positions[i] = [x, y, 0]
        return positions

    def visual_swap(self, i, j):
        self.data_values[i], self.data_values[j] = self.data_values[j], self.data_values[i]

        node_i = self.node_mobjects[i]
        node_j = self.node_mobjects[j]
        pos_i = self.node_positions[i]
        pos_j = self.node_positions[j]

        arr_i = self.array_group[i]
        arr_j = self.array_group[j]

        self.play(
            node_i.animate.move_to(pos_j),
            node_j.animate.move_to(pos_i),
            arr_i.animate.move_to(arr_j.get_center()),
            arr_j.animate.move_to(arr_i.get_center()),
            run_time=0.6
        )

        self.node_mobjects[i], self.node_mobjects[j] = self.node_mobjects[j], self.node_mobjects[i]
        self.array_group[i], self.array_group[j] = self.array_group[j], self.array_group[i]

    def visual_heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        self.play(self.node_mobjects[i][0].animate.set_fill(color=BLUE, opacity=0.5), run_time=0.2)

        if l < n:
            self.play(Indicate(self.node_mobjects[l][0], color=YELLOW, scale_factor=1.1), run_time=0.2)
            if self.data_values[l] > self.data_values[largest]:
                largest = l

        if r < n:
            self.play(Indicate(self.node_mobjects[r][0], color=YELLOW, scale_factor=1.1), run_time=0.2)
            if self.data_values[r] > self.data_values[largest]:
                largest = r

        if largest != i:
            self.visual_swap(i, largest)
            self.play(self.node_mobjects[largest][0].animate.set_fill(color=BLACK, opacity=1), run_time=0.1)
            self.visual_heapify(n, largest)
        else:
            self.play(self.node_mobjects[i][0].animate.set_fill(color=BLACK, opacity=1), run_time=0.1)