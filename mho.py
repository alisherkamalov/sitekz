import flet as ft
from header import header_container,logo_container, menu_button,logo_img,our_services,profile,text_our_services,text_profile
import time


def menu_header_open_part1_init():
    menu_button.opacity = 0
    logo_container.opacity = 0
    our_services.opacity = 0
    profile.opacity = 0
    
def menu_header_open_part2_init():
    logo_img.width=150
    time.sleep(0.5)
    text_profile.size=15
    text_profile.offset=ft.transform.Offset(0.135,0)
    text_our_services.size=15
    text_our_services.offset=ft.transform.Offset(0.1,0)
    header_container.height=200
    header_container.opacity = 0.9
    
def menu_header_open_part3_init():
    time.sleep(0.5)
    menu_button.icon=ft.icons.ARROW_BACK_IOS_NEW
    header_container.content=ft.Row([
        ft.Column([
            logo_container,
            our_services,
            profile,
        ]),
                    
        ft.Column([
                        
            ft.Container (
                width=50,
                height=5
            ),
            ft.Row([
                ft.Container (
                width=25,
                height=5
                ),
                    menu_button,
            ]),
                        
                        
        ])
                    
    ],spacing=10
    )
    
def menu_header_open_part4_init():
    time.sleep(0.1)
    logo_container.opacity = 1
    
def menu_header_open_part5_init():
    time.sleep(0.5)
    menu_button.opacity = 1
    our_services.opacity = 1
    profile.opacity = 1
    