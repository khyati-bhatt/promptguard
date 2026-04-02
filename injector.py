import json

def inject_payload(data, payload):
    try:
        obj = json.loads(data)

        if "message" in obj:
            obj["message"] = payload

        return json.dumps(obj)

    except Exception:
        return data  # fallback if not JSON