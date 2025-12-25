
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Дані та Логіка Алгоритму ---
heights = [1, 8, 6, 2, 5, 4, 7, 3, 6]
n = len(heights)
x_pos = np.arange(n)


def get_two_pointer_steps(h):
    """
    Попередньо розраховує кроки алгоритму двох вказівників.
    Повертає список кортежів: (left_idx, right_idx, current_area, max_area_so_far)
    """
    steps = []
    left = 0
    right = len(h) - 1
    max_area = 0

    while left < right:
        h_left = h[left]
        h_right = h[right]

        current_height = min(h_left, h_right)
        current_width = right - left
        current_area = current_height * current_width
        max_area = max(max_area, current_area)

        steps.append((left, right, current_area, max_area))

        # Логіка руху вказівників: рухаємо той, що менший
        if h_left < h_right:
            left += 1
        else:
            right -= 1

    return steps


# Отримуємо всі кроки алгоритму
algorithm_steps = get_two_pointer_steps(heights)

# --- Налаштування Анімації ---
fig, ax = plt.subplots(figsize=(8, 6))


def update(frame_idx):
    ax.clear()

    # Отримуємо стан для поточного кадру
    l, r, curr_a, max_a = algorithm_steps[frame_idx]

    # 1. Малюємо базові чорні стовпчики
    ax.bar(x_pos, heights, color='black', width=0.4, label='Column')

    # 2. Малюємо активні лівий і правий стовпчики червоним
    ax.bar(x_pos[l], heights[l], color='red', width=0.4, label='Poinets')
    ax.bar(x_pos[r], heights[r], color='red', width=0.4)

    # 3. Малюємо блакитну область води
    water_height = min(heights[l], heights[r])
    # Малюємо прямокутник між l і r висотою water_height
    ax.fill_between([l, r], [water_height, water_height], color='#90c0f0', alpha=0.7, zorder=0, label='Water')

    # Налаштування осей та заголовка
    ax.set_ylim(0, 9)
    ax.set_xlim(-0.5, 8.5)
    ax.set_yticks(range(0, 10))
    ax.set_xticks(x_pos)
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    ax.set_title(f"Step {frame_idx + 1}\nLeft: {l}, Right: {r} | Current Area: {curr_a} | Max Area: {max_a}")
    if frame_idx == 0:
        ax.legend(loc='upper right')


# Створення анімації
# interval=1000 означає 1 секунда на кадр
ani = animation.FuncAnimation(fig, update, frames=len(algorithm_steps), interval=1500, repeat=False)

# Збереження у GIF (потрібен встановлений пакет pillow)
output_filename = 'two_pointer_algorithm.gif'
print(f"Створення {output_filename}...")
# Використовуємо writer='pillow' для створення GIF без додаткових зовнішніх програм типу ImageMagick
ani.save(output_filename, writer='pillow', fps=1)
print("Готово!")
plt.close()  # Закриваємо вікно, щоб не показувати статичний кадр