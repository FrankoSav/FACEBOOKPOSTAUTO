import pyautogui
import time


def main():
    response = pyautogui.confirm(
        "Hola, Hacker! Estas seguro?\nvas a hacer una publicacion", buttons=["Si", "No"])

    if response == "No":
        print("Esta bien nos vemos!.")
        return

    time.sleep(2)
    # Primer Click para minimizar vscode o la ventana en que estes ejecutando el codigo
    pyautogui.click(1811, 24)
    time.sleep(2)
    # Segundo click para presionar y escribir el posteo
    pyautogui.click(933, 470)

    # Mensaje del posteo
    def posteo():
        return """
    AQUI PON EL MENSAJE DE TU POSTEO
        """
    # Velocidad a la que se escribe el posteo
    pyautogui.write(posteo(), interval=0.00)
    
    # Click para publicar el posteo
    pyautogui.click(954, 905)


if __name__ == "__main__":
    main()
