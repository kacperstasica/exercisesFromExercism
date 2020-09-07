def latest(scores):
    return scores[-1]


def personal_best(scores):
    highest_score = 0
    for num in scores:
        if num > highest_score:
            highest_score = num
    return highest_score


def personal_top_three(scores):
    top_three = []
    if len(scores) >= 3:
        first = max(scores)
        top_three.append(first)
        scores.pop(scores.index(first))
        second = max(scores)
        top_three.append(second)
        scores.pop(scores.index(second))
        third = max(scores)
        top_three.append(third)
    elif len(scores) == 2:
        scores.sort(reverse=True)
        return scores
    elif len(scores) == 1:
        return scores
    return top_three
