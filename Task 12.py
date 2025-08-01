class Codec:
    def encode(self, list_of_commands):
        separator = '|||'
        encoded_string = separator.join(list_of_commands)
        return encoded_string

    def decode(self, encoded_string):
        separator = '|||'
        original_list = encoded_string.split(separator)
        return original_list


def get_user_commands():

    terminator = "***END***"
    print("Please enter your F1 commands, one per line.")
    print(f"To finish, type '{terminator}' on its own line and press Enter.")

    commands = []
    while True:
        command = input("Enter command: ")
        if command == terminator:
            break
        commands.append(command)

    return commands


def main():
    codec = Codec()
    user_commands = get_user_commands()

    if not user_commands and not any(cmd == '' for cmd in user_commands):
        print("No commands entered. Exiting.")
        return

    print("\n--- Processing Commands ---")

    encoded_string = codec.encode(user_commands)
    print(f"Input: {user_commands}")

    decoded_list = codec.decode(encoded_string)
    print(f"Output: {decoded_list}")


if __name__ == "__main__":
    main()
