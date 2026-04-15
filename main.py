import dearpygui.dearpygui as dpg
from mail import TechIdeiasMail

dpg.create_context()
dpg.create_viewport(title="TechIdeiasMail", width=500, height=500)
dpg.setup_dearpygui()

with dpg.window(label="TechIdeiasMail", tag="TechIdeiasMail"):
    dpg.add_text("Email")
    dpg.add_input_text(tag="sender_email")
    dpg.add_text("App Password")
    dpg.add_input_text(tag="app_password")
    email = TechIdeiasMail(f"{dpg.get_value('sender_email')}", f"{dpg.get_value('app_password')}")

dpg.show_viewport()
dpg.set_primary_window("TechIdeiasMail", True)
dpg.start_dearpygui()
dpg.destroy_context()