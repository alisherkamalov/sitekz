from header import header_container,photo
from profilecontainers import navigation_bar
from endheader import end_header
import flet as ft
add_profile = ft.Column([
            ft.Stack([
                        ft.Column([
                    
                            ft.Row([
                                header_container
                            ],spacing=10)
                        ]),
                    
            ]),
            ft.Row([
                navigation_bar
            ]),
            ft.Row([
                end_header
            ])
            ],spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            animate_opacity=500,
            animate_offset=ft.animation.Animation(500,'ease')
            )  