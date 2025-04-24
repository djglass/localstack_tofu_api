<<<<<<< HEAD
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
=======
# lambda_function.py

import json
import requests
import traceback

def lambda_handler(event, context):
    try:
        # Handle event body
        body_str = event.get("body", "{}")
        print("📥 Raw event body:", body_str)

        body = json.loads(body_str)
        prompt = body.get("input", "").strip()

        if not prompt:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'input' in request body."})
            }

        print("🧠 Prompt received:", prompt)

        # Call Ollama running locally on host
        response = requests.post(
            "http://host.docker.internal:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        try:
            ollama_output = response.json()
        except Exception:
            return {
                "statusCode": 502,
                "body": json.dumps({
                    "error": "Invalid response from LLM",
                    "raw": response.text
                })
>>>>>>> 7bdd6d4 (working commit)
            }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
<<<<<<< HEAD
            "body": json.dumps({"response": ollama_output.get("response", ""), "full": ollama_output})
=======
            "body": json.dumps({
                "response": ollama_output.get("response", ""),
                "tokens": ollama_output.get("eval_count", "?")
            })
>>>>>>> 7bdd6d4 (working commit)
        }

    except Exception as e:
        return {
            "statusCode": 500,
<<<<<<< HEAD
            "body": json.dumps({"error": str(e)})
=======
            "body": json.dumps({
                "error": str(e),
                "traceback": traceback.format_exc()
            })
>>>>>>> 7bdd6d4 (working commit)
        }
