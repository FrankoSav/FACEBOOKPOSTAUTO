import pyautogui
import time


def main():
    response = pyautogui.confirm(
        "Hola, Hacker! Estas seguro?\nvas a hacer una publicacion", buttons=["Si", "No"])

    if response == "No":
        print("Esta bien nos vemos!.")
        return

    time.sleep(2)
    pyautogui.click(1811, 24)
    time.sleep(2)
    pyautogui.click(933, 470)

    def posteo():
        return """
    AQUI PON EL MENSAJE DE TU PUBLICACION!
        """
    pyautogui.write(posteo(), interval=0.00)
    pyautogui.click(954, 905)


if __name__ == "__main__":
    main()
