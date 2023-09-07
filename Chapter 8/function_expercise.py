def print_input(answer):
    return answer

response = input("are you ready to start?")

#the T in true is capitilized because it is a boolean
while True:
    ask = input("what do you want to do?")
    print_input(ask)

    response = input("ready yet?")
    if response.lower() == 'quit' or 'no':
        break