def category_parser(category):
    return {
        "🍏продукти": 1,
        "🏠комунальні": 2,
        "☕️кафе": 3,
        "💳кредити": 4,
        "💰+витрати": 5,
        "📊інвестиції": 6
    }[category]

def answer_parser(answer):
    return {
        "✅Вірно": True,
        "⛔️Відміна": False
    }[answer]


def category_parsernum(category):
    return {
        1: "🍏продукти",
        2: "🏠комунальні",
        3: "☕️кафе",
        4: "💳кредити",
        5: "💰+витрати",
        6: "📊інвестиції"
    }[category]

