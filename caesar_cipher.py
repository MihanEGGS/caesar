a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, o):#Функция для зашифровки
  result = "" 
  for char in text:# цикл, что перебирает символы в тексте, пока не дойдет до конца текста  
    if (alph.find(char) == -1):#если символ не найден в алфавите , то возвращается -1
      result += char
    else:# если таки найден, то он добавляется к алфавиту
      result += (alph[(alph.find(char) + o) % len(alph)])
  return result

def decrypt(text, o):# функция для расшифровки
  result = ""
  for char in text:# цикл, что перебирает символы в тексте, пока не дойдет до конца текста  
    if (alph.find(char) == -1):#если символ не найден в алфавите , то возвращается -1
      result += char
    else:# если таки найден, то он добавляется к алфавиту
      result += (alph[(alph.find(char) - o) % len(alph)])
  return result

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:#Если пользователь хочет зашифровать текст
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypt(text, rotation))
elif mode == 2:#Если пользователь хочет расшифровать текст 
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypt(text, rotation))
elif mode == 3:#Если нужно затроллить пользователя
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")

