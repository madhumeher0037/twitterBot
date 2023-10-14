import google.generativeai as palm
from Twiiter_Keys import Palm_API

palm.configure(api_key=Palm_API)

def command(prompt):
    response = palm.chat(messages=prompt)
    print(response.last)
    return response.last
