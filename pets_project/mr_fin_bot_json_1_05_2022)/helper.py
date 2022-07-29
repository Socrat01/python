
def category_parser(category):
    return {
        "🍏продукти": 'food',
        "🏠комунальні": 'utilities',
        "☕️кафе": 'cafe',
        "💳кредити": 'credit',
        "💰+витрати": 'dpay',
        "📊інвестиції": ''
    }[category]

def answer_parser(answer):
    return {
        "✅Вірно": True,
        "⛔️Відміна": False
    }[answer]






