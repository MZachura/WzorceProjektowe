from config import BLACK_MSG, CAMERA_CREATED_MSG, DB_CONNECTION_MESSAGE, ENDC, GREEN_MSG, RED, RED_MSG, YELLOW_MSG

class Message:
    def __init__(self, status, text):
        self.status = status
        self.text = text
    
    def __str__(self):
        return 'self.text'


class MessageDecorator:
    def __init__(self, objecto):
        self.obj = objecto

    def __str__(self):
        msg = self.obj.msg
        status = msg.status
        msgText = msg.text

        if status == 200:
            color = GREEN_MSG
        elif status == 0:
            color = YELLOW_MSG
        elif status == 1:
            color = BLACK_MSG
        else:
            color = RED_MSG

        return '%s%s%s' % (color, msgText, ENDC)


class simpleClass:
    def __init__(self):
        self.msg = Message(200, "lel")


class SimpleClass:
    def __init__(self):
        self.msg = Message(201, "lol")



def main():
    p = []
    p.append(simpleClass())
    p.append(SimpleClass())

    for m in p:
        m = MessageDecorator(m)
        print(m)

if __name__ == "__main__":
    main()
