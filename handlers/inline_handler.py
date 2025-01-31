from aiogram import Router
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)


router: Router = Router()


@router.inline_query()
async def process_inline_query(inline_query: InlineQuery):
    query = inline_query.query.lower()

    # Подсказки в зависимости от ввода пользователя
    suggestions = [
        "Тайлер",
        "Саманта"
    ]

    # Фильтруем подсказки по запросу пользователя
    results = [
        InlineQueryResultArticle(
            id=str(idx),
            title=suggestion,
            input_message_content=InputTextMessageContent(
                message_text=suggestion),
        )
        for idx, suggestion in enumerate(suggestions)
        if query in suggestion.lower()
    ]

    # Отправляем ответ с результатами на inline_query
    await inline_query.answer(results=results, is_personal=True)
