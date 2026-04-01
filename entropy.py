import math

def shannon_entropy(data):
    if not data:
        return 0

    freq = {}
    for c in data:
        freq[c] = freq.get(c, 0) + 1

    entropy = 0
    length = len(data)

    for f in freq.values():
        p = f / length
        entropy -= p * math.log2(p)

    return entropy


def find_high_entropy_strings(text, threshold=4.5):
    words = text.split()
    results = []

    for word in words:
        if len(word) < 8:
            continue

        ent = shannon_entropy(word)

        if ent >= threshold:
            results.append({
                "value": word,
                "entropy": round(ent, 2)
            })

    return results