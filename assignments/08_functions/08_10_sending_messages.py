# Brian Medina
#
# appending messages and data 

def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop()
        sent_messages.append(msg)
        print(msg)

messages = ["Hello", "Hi there", "Greetings"]

sent_messages = []
send_messages(messages, sent_messages)
print(sent_messages)