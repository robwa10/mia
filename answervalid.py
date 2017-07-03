def yes_no():
    message = '[Y/N] >'
    answer = input(message).lower()
    while answer not in ['y', 'n']:
        answer = input("Choose [Y/N] >").lower()
    return answer
