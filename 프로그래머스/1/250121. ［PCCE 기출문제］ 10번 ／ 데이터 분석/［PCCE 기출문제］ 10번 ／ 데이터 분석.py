def solution(data, ext, val_ext, sort_by):
    list = ["code", "date", "maximum", "remain"]
    ext_idx = list.index(ext)
    sort_idx = list.index(sort_by)

    answer = []
    for i, d in enumerate(data):
        if d[ext_idx] < val_ext:
            answer.append(d)

    answer.sort(key = lambda x: x[sort_idx])
    return answer