from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом."""

    now = datetime.now()  # Получить текущую дату и время по локальному времени
    year = now.year  # Получить год из даты
    return {
        'year': year
    }
