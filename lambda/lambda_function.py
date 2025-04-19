import json
import requests

def lambda_handler(event, context):
    try:
        raw_body = event.get("body") or "{}"
        body = json.loads(raw_body)
        prompt = body.get("prompt", "You are a helpful assistant.")

        response = requests.post("http://host.docker.internal:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }, timeout=15)

        # Parse Ollama's response JSON safely
        try:
            ollama_output = response.json()
        except Exception as parse_error:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to parse Ollama response", "raw": response.text})
            }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"response": ollama_output.get("response", ""), "full": ollama_output})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
