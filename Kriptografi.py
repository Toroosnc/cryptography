import string

def encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

lang = input("Language (id/en): ").strip().lower()

msgs = {
    "id": ("1) Enkripsi\n2) Dekripsi\nPilih: ", "Teks: ", "Geser: ", "Hasil: "),
    "en": ("1) Encrypt\n2) Decrypt\nChoose: ", "Text: ", "Shift: ", "Result: "),
}
menu, txt_prompt, shift_prompt, result_label = msgs.get(lang, msgs["en"])

choice = input(menu)
text = input(txt_prompt)
shift = int(input(shift_prompt))

out = encrypt(text, shift) if choice == "1" else decrypt(text, shift)
print(result_label + out)