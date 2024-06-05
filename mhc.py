import flet as ft
from header import header_container,logo_container, menu_button,logo_img,our_services,profile,text_our_services,text_profile
import time


def menu_header_close_part1_init():
    menu_button.opacity = 0
    logo_container.opacity = 0
    our_services.opacity = 0
    profile.opacity = 0
    
def menu_header_close_part2_init():
    time.sleep(0.5)
    text_profile.size=20
    text_profile.offset=ft.transform.Offset(0.135,0)
    text_our_services.size=20
    logo_img.width=200
    header_container.height=100
    header_container.opacity = 1

def menu_header_close_part3_init():
    time.sleep(0.5)
    menu_button.icon=ft.icons.MENU
    header_container.content=ft.Row([
        logo_container,
        menu_button,
    ],spacing=10
    )
    
def menu_header_close_part4_init():
    time.sleep(0.1)
    logo_container.opacity = 1
    
def menu_header_close_part5_init():
    time.sleep(0.5)
    menu_button.opacity = 1