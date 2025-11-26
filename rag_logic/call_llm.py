from openai import OpenAI


def generate_answer(prompt, api_key):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        error_msg = f"Error calling DeepSeek API: {e}"
        return error_msg
