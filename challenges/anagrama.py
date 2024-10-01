"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
#sorted, ordena una lista de elementos
def is_anagram(pal1,pal2):
    if pal1.lower() == pal2.lower():
        return False
    if sorted(pal1.lower()) == sorted(pal2.lower()):
        return True


print(is_anagram("roma","amor")) # True