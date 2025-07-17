class BaseConverter:
    def convert(self, celsius, target_scale='all'):

        """Конвертер температуры из Цельсия с выбором шкалы.

        Args:
            celsius (float): Температура в градусах Цельсия.
            target_scale (str): 'K' - Кельвины, 'F' - Фаренгейты или 'all' (по умолчанию).

        Returns:
            float | dict: Результат в выбранной шкале или в обеих.
        """

        K = celsius + 273.15
        F = celsius * 9 / 5 + 32

        if target_scale == 'K':
            return round(K, 2)
        elif target_scale == 'F':
            return round(F, 2)
        else:
            return {
                'Kelvin': round(K, 2),
                'Fahrenheit': round(F, 2)
            }