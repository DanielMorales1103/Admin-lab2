from textlib import reverse, count_vowels, is_palindrome, to_upper, concat


def main():
    print("=== Demo textlib ===\n")

    # reverse
    print("[reverse]")
    print('  reverse("hola") ->', reverse("hola"))

    # count_vowels
    print("[count_vowels]")
    print('  count_vowels("Pingüino rápido") ->', count_vowels("Pingüino rápido"))

    # is_palindrome
    print("[is_palindrome]")
    print('  is_palindrome("¿Acaso hubo búhos acá?") ->', is_palindrome("¿Acaso hubo búhos acá?"))

    # to_upper
    print("[to_upper]")
    print('  to_upper("mañana") ->', to_upper("mañana"))

    # concat
    print("[concat]")
    print('  concat("hola", " mundo") ->', concat("hola", " mundo"))



if __name__ == "__main__":
    main()
