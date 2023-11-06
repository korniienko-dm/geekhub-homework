"""
Task_4: 
Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе
та виводить декодоване значення (латинськими літерами).
   Особливості: 
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо
    використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад: 
    --. . . -.- .... ..- -...   .. ...   .... . .-. .
    результат:  GEEKHUB IS HERE
"""


def get_morse_simbol_decode() -> dict:
    """
    Returns a dictionary for decoding Morse code symbols to English letters.

    Parameters:
    morse_code_str (str): The input Morse code string to be decoded.
        Use only simbol:
        "Dot" -    ".";
        "Dashes" - "-";
        "Spaces" - " ";

        Separators:
        "One space" = "New letter"
        "Three spaces" = "New word"
    """
    morse_simbol = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '*SPACE*': ' ',
        '...---...': 'SOS',
    }

    return morse_simbol


def morse_code(morse_code_str:  str) -> str:
    """
    Decodes a given Morse code string to English text.
    """
    morse_simbol_decode = get_morse_simbol_decode()

    str_with_space = morse_code_str.replace('   ', ' *SPACE* ')
    list_all_morse_simbol = str_with_space.split(" ")
    
    try:
        decoding_morse_string = "".join(morse_simbol_decode[x] for x in list_all_morse_simbol)
    except KeyError as text_error:
        return f"KeyError! The symbol {text_error} was not found in the Morse code collection!"

    return decoding_morse_string


morse_string = "- .... .. ...   .. ...   - .... .   .-- .- -.--"
print(morse_code(morse_code_str=morse_string))
