import flet as ft

def main(page: ft.Page):

    # Lista de opciones para el ListBox
    options = [f"Item {i}" for i in range(1, 11)]
    
    # Variable para almacenar el índice actual del elemento seleccionado
    current_index = 0

    # Crear los controles de texto para ListView
    list_items = [ft.Text(option) for option in options]

    # Crear una columna para contener los elementos
    column = ft.Column(controls=list_items)

    # Crear ListView con la columna
    list_view = ft.ListView(
        controls=[column],
        spacing=5,
        expand=True,
        height=200
    )

    # Función para manejar eventos de teclado
    def on_keyboard_event(e: ft.KeyboardEvent):
        nonlocal current_index
        
        # Detectar la tecla de flecha hacia abajo
        if e.key == "ArrowDown":
            # Desseleccionar el elemento actual
            list_items[current_index].color = ft.colors.BLACK
            # Incrementar el índice del elemento seleccionado
            current_index = (current_index + 1) % len(list_items)
            # Seleccionar el nuevo elemento
            list_items[current_index].color = ft.colors.BLUE

        # Detectar la tecla de flecha hacia arriba
        elif e.key == "ArrowUp":
            # Desseleccionar el elemento actual
            list_items[current_index].color = ft.colors.BLACK
            # Decrementar el índice del elemento seleccionado
            current_index = (current_index - 1) % len(list_items)
            # Seleccionar el nuevo elemento
            list_items[current_index].color = ft.colors.BLUE
        
        page.update()  # Refrescar la página para reflejar el cambio

    # Configurar la página para escuchar eventos de teclado
    page.on_keyboard_event = on_keyboard_event

    # Inicialmente marcar el primer elemento como seleccionado
    list_items[current_index].color = ft.colors.BLUE

    # Agregar el ListView a la página
    page.add(list_view)

ft.app(target=main)
