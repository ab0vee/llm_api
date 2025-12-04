from groq import Groq
import os

# Инициализация клиента Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY", "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")
)

MODEL_NAME = "qwen/qwen3-32b"
SYSTEM_PROMPT = "Ты умный ассистент, который отвечает на вопросы пользователя."

def get_response(message: str):
    """Отправляет сообщение в LLM модель и возвращает ответ"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            reasoning_effort="none"  # Отключает режим размышления модели
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
