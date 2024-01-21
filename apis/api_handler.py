from openai import OpenAI


client = OpenAI()


def handle_sentence(sentence):
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You behave like a chat on a live streaming platform. You only answer my question "
                        "with answers of at most 4 users. They have a username you made up "},
            {"role": "user", "content": sentence}
        ]
    )
    """
    #print(sentence)
    #return response.choices[0].message.content
    return "Chat what do you think\n Chat what do you think\n Chat what do you think \nChat what do you think \nChat what do you"


