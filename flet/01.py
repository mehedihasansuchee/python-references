import flet as ft

def main(page: ft.Page):
    # Create a text field
    text_field = ft.TextField(label="Enter your name")

    # Define a function to handle button click
    def button_clicked(e):
        text_field.value = f"Hello, {text_field.value}!"
        page.update()

    # Create a button
    button = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    # Add the text field and button to the page
    page.add(
        text_field,
        button
    )

# Run the app
ft.app(target=main)