import json
import re


def parse_number(value):

    if isinstance(value, str):

        value = value.strip()

        # eliminar símbolos de moneda y texto
        value = re.sub(r"[^\d,.\-]", "", value)

        # caso europeo: 1.250,50
        if "," in value and "." in value:

            if value.rfind(",") > value.rfind("."):
                value = value.replace(".", "")
                value = value.replace(",", ".")

        # caso latino: 40,50
        elif "," in value and "." not in value:
            value = value.replace(",", ".")

    return float(value)


def clean_json_response(response_text):

    cleaned = re.sub(r"```json|```", "", response_text).strip()

    data = json.loads(cleaned)

    for item in data.get("items", []):

        item["cantidad"] = parse_number(item["cantidad"])
        item["precio"] = parse_number(item["precio"])

    data["monto_total"] = parse_number(data["monto_total"])

    return data