from manim import *


class FloydWarshallUltimate(Scene):
    def construct(self):
        # --- CONFIG ---
        inf = float('inf')

        # Colors
        C_BG = BLACK
        C_NODE = WHITE
        C_PIVOT = YELLOW  # For K highlights
        C_CHECK = ORANGE  # For current path segments (i->k, k->j)
        C_SUCCESS = GREEN  # For updates
        C_FAIL = RED_E  # For failed checks
        C_HEADER = BLUE
        C_CELL_STROKE = GRAY

        # --- DATA ---
        nodes_labels = ["A", "B", "C", "D", "E", "F"]
        n = 6
        node_map = {name: i for i, name in enumerate(nodes_labels)}

        raw_edges = [
            ["A", "B", 6],
            ["A", "C", 4],
            ["A", "D", 5],
            ["B", "E", -1],
            ["C", "B", 2],
            ["C", "E", 3],
            ["D", "C", -2],
            ["D", "F", -1],
            ["E", "F", 4],
            ["F", "C", -2],
            ["F", "A", 5]
        ]

        # Internal Structures
        dist = [[inf] * n for _ in range(n)]
        pred = [[None] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
            pred[i][i] = nodes_labels[i]

        edge_indices = []
        edge_lookup = {}  # Fast lookup for UI elements
        for u_str, v_str, w in raw_edges:
            u, v = node_map[u_str], node_map[v_str]
            dist[u][v] = w
            pred[u][v] = nodes_labels[u]
            edge_indices.append((u, v, w))
            edge_lookup[(u, v)] = w  # Mark existence

        # --- LAYOUT POSITIONS ---
        POS_LIST_X = -6.0
        POS_GRAPH_X = -2.0
        POS_MATRIX_X = 4.0

        # Tweaked positions to fit headers
        POS_TITLE = UP * 3.7           # Raised Title slightly
        POS_MATRIX_COST_Y = 1.7       # Lowered top matrix slightly
        POS_MATRIX_PRED_Y = -1.8       # Lowered bottom matrix slightly
        POS_CALC_BOX = DOWN * 3.5

        # --- 1. TITLE ---
        title = Text("Floyd-Warshall Algorithm", font_size=32).move_to(POS_TITLE)

        # --- 2. EDGE LIST (Left) ---
        list_group = VGroup()
        list_title = Text("Direct Edges:", font_size=18, color=C_HEADER)
        list_group.add(list_title)

        edge_list_items = {}  # (u, v) -> TextObject

        for u, v, w in edge_indices:
            txt = Text(f"{nodes_labels[u]} → {nodes_labels[v]} : {w}", font_size=16, color=GRAY)
            edge_list_items[(u, v)] = txt
            list_group.add(txt)

        list_group.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        list_group.move_to(RIGHT * POS_LIST_X)

        # --- 3. GRAPH (Center-Left) ---
        layout = {
            0: [-3.5, 2.0, 0],  # A
            1: [-3.5, -2.0, 0],  # B
            2: [-1.5, 0, 0],  # C
            3: [-1.5, 2.8, 0],  # D
            4: [0.5, -2.0, 0],  # E
            5: [0.5, 2.0, 0]  # F
        }
        # Adjust layout to center graph visually around POS_GRAPH_X
        for k in layout: layout[k] += LEFT * 0.5

        g = DiGraph(
            list(range(n)),
            [(u, v) for u, v, w in edge_indices],
            layout=layout,
            labels=False,
            vertex_config={"radius": 0.3, "color": C_NODE, "fill_color": BLACK, "fill_opacity": 1, "stroke_width": 2},
            edge_config={"color": GRAY, "stroke_width": 2, "stroke_opacity": 0.6, "tip_config": {"tip_length": 0.12}}
        )

        node_texts = VGroup()
        for i in range(n):
            node_texts.add(Text(nodes_labels[i], font_size=20, color=WHITE).move_to(layout[i]))

        edge_weights = VGroup()
        for u, v, w in edge_indices:
            edge_obj = g.edges[(u, v)]
            shift = UP * 0.15
            if (u, v) == (2, 1): shift = DOWN * 0.15
            txt = Integer(w).scale(0.4).move_to(edge_obj.get_center()).shift(shift)
            bg = BackgroundRectangle(txt, fill_opacity=1, color=BLACK, buff=0.05)
            edge_weights.add(VGroup(bg, txt))

        graph_group = VGroup(g, edge_weights, node_texts)

        # --- 4. MATRICES (Right) ---
        def create_matrix(data, name, center_pos):
            grp = VGroup()
            # Title relative to center - INCREASED HEIGHT (1.5 -> 1.85)
            t = Text(name, font_size=20, color=C_HEADER).move_to(center_pos + UP * 1.85)
            grp.add(t)

            cell_size = 0.40
            cells = {}

            # Headers
            for k in range(n):
                offset_x = (k - (n - 1) / 2) * cell_size
                offset_y = ((n - 1) / 2 - k) * cell_size

                h_top = Text(nodes_labels[k], font_size=12, color=YELLOW).move_to(
                    center_pos + RIGHT * offset_x + UP * ((n) / 2 * cell_size + 0.15))
                h_left = Text(nodes_labels[k], font_size=12, color=YELLOW).move_to(
                    center_pos + LEFT * ((n) / 2 * cell_size + 0.15) + UP * offset_y)
                grp.add(h_top, h_left)

            for r in range(n):
                for c in range(n):
                    x_offset = (c - (n - 1) / 2) * cell_size
                    y_offset = ((n - 1) / 2 - r) * cell_size
                    pos = center_pos + RIGHT * x_offset + UP * y_offset

                    val = data[r][c]
                    val_str = "∞" if val == inf else str(val)
                    if val is None: val_str = "-"

                    bg = Square(side_length=cell_size, stroke_width=1, stroke_color=C_CELL_STROKE, fill_color=BLACK,
                                fill_opacity=1)
                    bg.move_to(pos)

                    col = WHITE
                    if r == c: col = GRAY
                    txt = Text(val_str, font_size=12, color=col).move_to(pos)

                    cells[(r, c)] = {"bg": bg, "txt": txt}
                    grp.add(bg, txt)
            return grp, cells

        cost_grp, cost_cells = create_matrix(dist, "Costs", RIGHT * POS_MATRIX_X + UP * POS_MATRIX_COST_Y)
        pred_grp, pred_cells = create_matrix(pred, "Predecessors", RIGHT * POS_MATRIX_X + UP * POS_MATRIX_PRED_Y)

        # --- 5. CALCULATION BOX ---
        calc_box_rect = Rectangle(width=13, height=0.8, color=BLUE).move_to(POS_CALC_BOX)
        calc_text = Text("Ready", font_size=18).move_to(calc_box_rect)
        calc_group = VGroup(calc_box_rect, calc_text)

        # Info about K
        k_info = Text("", font_size=20, color=C_PIVOT).next_to(title, DOWN)

        # --- ANIMATION START ---
        self.play(
            Write(title),
            FadeIn(list_group),
            FadeIn(graph_group),
            FadeIn(cost_grp), FadeIn(pred_grp),
            FadeIn(calc_group)
        )

        # --- MAIN ALGORITHM ---
        for k in range(n):
            # Phase Start
            self.play(
                Transform(k_info,
                          Text(f"Pivot K = {nodes_labels[k]}", font_size=20, color=C_PIVOT).next_to(title, DOWN)),
                g.vertices[k].animate.set_stroke(color=C_PIVOT, width=6),
                run_time=0.4
            )

            # Highlight Pivot Cross (Row K & Col K) in BOTH matrices
            pivot_anims = []
            for idx in range(n):
                pivot_anims.append(cost_cells[(k, idx)]["bg"].animate.set_fill(C_PIVOT, opacity=0.2))
                pivot_anims.append(cost_cells[(idx, k)]["bg"].animate.set_fill(C_PIVOT, opacity=0.2))
                pivot_anims.append(pred_cells[(k, idx)]["bg"].animate.set_fill(C_PIVOT, opacity=0.2))
                pivot_anims.append(pred_cells[(idx, k)]["bg"].animate.set_fill(C_PIVOT, opacity=0.2))

            self.play(*pivot_anims, run_time=0.3)

            for i in range(n):
                for j in range(n):
                    # Values
                    d_ik = dist[i][k]
                    d_kj = dist[k][j]
                    d_ij = dist[i][j]

                    # 1. PREPARE HIGHLIGHTS (Visual Check)
                    anims_on = []

                    # Helper for edges
                    def highlight_edge_segment(u, v):
                        if (u, v) in edge_list_items:
                            anims_on.append(edge_list_items[(u, v)].animate.set_color(C_CHECK))
                        if (u, v) in g.edges:
                            anims_on.append(g.edges[(u, v)].animate.set_color(C_CHECK).set_stroke(width=4))

                    highlight_edge_segment(i, k)
                    highlight_edge_segment(k, j)

                    # Matrix Input Cells (i,k) and (k,j)
                    anims_on.append(cost_cells[(i, k)]["bg"].animate.set_stroke(C_CHECK, width=3))
                    anims_on.append(cost_cells[(k, j)]["bg"].animate.set_stroke(C_CHECK, width=3))
                    anims_on.append(pred_cells[(i, k)]["bg"].animate.set_stroke(C_CHECK, width=3))
                    anims_on.append(pred_cells[(k, j)]["bg"].animate.set_stroke(C_CHECK, width=3))

                    # Also Highlight Target (i, j) to show where result goes
                    anims_on.append(cost_cells[(i, j)]["bg"].animate.set_stroke(C_HEADER, width=3))

                    # Formula Text
                    v_ik = "∞" if d_ik == inf else str(d_ik)
                    v_kj = "∞" if d_kj == inf else str(d_kj)
                    v_ij = "∞" if d_ij == inf else str(d_ij)
                    v_sum = "∞" if (d_ik == inf or d_kj == inf) else str(d_ik + d_kj)

                    txt_check = Text(
                        f"Check {nodes_labels[i]}->{nodes_labels[k]}->{nodes_labels[j]} : {v_ik} + {v_kj} = {v_sum} < {v_ij} ?",
                        font_size=18).move_to(calc_box_rect)

                    # EXECUTE HIGHLIGHT
                    self.play(*anims_on, Transform(calc_text, txt_check), run_time=0.05)

                    # 2. LOGIC
                    if d_ik != inf and d_kj != inf and d_ik + d_kj < d_ij:
                        # UPDATE
                        new_val = d_ik + d_kj
                        dist[i][j] = new_val
                        pred[i][j] = pred[k][j]

                        # Prepare Success Text
                        res_txt = Text("Update!", font_size=18, color=C_SUCCESS).next_to(txt_check, RIGHT, buff=0.5)

                        # Prepare Value Changes
                        t_cost_new = Text(str(new_val), font_size=12, color=C_SUCCESS).move_to(
                            cost_cells[(i, j)]["txt"])
                        t_pred_new = Text(str(pred[i][j]), font_size=12, color=C_SUCCESS).move_to(
                            pred_cells[(i, j)]["txt"])

                        self.play(
                            FadeIn(res_txt),
                            # Update Text
                            Transform(cost_cells[(i, j)]["txt"], t_cost_new),
                            Transform(pred_cells[(i, j)]["txt"], t_pred_new),
                            # Green BG
                            cost_cells[(i, j)]["bg"].animate.set_fill(C_SUCCESS, opacity=0.4),
                            pred_cells[(i, j)]["bg"].animate.set_fill(C_SUCCESS, opacity=0.4),
                            run_time=0.4
                        )

                        self.wait(0.5)  # PAUSE ON UPDATE

                        # Revert Update Styling
                        self.play(
                            FadeOut(res_txt),
                            cost_cells[(i, j)]["bg"].animate.set_fill(BLACK, opacity=1),
                            pred_cells[(i, j)]["bg"].animate.set_fill(BLACK, opacity=1),
                        )

                    else:
                        # NO UPDATE
                        res_txt = Text("False", font_size=18, color=C_FAIL).next_to(txt_check, RIGHT, buff=0.5)
                        self.add(res_txt)
                        self.wait(0.05)
                        self.remove(res_txt)

                    # 3. CLEANUP HIGHLIGHTS
                    anims_off = []

                    # Reset edges
                    def reset_edge_segment(u, v):
                        if (u, v) in edge_list_items:
                            anims_off.append(edge_list_items[(u, v)].animate.set_color(GRAY))
                        if (u, v) in g.edges:
                            anims_off.append(g.edges[(u, v)].animate.set_color(GRAY).set_stroke(width=2))

                    reset_edge_segment(i, k)
                    reset_edge_segment(k, j)

                    # Reset Matrix strokes
                    anims_off.append(cost_cells[(i, k)]["bg"].animate.set_stroke(C_CELL_STROKE, width=1))
                    anims_off.append(cost_cells[(k, j)]["bg"].animate.set_stroke(C_CELL_STROKE, width=1))
                    anims_off.append(pred_cells[(i, k)]["bg"].animate.set_stroke(C_CELL_STROKE, width=1))
                    anims_off.append(pred_cells[(k, j)]["bg"].animate.set_stroke(C_CELL_STROKE, width=1))
                    anims_off.append(cost_cells[(i, j)]["bg"].animate.set_stroke(C_CELL_STROKE, width=1))

                    self.play(*anims_off, run_time=0.05)

            # End of Phase K - Cleanup Pivot
            pivot_cleanup = [g.vertices[k].animate.set_stroke(color=C_NODE, width=2)]
            for idx in range(n):
                pivot_cleanup.append(cost_cells[(k, idx)]["bg"].animate.set_fill(BLACK, opacity=1))
                pivot_cleanup.append(cost_cells[(idx, k)]["bg"].animate.set_fill(BLACK, opacity=1))
                pivot_cleanup.append(pred_cells[(k, idx)]["bg"].animate.set_fill(BLACK, opacity=1))
                pivot_cleanup.append(pred_cells[(idx, k)]["bg"].animate.set_fill(BLACK, opacity=1))

            self.play(*pivot_cleanup, run_time=0.3)

        # --- FINAL ---
        self.play(
            FadeOut(k_info),
            Transform(calc_text, Text("Done!", font_size=20, color=C_SUCCESS).move_to(calc_box_rect))
        )
        self.wait(3)