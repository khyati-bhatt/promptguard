def compare_responses(base, injected, payload):
    results = {
        "reflection": False,
        "length_change": False
    }

    if payload.lower() in injected.lower():
        results["reflection"] = True

    if abs(len(base) - len(injected)) > 20:
        results["length_change"] = True

    return results