import openai
import time
import os
import sqlite3
from dotenv import load_dotenv

from utils import num_tokens_from_messages, log_to_db

load_dotenv()

openai.api_base = os.getenv("OPENAI_BASE_URL")
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")

conn = sqlite3.connect("telemetry.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        role TEXT,
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

history = []

def save_message(role, content):
    history.append({"role": role, "content": content})
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    if len(history) > 10:
        history.pop(0)

def main():
    print("AI Chat (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        save_message("user", user_input)
        messages = history[-10:]

        start_time = time.time()
        try:
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=messages,
                stream=True
            )

            full_reply = ""
            print("Assistant:", end=" ", flush=True)
            for chunk in response:
                delta = chunk['choices'][0]['delta']
                if "content" in delta:
                    print(delta["content"], end="", flush=True)
                    full_reply += delta["content"]
            print()

            latency = int((time.time() - start_time) * 1000)

            save_message("assistant", full_reply)

            prompt_tokens = num_tokens_from_messages(messages)
            completion_tokens = num_tokens_from_messages([{ "role": "assistant", "content": full_reply }])
            total_tokens = prompt_tokens + completion_tokens
            cost = round((prompt_tokens + completion_tokens) * 0.00001, 6)

            log_to_db(prompt_tokens, completion_tokens, cost, latency)
            print(f"[stats] prompt={prompt_tokens} completion={completion_tokens} cost=${cost} latency={latency} ms")
        except Exception as e:
            print(f"\n[error] {e}")

if __name__ == "__main__":
    main()
