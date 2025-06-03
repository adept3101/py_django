from django import template

register = template.Library()


@register.filter
def pagination_window(page_obj, window_size=5):
    """
    Возвращает окно страниц вокруг текущей страницы
    :param page_obj: объект страницы пагинатора
    :param window_size: количество страниц по бокам от текущей
    :return: список страниц для отображения
    """
    current = page_obj.number
    total = page_obj.paginator.num_pages

    # Рассчитываем границы окна
    left = max(1, current - window_size)
    right = min(total, current + window_size)

    # Корректируем окно, если оно меньше заданного размера
    if current - left < window_size:
        right = min(right + (window_size - (current - left)), total)
    if right - current < window_size:
        left = max(left - (window_size - (right - current)), 1)

    # Генерируем список страниц в окне
    pages = list(range(left, right + 1))

    # Добавляем разрывы и крайние страницы
    if left > 1:
        if left > 2:
            pages.insert(0, '...')
        pages.insert(0, 1)
    if right < total:
        if right < total - 1:
            pages.append('...')
        pages.append(total)

    return pages