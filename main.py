from mail import TechIdeiasMail
from nicegui import ui


ui.label('TechIdeiasEmail')

from_email = ui.input(label='From')
password_email = ui.input(label='Email password', password=True, password_toggle_button=True)

to_email = ui.input(label='To')
subject_email = ui.input(label='Subject')
body_email = ui.textarea(label='Body')

email = TechIdeiasMail("", "")
ui.button('Login', on_click=lambda: email.login(from_email.value, password_email.value))
ui.button("Send", on_click=lambda: email.send_email(subject_email.value, body_email.value, to_email.value))

ui.run()