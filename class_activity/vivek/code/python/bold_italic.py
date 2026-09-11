



def make_bold(func: function):
    def wrapper(*args, **kwargs):
        text = func()
        return f"<b>{text}</b>"
    return wrapper


def make_italic(func: function):
    def wrapper():
        text = func()
        return f"<i>{text}</i>"
    return wrapper


@make_bold
@make_italic
def get_text():
    return "Hello!"

print(get_text())