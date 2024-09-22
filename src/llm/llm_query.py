import requests
import prompt_engineering

openai_api_key = ""  # put your api key here


def get_results_open_ai(question):
    "send the wiki context to openai GPT api and ask it to recognize entities and relationships"
    responses = []
    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content":  f"""<|im_start|>system
                            You are a friendly sql assistant. You build sqls based on questions from users.
                            The schema of the database on which the sql needs to be built is this:  
                                {prompt_engineering.sql_context}                                 
                            <|im_end|>
                            
                            <|im_start|>user
                            Build a sql to answer the following question. Output as Text
                            text: {question} <|im_end|>
                            <|im_start|>assistant
                            """
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print('\n')
        print('##################################################')
        print(response.json()['choices'][0]['message']['content'])
        responses.append(response.json()['choices'][0]['message']['content'])
    else:
        print("Error:", response.status_code, response.text)
    print('##################################################')
    return responses
