import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    # new_code = ''
    # for _ in range(size):
    #     new_code.join(random.choice(chars))
    # return new_code

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    shortener_url = instance.__class__#Shortener_URL model name from models is needed that's why
    qs_exists = shortener_url.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code