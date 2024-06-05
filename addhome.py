from header import header_container,photo
from body import cityes
from map import map
from endheader import end_header
import flet as ft


add_home = ft.Column([
            ft.Stack([
                        photo,
                        ft.Column([
                    
                            ft.Row([
                                header_container
                            ],spacing=10)
                        ]),
                    
            ]),
            ft.Row([
                cityes
            ]),
            
            ft.Row([
                map
            ]),
            ft.Row([
                end_header
            ])
            ],spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            animate_opacity=500,
            animate_offset=ft.animation.Animation(500,'ease')
            )  