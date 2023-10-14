from bardapi import BardCookies
from Twiiter_Keys import Secure_1PSID,Secure_1PSIDTS
cookie_dict = {
    "__Secure-1PSID": Secure_1PSID ,
    "__Secure-1PSIDTS": Secure_1PSIDTS,
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)
def command(prompt):
    response = bard.get_answer(prompt)['content']
    print(response)
    return response
