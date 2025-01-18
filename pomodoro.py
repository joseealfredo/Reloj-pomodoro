import time

def pomodoro_timer(work_duration, short_break, long_break, cycles):
    """Ejecuta el temporizador Pomodoro con las configuraciones dadas."""
    for cycle in range(1, cycles + 1):
        print(f"\nCiclo {cycle} de {cycles}")
        print("Es hora de concentrarse. ¡Comienza tu sesión de trabajo!")
        countdown(work_duration)

        if cycle < cycles:
            print("Tómate un breve descanso.")
            countdown(short_break)
        else:
            print("Has completado todos los ciclos. ¡Tómate un descanso largo!")
            countdown(long_break)

def countdown(minutes):
    """Cuenta regresiva en minutos."""
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\nTiempo terminado.\n")

def main():
    """Menú principal del programa Pomodoro."""
    menu_art = """
    __  _    __   _
   / __ \/   |  /  _/ | / /
  / /_/ / /| |  / //  |/ / 
 / _/ __ |_/ // /|  /  
//   //  |/_// |_/    
    """
    print(menu_art)
    print("Bienvenido al Reloj Pomodoro")

    try:
        work_duration = int(input("Ingresa la duración de la sesión de trabajo (minutos): "))
        short_break = int(input("Ingresa la duración del descanso corto (minutos): "))
        long_break = int(input("Ingresa la duración del descanso largo (minutos): "))
        cycles = int(input("Ingresa el número de ciclos: "))

        print("\nConfiguración completa. ¡Vamos a comenzar!")
        pomodoro_timer(work_duration, short_break, long_break, cycles)

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

# Corregido el error en esta línea
if __name__ == "__main__":
    main()
