def clock_angle(hours, minutes):
    """Вычисляет угол между часовой и минутной стрелкой.

    Args:
        hours (int): Часы (0–23).
        minutes (int): Минуты (0–59).

    Returns:
        float: Угол в градусах (0°–180°).
    """
    # Перевод 24-часового формата в 12-часовой
    hours = hours % 12

    hour_angle = 30 * hours + 0.5 * minutes  # 30° в час + 0.5° в минуту
    minute_angle = 6 * minutes  # 6° в минуту
    # Находим минимальный угол между стрелками
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)  # Возвращаем наименьший угол (0°–180°)