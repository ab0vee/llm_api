from openai import OpenAI
import os

# Инициализация клиента OpenAI для OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY", "YOUR API_KEY"),
)

MODEL_NAME = "anthropic/claude-sonnet-4.5"
SYSTEM_PROMPT = "Ты умный ассистент, который отвечает на вопросы пользователя."
MAX_TOKENS = 4000  # Ограничение токенов для ответа (чтобы не превысить лимит кредитов)


def get_response(message: str):
    """Отправляет сообщение в LLM модель и возвращает ответ"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            max_tokens=MAX_TOKENS,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка: {str(e)}"


if __name__ == "__main__":
    print(f"LLM API - Модель: {MODEL_NAME}")
    print("Введите 'exit' или 'quit' для выхода\n")
    
    while True:
        user_input = input("Вы: ")
        
        if user_input.lower() in ['exit', 'quit', 'выход']:
            print("До свидания!")
            break
        
        if not user_input.strip():
            continue
        
        print("\nОжидание ответа...")
        response = get_response(user_input)
        print(f"\nМодель: {response}\n")
