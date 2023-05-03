from typing import List
import ipaddress
import platform

def palindrome(text: str) -> List[str]:
    """
    Returns a list of all palindromic words in the input text, ignoring case and punctuation.

    Args:
        text (str): The input text to search for palindromes in.

    Returns:
        List[str]: A list of all palindromic words found in the input text.
    """
    palindromes = list()
    # convert input text to lowercase and split into individual words
    text = text.lower()
    list_of_words = text.split(' ')

    # check each word to see if it's a palindrome
    for word in list_of_words:
        # ignore punctuation and whitespace
        word = ''.join(c for c in word if c.isalnum())
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


def validate_ip(ip: str) -> None:
    """
    Validates whether the input string is a valid IP address and prints the result.

    Args:
        ip (str): The input string to validate as an IP address.
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f'This ip is valid: {ip_obj}')
    except ValueError:
        print(f'This ip is not valid: {ip}')


def get_os() -> None:
    """
    Prints the name of the operating system that the code is running on.
    """
    system = platform.system()

    # use a match statement to determine the operating system
    match system:
        case 'Linux':
            print('Linux')
        case 'Darwin':
            print('Mac')
        case 'Windows':
            print('Windows')
        case _:
            print('Unregistered OS')


if __name__ == '__main__':
    # prompt the user for input and call each function with the input
    text = input('Enter your text for search palindromes: ')
    print(palindrome(text))
    ip = input('Enter ip address: ')
    validate_ip(ip)
    get_os()