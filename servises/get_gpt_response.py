import requests
from lexicon.lexicon_ru import INSTRUCTION
from servises.prompt import PROMPT
from config_data.config import load_config
import json


def get_gpt_response(question: str, character: str) -> str:

    """ Авторизация """
    API_KEY = load_config().api_key.key
    url = "https://llm.api.cloud.yandex.net/llm/v1alpha/instruct"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Api-key {API_KEY}'
    }

    """ Создаем промпт """
    prompt = PROMPT()
    prompt.set_generation_options(temperature=0.5)
    prompt.set_instruction_text(instruction_text=INSTRUCTION[character])
    final_prompt = prompt.generate_prompt(question)

    """ Отправляем запрос API """
    response = requests.post(url,
                             headers=headers,
                             data=json.dumps(final_prompt))

    if response.status_code == 200:
        gpt_answer = response.json()['result']['alternatives'][0]['text']
    else:
        gpt_answer = f"Error: {response}"

    return gpt_answer
