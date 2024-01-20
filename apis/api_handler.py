from openai import OpenAI


client = OpenAI()


def handle_sentence(sentence):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You behave like a chat on a live streaming platform and only answer my question "
                        "with answers of multiple users with a name you made up "},
            {"role": "user", "content": sentence}
        ]
    )
    return response['choices'][0]['message']['content']
