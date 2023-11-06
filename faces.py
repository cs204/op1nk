def convert(input_str):
    input_str = input_str.replace(':)', '🙂')
    input_str = input_str.replace(':(', '🙁')
    return input_str

def main():
    user_input = input()
    converted_text = convert(user_input)
    print(converted_text)

if __name__ == "__main__":
    main()