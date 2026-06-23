import dearpygui.dearpygui as dpg
from mail import TechIdeiasMail

dpg.create_context()
dpg.create_viewport(title="TechIdeiasMail", width=500, height=500)
dpg.setup_dearpygui()

def send_email(sender, app_data, user_data):
    email_object = TechIdeiasMail(f"{dpg.get_value('sender_email')}", f"{dpg.get_value('app_password')}")
    emails = [email for email in str(dpg.get_value("emails")).strip().replace("\n", "").split(sep=",")]
    email_object.send_email(dpg.get_value("subject"), dpg.get_value("body"), emails)

with dpg.window(label="TechIdeiasMail", tag="TechIdeiasMail"):
    dpg.add_text("Email")
    dpg.add_input_text(tag="sender_email")
    dpg.add_text("App Password")
    dpg.add_input_text(tag="app_password")
    
    with dpg.group(horizontal=True):
        dpg.add_text("List of emails")
        dpg.add_input_text(multiline=True, hint="email@email.com, email2@email2.com", tag="emails")

    with dpg.group(horizontal=True):
        dpg.add_text("Subject")
        dpg.add_input_text(tag="subject")

    with dpg.group(horizontal=True):
        dpg.add_text("Message")
        dpg.add_input_text(multiline=True, tag="body")

    dpg.add_button(label="Send", callback=send_email)
         
dpg.show_viewport()
dpg.set_primary_window("TechIdeiasMail", True)
dpg.start_dearpygui()
dpg.destroy_context()