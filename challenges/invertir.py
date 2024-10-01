#programa que invierta el orden de una cadena de texto

def reversr(text):
    text_len = len(text)
    reser_text = ""
    for i in range(0,text_len):
        reser_text += text[text_len - i - 1]
    return reser_text


print(reversr("Hola mundo")) #odnum aloH