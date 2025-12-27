import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


def create_centered_viz(s):
    alphabet = [chr(i + 97) for i in range(26)]
    char_indices_map = {ch: [] for ch in alphabet}
    for idx, ch in enumerate(s):
        char_indices_map[ch].append(idx)

    steps = []
    current_counts = [0] * 26

    # Початкова пауза
    for _ in range(5):
        steps.append(
            {'phase': 'init', 'counts': [0] * 26, 'highlight_input_idxs': [], 'highlight_alpha_idx': -1, 'left': "",
             'middle': "", 'right': "", 'info': "Start: Analyzing input string..."})

    # ЕТАП 1: Підрахунок
    for i, char in enumerate(s):
        alpha_idx = ord(char) - 97
        current_counts[alpha_idx] += 1
        for _ in range(2):
            steps.append({'phase': 'counting', 'counts': list(current_counts), 'highlight_input_idxs': [i],
                          'highlight_alpha_idx': alpha_idx, 'left': "", 'middle': "", 'right': "",
                          'info': f"Counting '{char}'..."})

    # ЕТАП 2: Конструкція
    left_part = ""
    middle_char = ""
    for _ in range(5):
        steps.append({'phase': 'scanning_empty', 'counts': list(current_counts), 'highlight_input_idxs': [],
                      'highlight_alpha_idx': -1, 'left': "", 'middle': "", 'right': "",
                      'info': "Frequency map ready. Starting A-Z scan..."})

    for i in range(26):
        count = current_counts[i]
        char = alphabet[i]
        input_indices = char_indices_map[char]

        if count == 0:
            steps.append({'phase': 'scanning_empty', 'counts': list(current_counts), 'highlight_input_idxs': [],
                          'highlight_alpha_idx': i, 'left': left_part, 'middle': middle_char, 'right': "",
                          'info': f"Scanning '{char}': 0 found (Skip)"})
        else:
            # Підсвітка
            for _ in range(6):
                steps.append(
                    {'phase': 'scanning_found', 'counts': list(current_counts), 'highlight_input_idxs': input_indices,
                     'highlight_alpha_idx': i, 'left': left_part, 'middle': middle_char, 'right': "",
                     'info': f"Processing '{char}': Found {count} occurences!"})

            pairs = count // 2
            is_odd = (count % 2 == 1)

            # Перенесення пар
            if pairs > 0:
                left_part += char * pairs
                current_counts[i] -= (pairs * 2)
                for _ in range(8):
                    steps.append(
                        {'phase': 'building', 'counts': list(current_counts), 'highlight_input_idxs': input_indices,
                         'highlight_alpha_idx': i, 'left': left_part, 'middle': middle_char, 'right': "",
                         'info': f"Moved {pairs} pair(s) of '{char}' to result"})

            # Середній елемент
            if is_odd:
                for _ in range(4):
                    steps.append(
                        {'phase': 'middle_check', 'counts': list(current_counts), 'highlight_input_idxs': input_indices,
                         'highlight_alpha_idx': i, 'left': left_part, 'middle': middle_char, 'right': "",
                         'info': f"Odd count for '{char}'. Set as CENTER."})
                middle_char = char
                current_counts[i] = 0
                for _ in range(5):
                    steps.append(
                        {'phase': 'middle_set', 'counts': list(current_counts), 'highlight_input_idxs': input_indices,
                         'highlight_alpha_idx': i, 'left': left_part, 'middle': middle_char, 'right': "",
                         'info': f"Center updated to '{char}'"})

    # ЕТАП 3: Дзеркалення
    right_part = left_part[::-1]
    for _ in range(6):
        steps.append({'phase': 'mirroring_wait', 'counts': list(current_counts), 'highlight_input_idxs': [],
                      'highlight_alpha_idx': -1, 'left': left_part, 'middle': middle_char, 'right': "",
                      'info': "Left side ready. Mirroring..."})
    for _ in range(10):
        steps.append({'phase': 'mirroring_done', 'counts': list(current_counts), 'highlight_input_idxs': [],
                      'highlight_alpha_idx': -1, 'left': left_part, 'middle': middle_char, 'right': right_part,
                      'info': "PALINDROME COMPLETE"})

    # --- ВІЗУАЛІЗАЦІЯ (Оновлена) ---
    fig, ax = plt.subplots(figsize=(12, 8))  # Трохи збільшив висоту

    # Константи для центрування
    VISUAL_CENTER = 12.5  # Центр алфавітної стрічки (0-25)
    input_len = len(s)
    # Розрахунок стартової позиції X для вхідного рядка, щоб він був по центру
    input_start_x = VISUAL_CENTER - (input_len / 2.0)

    def update(frame_idx):
        ax.clear()
        ax.set_xlim(-1, 27)
        ax.set_ylim(-1, 7)  # Розширили межі по Y
        ax.axis('off')

        step = steps[frame_idx]

        # --- 1. ВХІДНИЙ РЯДОК (TOP) ---
        # Заголовок по центру
        ax.text(VISUAL_CENTER, 6.0, "Input String:", fontsize=12, color='gray', va='center', ha='center')

        for i, char in enumerate(s):
            is_highlighted = i in step['highlight_input_idxs']
            face_color = '#E6E6FA'
            edge_color = 'gray'
            font_weight = 'normal'
            if is_highlighted:
                face_color = '#BA55D3'
                edge_color = 'black'
                font_weight = 'bold'

            # Використовуємо зміщення input_start_x
            pos_x = input_start_x + i
            rect = patches.Rectangle((pos_x, 5.0), 0.8, 0.8, facecolor=face_color, edgecolor=edge_color)
            ax.add_patch(rect)
            ax.text(pos_x + 0.4, 5.4, char, ha='center', va='center', fontweight=font_weight, fontsize=12)
            ax.text(pos_x + 0.4, 4.8, str(i), ha='center', va='center', fontsize=7, color='gray')

        # --- 2. АЛФАВІТ (MIDDLE) ---
        # Заголовок по центру
        ax.text(VISUAL_CENTER, 3.5, "Frequency Map:", fontsize=12, color='gray', va='center', ha='center')

        for i in range(26):
            char = alphabet[i]
            count = step['counts'][i]
            is_active = (i == step['highlight_alpha_idx'])

            face_color = 'white'
            if is_active:
                if step['phase'] == 'counting':
                    face_color = '#FFFFE0'
                elif step['phase'] == 'scanning_found':
                    face_color = '#FFA500'
                elif step['phase'] == 'middle_set':
                    face_color = '#FF6347'
                elif step['phase'] == 'scanning_empty':
                    face_color = '#F5F5F5'

            edge_color = 'black' if is_active else 'lightgray'
            line_width = 2 if is_active else 1

            rect = patches.Rectangle((i, 2), 0.8, 1, facecolor=face_color, edgecolor=edge_color, linewidth=line_width)
            ax.add_patch(rect)

            ax.text(i + 0.4, 2.7, char, ha='center', va='center', fontsize=11, fontweight='bold')
            if count > 0 or step['phase'] == 'counting':
                ax.text(i + 0.4, 2.3, str(count), ha='center', va='center', fontsize=10)

        # --- 3. РЕЗУЛЬТАТ (BOTTOM) ---
        # Інфо-текст по центру
        ax.text(VISUAL_CENTER, 4.2, step['info'], ha='center', fontsize=12, color='#555555', style='italic',
                fontweight='bold')

        # Заголовок по центру
        ax.text(VISUAL_CENTER, 1.2, "Building Palindrome:", ha='center', fontsize=10, color='gray')

        # Результат будується від центру (12.5 або 13)
        CENTER_X = VISUAL_CENTER

        if step['left']:
            ax.text(CENTER_X - 0.2, 0.5, step['left'], ha='right', va='center', fontsize=22, color='green',
                    fontweight='bold', fontfamily='monospace')

        if step['middle']:
            circle = patches.Circle((CENTER_X, 0.5), 0.45, facecolor='#FFE4E1', edgecolor='red')
            ax.add_patch(circle)
            ax.text(CENTER_X, 0.5, step['middle'], ha='center', va='center', fontsize=24, color='red',
                    fontweight='bold', fontfamily='monospace')

        if step['right']:
            ax.text(CENTER_X + 0.2, 0.5, step['right'], ha='left', va='center', fontsize=22, color='blue',
                    fontweight='bold', fontfamily='monospace')

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=100, repeat=False)

    output_file = 'palindrome_centered_slow.gif'
    print(f"Creating {output_file}...")
    # FPS = 4 (повільно і плавно)
    ani.save(output_file, writer='pillow', fps=10)
    print("Done!")
    plt.close()


input_s = "newyearraeywen"
create_centered_viz(input_s)


