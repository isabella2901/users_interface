import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
from PIL import Image, ImageTk, ImageDraw
from controllers.user_controller import UserController

user_controller = UserController()
# Datos de ejemplo de ejercicios
# Datos de ejemplo de ejercicios
EXERCISES = {
    "abdomen": [
        {
            "nombre": "Crunch abdominal",
            "imagen": "./images/ABDOMEN/CRUNCH ABDOMINAL.JPG",
            "orden": 1,
            "tiempo": 10,
            "series": 2,
            "repeticiones_por_serie": 12,
            "descripcion": "Acostado boca arriba, eleva el torso hacia las rodillas mientras mantienes las piernas dobladas.",
        },
        {
            "nombre": "Elevación de piernas",
            "imagen": "./images/ABDOMEN/ELEVACION DE PIERNAS.JPG",
            "orden": 2,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Acostado boca arriba, levanta las piernas estiradas hacia arriba hasta formar un ángulo recto con el cuerpo.",
        },
        {
            "nombre": "Mountain climbers",
            "imagen": "./images/ABDOMEN/MOUNTAIN CLIMBERS.JPG",
            "orden": 3,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "En posición de plancha, lleva las rodillas hacia el pecho rápidamente, alternando entre ambas piernas.",
        },
        {
            "nombre": "Plancha con rotación",
            "imagen": "./images/ABDOMEN/PLANCHA CON ROTACION.JPG",
            "orden": 4,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Desde la posición de plancha, rota el torso hacia un lado y extiende el brazo hacia el techo. Alterna lados.",
        },
        {
            "nombre": "Plancha sobre un pie",
            "imagen": "./images/ABDOMEN/PLANCHA SOBRE UN PIE.JPG",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "En posición de plancha, levanta una pierna manteniendo el cuerpo estable.",
        },
        {
            "nombre": "Plancha sostenida por un minuto",
            "imagen": "./images/ABDOMEN/PLANCHA SOSTENIDA.JPG",
            "orden": 6,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Mantén la posición de plancha durante un minuto.",
        },
    ],
    "piernas": [
        {
            "nombre": "Sentadilla",
            "imagen": "./images/PIERNA/sentadilla.JPG",
            "orden": 1,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Baja las caderas como si te fueras a sentar en una silla, manteniendo el torso recto y los pies separados a la altura de los hombros.",
        },
        {
            "nombre": "Peso muerto",
            "imagen": "./images/PIERNA/peso muerto.JPG",
            "orden": 2,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "De pie, con una barra o mancuerna en las manos, inclina el torso hacia adelante desde las caderas, manteniendo la espalda recta y las rodillas ligeramente flexionadas.",
        },
        {
            "nombre": "Puente de glúteos",
            "imagen": "./images/PIERNA/puente de egluteos.JPG",
            "orden": 3,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Acostado boca arriba, flexiona las rodillas y eleva las caderas hasta formar una línea recta entre hombros y rodillas, apretando los glúteos en la parte superior. ",
        },
        {
            "nombre": "Sentadilla búlgara",
            "imagen": "./images/PIERNA/sentadilla bulgara.JPG",
            "orden": 4,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Con un pie apoyado en un banco detrás de ti, realiza una sentadilla manteniendo el torso recto. ",
        },
        {
            "nombre": "Sentadilla sostenida",
            "imagen": "./images/PIERNA/sentadilla sostenida.JPG",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Baja en una sentadilla y mantén la posición durante 30 segundos a 1 minuto, manteniendo los muslos paralelos al suelo. ",
        },
        {
            "nombre": "Sentadillas laterales",
            "imagen": "./images/PIERNA/sentadillas laterales.JPG",
            "orden": 6,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Da un paso lateral amplio y baja en una sentadilla, manteniendo una pierna extendida.",
        },
    ],
    "espalda": [
        {
            "nombre": "Dominadas",
            "imagen": "./images/ESPALDA/dominadas.JPG",
            "orden": 1,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Sube y baja tu cuerpo colgado de una barra, llevando la barbilla por encima de la barra en cada repetición.",
        },
        {
            "nombre": "Plancha en T",
            "imagen": "./images/ESPALDA/plancha en T.JPG",
            "orden": 2,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Desde la posición de plancha, rota el cuerpo hacia un lado, extendiendo un brazo hacia el techo, formando una T con el cuerpo. ",
        },
        {
            "nombre": "Remo con mancuerna",
            "imagen": "./images/ESPALDA/remo con mancuerna.JPG",
            "orden": 3,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Inclínate hacia adelante desde la cintura y, con una mancuerna en una mano, tira del peso hacia tu torso. ",
        },
        {
            "nombre": "Remo en máquina",
            "imagen": "./images/ESPALDA/remo en maquina.JPG",
            "orden": 4,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Sentado en una máquina de remo, tira de la barra hacia tu torso, llevando los codos hacia atrás. ",
        },
        {
            "nombre": "Remo invertido",
            "imagen": "./images/ESPALDA/remo invertido.JPG",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Colgado de una barra con los pies apoyados en el suelo, tira del torso hacia la barra, manteniendo el cuerpo recto.  ",
        },
        {
            "nombre": "Renegade Rows",
            "imagen": "./images/ESPALDA/renegade rows.JPG",
            "orden": 6,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "En posición de plancha con mancuernas, tira de una mancuerna hacia el torso mientras mantienes la posición de plancha. ",
        },
    ],
    "brazos": [
        {
            "nombre": "Curl de bíceps",
            "imagen": "./images/BRAZOS/curl de biceps.JPG",
            "orden": 1,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Con mancuernas o una barra, flexiona los codos para levantar el peso hacia los hombros.  ",
        },
        {
            "nombre": "Extensión de tríceps",
            "imagen": "./images/BRAZOS/extensión de triceps.JPG",
            "orden": 2,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Con una mancuerna o una barra, extiende los codos por encima de la cabeza, luego baja lentamente.",
        },
        {
            "nombre": "Flexiones de pecho",
            "imagen": "./images/BRAZOS/flexiones de pecho.JPG",
            "orden": 3,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Desde la posición de plancha, baja el pecho hacia el suelo y luego empuja hacia arriba.",
        },
        {
            "nombre": "Elevación lateral",
            "imagen": "./images/BRAZOS/elevacion lateral.JPG",
            "orden": 4,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "con dos mancuernas y de pie inclínate y levanta las mancuernas lateralmente hasta alcanzar la misma altura de los hombros",
        },
        {
            "nombre": "Press de hombro",
            "imagen": "./images/BRAZOS/press de hombro.JPG",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Con mancuernas o una barra, empuja el peso desde los hombros hacia arriba hasta extender los brazos completamente.",
        },
        {
            "nombre": "Tríceps",
            "imagen": "./images/BRAZOS/triceps.JPG",
            "orden": 6,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Realiza flexiones apoyando las manos en un banco, con los codos hacia atrás para trabajar el tríceps. ",
        },
    ],
    "Glúteos": [
        {
            "nombre": "Abducción de cadera",
            "imagen": "./images/GLUTEOS/abduccion de cadera.JPG",
            "orden": 1,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Acuéstate de lado y levanta la pierna superior lo más alto posible, manteniéndola recta. ",
        },
        {
            "nombre": "Patada trasera en posición de gateo",
            "imagen": "./images/GLUTEOS/patada trasera.JPG",
            "orden": 2,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "En posición de cuatro patas, levanta una pierna flexionada hacia arriba. ",
        },
        {
            "nombre": "Prensa con pierna",
            "imagen": "./images/GLUTEOS/prensa de pierna.JPG",
            "orden": 3,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Sentado en una máquina de prensa, empuja el peso hacia adelante con las piernas.   ",
        },
        {
            "nombre": "Sentadilla con peso",
            "imagen": "./images/GLUTEOS/sentadilla con peso.JPG",
            "orden": 4,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Realiza una sentadilla manteniendo una barra o mancuernas a la altura de los hombros. ",
        },
        {
            "nombre": "Step up",
            "imagen": "./images/GLUTEOS/step up.JPG",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Sube a un banco o caja con una pierna y luego baja lentamente. Alterna entre ambas piernas. ",
        },
        {
            "nombre": "Sumo squat",
            "imagen": "./images/GLUTEOS/SUMO_SQUAT.jpg",
            "orden": 5,
            "tiempo": 10,
            "series": 1,
            "repeticiones_por_serie": 10,
            "descripcion": "Sube a un banco o caja con una pierna y luego baja lentamente. Alterna entre ambas piernas. ",
        },
    ],
}

# Variables para controlar el estado del ejercicio actual y el timer
actual_category = None
index_exercise = 0
time_left = 0
timer_active = False
current_serie = 1
list_menu_random = []
index_random_exercise = 0


# Función para validar el login
def validate_login():
    user = entry_user.get()
    password = entry_password.get()

    user_found = user_controller.get_user_by_id(user)
    
    if user_found.get("message"):
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        return
    

    if user == user_found.get("username") and password == user_found.get("password"):  # Ejemplo simple de validación
        # olvidar pantalla de login
        login_screen.pack_forget()
        show_screen_exercises()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# Función para mostrar la pantalla de selección de parte del cuerpo
def show_screen_exercises():
    exercises_screen.pack(fill="both", expand=True)


# Función para mostrar la pantalla intermedia de selección de ejercicio
def show_screen_selection_exercise(ejercicio):

    print("ejercicio", ejercicio)

    if ejercicio == "random":
        global list_menu_random
        listado_ejercicios_random = []
        for categoria in EXERCISES.keys():
            # escoger uno al azar
            ejercicio_random = random.choice(EXERCISES[categoria])
            listado_ejercicios_random.append(ejercicio_random)
        list_menu_random = listado_ejercicios_random
        show_random_exercises(list_menu_random)
    else:
        global actual_category
        actual_category = ejercicio
        # olvidar pantalla
        exercises_screen.pack_forget()
        screen_selection_exercise.pack(fill="both", expand=True)

        # Limpiar los ejercicios anteriores en pantalla
        for widget in screen_selection_exercise.winfo_children():
            widget.pack_forget()

        # Mostrar los ejercicios disponibles en la categoría seleccionada
        label_selection.config(text=f"Ejercicios para {actual_category}")
        label_selection.pack(pady=10)
        lista_ejercicios = EXERCISES[actual_category]

        for idx, ejercicio in enumerate(lista_ejercicios):
            boton_ejercicio = tk.Button(
                screen_selection_exercise,
                text=ejercicio["nombre"],
                command=lambda i=idx: show_detail_exercise(i),
            )
            boton_ejercicio.pack(pady=5)

        boton_ejercicio = tk.Button(
            screen_selection_exercise,
            text="Volver",
            command=lambda i=idx: go_back_to_principal_menu_from_selection(),
        )
        boton_ejercicio.pack(pady=5)


def go_to_users_management():
    exercises_screen.pack_forget()
    screen_users.pack()
    screen_users.pack(fill="both", expand=True)


def go_back_to_principal_menu_from_selection():
    screen_random.pack_forget()
    screen_selection_exercise.pack_forget()
    show_screen_exercises()

def show_random_exercises(list_ejercicios):

    # Limpiar los ejercicios anteriores en pantalla
    for widget in screen_random.winfo_children():
        widget.pack_forget()
    exercises_screen.pack_forget()
    screen_random.pack(fill="both", expand=True)

    for idx, ejercicio in enumerate(list_ejercicios):
        boton_ejercicio = tk.Button(
            screen_random,
            text=ejercicio["nombre"],
            command=lambda i=idx: show_detail_random_exercise(i),
        )
        boton_ejercicio.pack(pady=5)

    boton_ejercicio = tk.Button(
        screen_random,
        text="Volver",
        command=lambda i=idx: go_back_to_principal_menu_from_selection(),
    )
    boton_ejercicio.pack(pady=5)

def show_detail_random_exercise(indice):
    global time_left, timer_active, current_serie, index_random_exercise

    index_random_exercise=indice
    # mostrar detalle del ejercicio

    ejercicio = list_menu_random[indice]
    print(ejercicio)

    time_left = ejercicio["tiempo"]
    minutos = time_left // 60
    segundos = time_left % 60
    label_timer_random.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
    label_timer_random.pack()
    # setear el tiempo restante al configurado del ejercicio
    label_random_name.config(text=ejercicio["nombre"])
    label_description_random.config(text=ejercicio["descripcion"])

    label_series_random.config(
        text=f"Series: {ejercicio['series']} x {ejercicio['repeticiones_por_serie']}"
    )
    label_count_series_random.config(
        text=f"Serie actual: {current_serie} de {ejercicio['series']}"
    )

    # Cargar la imagen del ejercicio
    try:
        
        # Abre la imagen usando PIL
        imagen_pil = Image.open(ejercicio["imagen"])

        nueva_anchura = 300
        nueva_altura = 300

        # Redimensionar la imagen
        imagen_redimensionada = imagen_pil.resize(
            (nueva_anchura, nueva_altura), Image.Resampling.LANCZOS
        )

        # Convertir la imagen a un formato compatible con tkinter
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Configurar el label para mostrar la imagen
        label_imagen_random.config(image=imagen_tk)
        label_imagen_random.image = imagen_tk  # Mantener una referencia a la imagen

    except Exception as e:
        print(f"Error cargando imagen: {e}")
        label_imagen_random.config(image="")  # Si no se encuentra la imagen

    timer_active = False
    update_timer_random()

    screen_random.pack_forget()

    button_play_random.pack(pady=5)
    screen_random_exercise.pack(fill="both", expand=True)


# Función para mostrar el detalle del ejercicio actual
def show_detail_exercise(indice):
    global index_exercise, actual_category, time_left, timer_active, current_serie

    index_exercise = indice
    current_serie = 1
    
    
    # Obtenemos el ejercicio actual
    ejercicio = EXERCISES[actual_category][index_exercise]
    time_left = ejercicio["tiempo"]
    minutos = time_left // 60
    segundos = time_left % 60
    label_timer.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
    label_timer.pack()
    # setear el tiempo restante al configurado del ejercicio

    # Actualizar la interfaz con los datos del ejercicio
    label_name.config(text=ejercicio["nombre"])
    label_description.config(text=ejercicio["descripcion"])

    label_series.config(
        text=f"Series: {ejercicio['series']} x {ejercicio['repeticiones_por_serie']}"
    )
    label_count_series.config(
        text=f"Serie actual: {current_serie} de {ejercicio['series']}"
    )

    # Cargar la imagen del ejercicio
    try:
        print(ejercicio["imagen"])

        # Abre la imagen usando PIL
        imagen_pil = Image.open(ejercicio["imagen"])  
        
        nueva_anchura = 300
        nueva_altura = 300

        # Redimensionar la imagen
        imagen_redimensionada = imagen_pil.resize((nueva_anchura, nueva_altura), Image.Resampling.LANCZOS)

        # Convertir la imagen a un formato compatible con tkinter
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Configurar el label para mostrar la imagen
        label_imagen.config(image=imagen_tk)
        label_imagen.image = imagen_tk  # Mantener una referencia a la imagen
    except Exception as e:
        print(f"Error cargando imagen: {e}")
        label_imagen.config(image="")  # Si no se encuentra la imagen

    timer_active = False
    update_timer()

    screen_selection_exercise.pack_forget()
    
    screen_exercise.pack(fill="both", expand=True)


# Función para actualizar el timer
def update_timer():
    global time_left, timer_active, current_serie, index_exercise, actual_category

    ejercicio = EXERCISES[actual_category][index_exercise]

    if timer_active and time_left > 0:
        minutos = time_left // 60
        segundos = time_left % 60
        label_timer.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
        label_timer.pack()
        # Resta un segundo y programa la próxima actualización en 1000 ms (1 segundo)
        time_left -= 1
        screen_exercise.after(1000, update_timer)
    elif time_left <= 0:
        print("se acabo el tiempo")
        if current_serie == ejercicio["series"]:
            print("Se acabaron las series")
            # volver contador de serie a 1
            current_serie = 1
            
            
            screen_exercise.pack_forget()
            # mostrar siguiente ejercicio
            if index_exercise + 1 < len(EXERCISES[actual_category]):
                index_exercise += 1
            else:
                screen_exercise.pack_forget()
                show_screen_selection_exercise(actual_category)
                return
            show_detail_exercise(index_exercise)

            return
        # tiempo_restante = ejercicio["tiempo"]
        current_serie += 1
        label_count_series.config(
            text=f"Serie actual: {current_serie} de {ejercicio['series']}"
        )
        # volver al tiempo original
        time_left = ejercicio["tiempo"]
        update_timer()
        
        timer_active = False


def update_timer_random():
    global time_left, timer_active, current_serie, index_exercise, actual_category,index_random_exercise

    ejercicio = list_menu_random[index_random_exercise]

    if timer_active and time_left > 0:
        minutos = time_left // 60
        segundos = time_left % 60
        label_timer_random.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
        label_timer_random.pack()
        # Resta un segundo y programa la próxima actualización en 1000 ms (1 segundo)
        time_left -= 1
        screen_random_exercise.after(1000, update_timer_random)
    elif time_left <= 0:
        if current_serie == ejercicio["series"]:
            screen_random_exercise.pack_forget()
            # mostrar siguiente ejercicio
            if index_random_exercise + 1 < len(list_menu_random):
                index_random_exercise += 1
                show_detail_random_exercise(index_random_exercise)
            else:
                screen_random_exercise.pack_forget()
                show_random_exercises(list_menu_random)
                return

        # tiempo_restante = ejercicio["tiempo"]
        current_serie += 1
        label_count_series.config(
            text=f"Serie actual: {current_serie} de {ejercicio['series']}"
        )
        timer_active = False


# Función para pausar el timer
def stop_timer():
    global timer_active
    timer_active = False


# Función para reanudar el timer
def play_timer():
    global timer_active
    if not timer_active:
        timer_active = True
        update_timer()

def play_timer_random():
    global timer_active
    if not timer_active:
        timer_active = True
        update_timer_random()


def skip_exercise():
    global index_exercise, actual_category
    if index_exercise + 1 < len(EXERCISES[actual_category]):
        index_exercise += 1
        show_detail_exercise(index_exercise)
    else:
        # limpiar pantalla
        screen_exercise.pack_forget()
        show_screen_selection_exercise(actual_category)

def go_back_from_exercise_detail():
    screen_exercise.pack_forget()
    screen_selection_exercise.pack(fill="both", expand=True)


def go_back_from_exercise_detail_random():
    screen_random_exercise.pack_forget()
    screen_random.pack(fill="both", expand=True)

def skip_random_exercise():
    global index_random_exercise
    if index_random_exercise + 1 < len(list_menu_random):
        index_random_exercise += 1
        show_detail_random_exercise(index_random_exercise)
    else:
        # limpiar pantalla
        screen_random_exercise.pack_forget()
        show_random_exercises(list_menu_random)


def go_to_principal_menu_from_users_management():
    screen_users.pack_forget()
    show_screen_exercises()


def go_to_create_user():
    screen_users.pack_forget()
    screen_create_user.pack(fill="both", expand=True)


def go_to_menu_users_management_from_create_user():
    screen_create_user.pack_forget()
    screen_users.pack(fill="both", expand=True)


def go_to_update_user():
    screen_users.pack_forget()
    screen_update_user.pack(fill="both", expand=True)

def go_to_menu_users_management_from_update_user():
    screen_update_user.pack_forget()
    screen_users.pack(fill="both", expand=True)

def saveUsuario():

    username = entry_username_new_user.get()
    password = entry_password_new_user.get()
    name = entry_name_new_user.get()
    last_name = entry_last_name_new_user.get()
    email = entry_email_new_user.get()

    user_to_save = {
        "username": username,
        "password": password,
        "name": name,
        "lastName": last_name,
    }
    user_controller.create_user(user_to_save)

    messagebox.showinfo("Usuario creado", "Usuario creado con éxito")


# Crear la ventana principal
window_general = tk.Tk()
window_general.title("BodyBuilder")
window_general.geometry("600x700")

# //////////////////   Pantalla de login
login_screen = tk.Frame(window_general, bg="#FFC0CB")
login_screen.pack(fill="both", expand=True)

label_user = tk.Label(login_screen, text="Usuario:", fg="black")
label_user.pack(pady=10)

entry_user = tk.Entry(login_screen, bg="white")
entry_user.pack(pady=5)

label_password = tk.Label(login_screen, text="Contraseña:", fg="black")
label_password.pack(pady=5)

entry_password = tk.Entry(login_screen, show="*", bg="white")
entry_password.pack(pady=5)

button_login = tk.Button(login_screen, text="Iniciar sesión", command=validate_login)
button_login.pack(pady=10)

# //////////////////   Pantalla de selección de parte del cuerpo
exercises_screen = tk.Frame(window_general, bg="#FFC0CB")

label_title = tk.Label(
    exercises_screen, text="Selecciona una parte del cuerpo", fg="black"
)
label_title.pack(pady=10)

# recorre las categorías de ejercicios y las muestra

for ctgry in EXERCISES.keys():
    button_category = tk.Button(
        exercises_screen,
        text=ctgry,
        command=lambda c=ctgry: show_screen_selection_exercise(c),
    )
    button_category.pack(pady=5)

# agregar boton random
button_random = tk.Button(
    exercises_screen, text="Random", command=lambda: show_screen_selection_exercise("random")
)
button_random.pack(pady=5)

button_goto_menu_users = tk.Button(
    exercises_screen, text="Menu usuarios", command=go_to_users_management
)
button_goto_menu_users.pack(pady=5)

# //////////////////   Pantalla de menu de usuarios
screen_users = tk.Frame(window_general, bg="#FFC0CB")

label_title_usuarios = tk.Label(
    screen_users, text="Menu de usuarios", fg="black"
)

label_title_usuarios.pack()

button_all_create_user = tk.Button(
    screen_users, text="Crear usuario", command=go_to_create_user
)
button_all_create_user.pack(pady=5)


button_all_update_user = tk.Button(
    screen_users, text="Actualizar usuario", command=go_to_update_user
)
button_all_update_user.pack(pady=5)

button_users_menu_back = tk.Button(
    screen_users, text="Volver", command=go_to_principal_menu_from_users_management
)

button_users_menu_back.pack(pady=5)


# //////////////////   Pantalla de crear usuario
screen_create_user = tk.Frame(window_general, bg="#FFC0CB")

label_title_create_user = tk.Label(
    screen_create_user, text="Crear usuario", fg="black"
)
label_title_create_user.pack()

label_new_username= tk.Label(
    screen_create_user, text="Nombre de usuario", fg="black"
)
label_new_username.pack(pady=5)

entry_username_new_user = tk.Entry(screen_create_user, bg="white")
entry_username_new_user.pack(pady=5)

label_new_password = tk.Label(
    screen_create_user, text="Contraseña", fg="black"
)

label_new_password.pack(pady=5)

entry_password_new_user = tk.Entry(screen_create_user, show="*", bg="white")
entry_password_new_user.pack(pady=5)


label_new_name = tk.Label(
    screen_create_user, text="Nombre", fg="black"
)

label_new_name.pack(pady=5)

entry_name_new_user = tk.Entry(screen_create_user, bg="white")
entry_name_new_user.pack(pady=5)


label_new_last_name = tk.Label(
    screen_create_user, text="Apellido", fg="black"
)

label_new_last_name.pack(pady=5)

entry_last_name_new_user = tk.Entry(screen_create_user, bg="white")
entry_last_name_new_user.pack(pady=5)

label_new_email = tk.Label(
    screen_create_user, text="Correo", fg="black"
)

label_new_email.pack(pady=5)

entry_email_new_user = tk.Entry(screen_create_user, bg="white")
entry_email_new_user.pack(pady=5)


button_create_new_user = tk.Button(
    screen_create_user, text="Crear usuario", command=saveUsuario
)

button_create_new_user.pack(pady=5)

button_back_user_management = tk.Button(
    screen_create_user, text="Volver", command=go_to_menu_users_management_from_create_user
)

button_back_user_management.pack(pady=5)


# //////////////////   Pantalla de actualizacion de usuario

screen_update_user = tk.Frame(window_general, bg="#FFC0CB")

label_title_update_user = tk.Label(
    screen_update_user, text="Actualizar usuario", fg="black"
)

label_title_update_user.pack()

label_update_username = tk.Label(
    screen_update_user, text="Nombre de usuario", fg="black"   
)

label_update_username.pack(pady=5)

entry_update_username = tk.Entry(screen_update_user, bg="white")

entry_update_username.pack(pady=5)

label_update_password = tk.Label(
    screen_update_user, text="Contraseña", fg="black"
)

label_update_password.pack(pady=5)

entry_update_password = tk.Entry(screen_update_user, show="*", bg="white")

entry_update_password.pack(pady=5)

label_update_name = tk.Label(
    screen_update_user, text="Nombre", fg="black"
)

label_update_name.pack(pady=5)

entry_update_name = tk.Entry(screen_update_user, bg="white")

entry_update_name.pack(pady=5)

label_update_last_name = tk.Label(
    screen_update_user, text="Apellido", fg="black"
)

label_update_last_name.pack(pady=5)

entry_update_last_name = tk.Entry(screen_update_user, bg="white")

entry_update_last_name.pack(pady=5)

def updateUser():
    username = entry_update_username.get()
    password = entry_update_password.get()
    name = entry_update_name.get()
    last_name = entry_update_last_name.get()

    user_to_update = {
        "username": username,
        "password": password,
        "name": name,
        "lastName": last_name,
    }
    user_controller.update_user(username,user_to_update)

    messagebox.showinfo("Usuario actualizado", "Usuario actualizado con éxito")

button_update_user_action = tk.Button(
    screen_update_user, text="Actualizar", command=updateUser
)
button_update_user_action.pack(pady=5)

button_back_user_update = tk.Button(
    screen_update_user,
    text="Volver",
    command=go_to_menu_users_management_from_update_user,
)

button_back_user_update.pack()

# //////////////////   Pantalla de selección de ejercicios
screen_selection_exercise = tk.Frame(window_general, bg="#FFC0CB")

label_selection = tk.Label(screen_selection_exercise, text="", fg="black")
label_selection.pack(pady=10)

# //////////////////   Pantalla de ejercicio
screen_exercise = tk.Frame(window_general, bg="#FFC0CB")

label_name = tk.Label(screen_exercise, text="", fg="black")
label_name.pack(pady=10)

label_description = tk.Label(screen_exercise, text="", fg="black")
label_description.pack(pady=10)

label_series = tk.Label(screen_exercise, text="", fg="black")
label_series.pack(pady=10)

label_count_series = tk.Label(screen_exercise, text="", fg="black")
label_count_series.pack(pady=10)

label_timer = tk.Label(screen_exercise, text="", fg="black")
label_timer.pack(pady=10)

label_imagen = tk.Label(screen_exercise)
label_imagen.pack(pady=10)

button_stop = tk.Button(screen_exercise, text="Pausar", command=stop_timer)
button_stop.pack(pady=5)

button_play = tk.Button(screen_exercise, text="Reanudar", command=play_timer)
button_play.pack(pady=5)

boton_saltar = tk.Button(
    screen_exercise, text="Saltar ejercicio", command=skip_exercise
)
boton_saltar.pack(pady=5)

button_back = tk.Button(
    screen_exercise, text="Volver", command=go_back_from_exercise_detail
)

button_back.pack(pady=5)
# //////////////////   Pantalla de menu de random
screen_random = tk.Frame(window_general, bg="#FFC0CB")

# //////////////////   Pantalla de ejercicio random
screen_random_exercise = tk.Frame(window_general, bg="#FFC0CB")

label_random_name = tk.Label(screen_random_exercise, text="", fg="black")
label_name.pack(pady=10)

label_description_random = tk.Label(screen_random_exercise, text="", fg="black")
label_description_random.pack(pady=10)


label_series_random = tk.Label(screen_random_exercise, text="", fg="black")
label_series_random.pack(pady=10)

label_count_series_random = tk.Label(screen_random_exercise, text="", fg="black")
label_count_series_random.pack(pady=10)

label_timer_random = tk.Label(screen_random_exercise, text="", fg="black")
label_timer_random.pack(pady=10)

label_imagen_random = tk.Label(screen_random_exercise)
label_imagen_random.pack(pady=10)

button_stop_random = tk.Button(screen_random_exercise, text="Pausar", command=stop_timer)
button_stop_random.pack(pady=5)

button_play_random = tk.Button(screen_random_exercise, text="Reanudar", command=play_timer_random)
button_play_random.pack(pady=5)

button_back_random = tk.Button(
    screen_random_exercise, text="Volver", command=go_back_from_exercise_detail_random
)
button_back_random.pack(pady=5)

button_back_random = tk.Button(
    screen_random_exercise,
    text="Saltar ejercicio",
    command=skip_random_exercise,
)
button_back_random.pack(pady=5)
# Iniciar la aplicación
window_general.mainloop()
