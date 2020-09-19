def find_anagrams(w, cs):
    return [c for c in cs if sorted(w.lower()) == sorted(c.lower()) and c.lower() != w.lower()]

# def find_anagrams(word, candidates):
#     expected = []
#     for candidate in candidates:
#         if sorted(word.lower()) == sorted(candidate.lower()):
#             if candidate.lower() != word.lower():
#                 expected.append(candidate)
#     return expected
