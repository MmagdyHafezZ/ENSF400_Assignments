import os
import random
import string

def generate_random_string(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    file_path = '/serverdata/random.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print("Existing content:", file.read())
    with open(file_path, 'w') as file:
        new_data = generate_random_string()
        file.write(new_data)
        print("New data:", new_data)

if __name__ == '__main__':
    main()
