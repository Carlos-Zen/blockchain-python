from prompt_toolkit import prompt

if __name__ == '__main__':
    answer = prompt('Give me some input: ')
    answer1 = prompt('Give me some input: ')
    print('You said: %s,%s' % (answer,answer1))