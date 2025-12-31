from manim import *


class DSU_All_In_One(Scene):
    def construct(self):
        # Константи та налаштування
        self.vertices = [0, 1, 2, 3, 4, 5, 6, 7]
        self.node_radius = 0.35
        self.spacing_x = 1.0
        self.level_height = 1.5

        # ЧАС ЗАТРИМКИ (змінено на 0.6)
        self.DELAY = 0.6

        # Список операцій
        self.operations = [(3, 2), (1, 4), (4, 2), (5, 0), (0, 1), (7, 2), (1, 6)]

        # --- ЧАСТИНА 1: NAIVE ---
        self.setup_scene("1. Naive Implementation")
        self.run_naive()
        self.clear_screen_transition()

        # --- ЧАСТИНА 2: UNION BY SIZE ---
        self.setup_scene("2. Union by Size (Small -> Large)")
        self.run_size()
        self.clear_screen_transition()

        # --- ЧАСТИНА 3: FULL COMPRESSION ---
        self.setup_scene("3. Full Compression (Flatten on Union)")
        self.run_compression()

        self.wait(2)

    # ==========================================
    #      МЕТОДИ НАЛАШТУВАННЯ ТА ОЧИЩЕННЯ
    # ==========================================

    def setup_scene(self, title_text):
        self.parent = {i: i for i in self.vertices}
        self.rank = {i: 0 for i in self.vertices}
        self.size = {i: 1 for i in self.vertices}
        self.v_nodes = {}
        self.v_arrows = {}

        self.title = Text(title_text, font_size=36).to_edge(UP)
        self.add(self.title)

        self.func_text = Text("Start", font_size=28, color=YELLOW).to_corner(DR).shift(UP * 0.5 + LEFT * 0.5)
        self.add(self.func_text)

        start_x = -(len(self.vertices) - 1) * self.spacing_x / 2
        initial_y = 2.5

        for i, val in enumerate(self.vertices):
            pos = np.array([start_x + i * self.spacing_x, initial_y, 0])
            circle = Circle(radius=self.node_radius, color=TEAL, fill_opacity=0.5, stroke_width=4)
            label = Text(str(val), font_size=24)
            node_group = VGroup(circle, label).move_to(pos)
            node_group.z_index = 10
            self.v_nodes[val] = node_group
            self.add(node_group)

    def clear_screen_transition(self):
        self.wait(1)
        self.clear()
        self.wait(1)

    def update_status(self, text):
        self.func_text.become(
            Text(text, font_size=28, color=YELLOW).to_corner(DR).shift(UP * 0.5 + LEFT * 0.5)
        )

    # ==========================================
    #          ВІЗУАЛЬНІ ЕФЕКТИ
    # ==========================================

    def add_visual_connection(self, child, parent):
        if child in self.v_arrows:
            self.remove(self.v_arrows[child])

        arrow = always_redraw(lambda c=child, p=parent: Arrow(
            start=self.v_nodes[c].get_top(),
            end=self.v_nodes[p].get_bottom(),
            buff=0.05,
            color=WHITE,
            max_tip_length_to_length_ratio=0.15,
            stroke_width=3
        ))
        self.v_arrows[child] = arrow
        self.add(arrow)

    def rearrange_tree(self):
        roots = [i for i in self.vertices if self.parent[i] == i]
        adj = {i: [] for i in self.vertices}
        for node, par in self.parent.items():
            if node != par:
                adj[par].append(node)

        subtree_width = {}

        def get_width(node):
            if not adj[node]:
                subtree_width[node] = 1
                return 1
            width = sum(get_width(child) for child in adj[node])
            subtree_width[node] = width
            return width

        for r in roots: get_width(r)

        new_positions = {}
        total_width = sum(subtree_width[r] for r in roots)
        current_x = - (total_width * self.spacing_x) / 2

        def assign_pos(node, x_start, depth):
            my_width = subtree_width[node]
            center_x = x_start + (my_width * self.spacing_x) / 2
            pos_y = 2.5 - depth * self.level_height
            new_positions[node] = np.array([center_x, pos_y, 0])

            child_x_start = x_start
            for child in adj[node]:
                w = subtree_width[child]
                assign_pos(child, child_x_start, depth + 1)
                child_x_start += w * self.spacing_x

        for r in roots:
            assign_pos(r, current_x, 0)
            current_x += subtree_width[r] * self.spacing_x

        anims = []
        for node_id, target_pos in new_positions.items():
            anims.append(self.v_nodes[node_id].animate.move_to(target_pos))

        if anims:
            # Анімація руху вершин триває 0.6 с
            self.play(*anims, run_time=self.DELAY)

    def reset_colors(self):
        self.play(
            *[self.v_nodes[i][0].animate.set_color(TEAL) for i in self.vertices],
            run_time=0.3
        )

    def find_visual(self, x):
        curr = x
        self.v_nodes[curr][0].set_color(YELLOW)
        while self.parent[curr] != curr:
            curr = self.parent[curr]
            self.v_nodes[curr][0].set_color(YELLOW)
        return curr

    def find_simple(self, x):
        curr = x
        while self.parent[curr] != curr:
            curr = self.parent[curr]
        return curr

    # ==========================================
    #        ЛОГІКА АЛГОРИТМІВ
    # ==========================================

    def run_naive(self):
        for x, y in self.operations:
            self.update_status(f"union({x}, {y})")
            root_x = self.find_visual(x)
            root_y = self.find_visual(y)

            if root_x != root_y:
                self.parent[root_y] = root_x
                self.add_visual_connection(root_y, root_x)
                self.rearrange_tree()
                # ДОДАНО: Затримка після зміни структури
                self.wait(self.DELAY)

            self.reset_colors()

    def run_size(self):
        for x, y in self.operations:
            self.update_status(f"union({x}, {y})")
            root_x = self.find_visual(x)
            root_y = self.find_visual(y)

            if root_x != root_y:
                if self.size[root_x] < self.size[root_y]:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]
                    self.add_visual_connection(root_x, root_y)
                else:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                    self.add_visual_connection(root_y, root_x)

                self.rearrange_tree()
                # ДОДАНО: Затримка після зміни структури
                self.wait(self.DELAY)
            else:
                # ЗМІНЕНО: 0.3 -> 0.6
                self.wait(self.DELAY)

            self.reset_colors()

    def run_compression(self):
        for x, y in self.operations:
            self.update_status(f"union({x}, {y})")
            root_x = self.find_visual(x)
            root_y = self.find_visual(y)

            if root_x != root_y:
                if self.rank[root_x] < self.rank[root_y]:
                    self.flatten_and_union(child_root=root_x, new_main_root=root_y)
                elif self.rank[root_x] > self.rank[root_y]:
                    self.flatten_and_union(child_root=root_y, new_main_root=root_x)
                else:
                    self.flatten_and_union(child_root=root_y, new_main_root=root_x)
                    self.rank[root_x] += 1
            else:
                # ЗМІНЕНО: 0.3 -> 0.6
                self.wait(self.DELAY)

            self.reset_colors()

    def flatten_and_union(self, child_root, new_main_root):
        nodes_to_move = []
        for i in self.vertices:
            if self.find_simple(i) == child_root:
                nodes_to_move.append(i)

        # ЗМІНЕНО: run_time 0.3 -> 0.6 для підсвічування зеленим
        self.play(
            *[self.v_nodes[n][0].animate.set_color(GREEN) for n in nodes_to_move],
            run_time=self.DELAY
        )

        for node in nodes_to_move:
            self.parent[node] = new_main_root
            self.add_visual_connection(node, new_main_root)

        self.rearrange_tree()
        # ДОДАНО: Затримка після стиснення шляхів
        self.wait(self.DELAY)