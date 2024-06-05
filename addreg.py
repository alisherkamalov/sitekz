from header import header_container,photo
from reg_and_auth_container import reg_cont
import flet as ft
from body import cityes

add_reg = ft.Column([
            ft.Stack([
                        photo,
                        ft.Column([
                    
                            ft.Row([
                                header_container
                            ],spacing=10),
                            ft.Row([
                                reg_cont
                            ],alignment=ft.MainAxisAlignment.CENTER),
                        ],spacing=15),
                    
            ]),
            ft.Row([
                ft.Container (
                    bgcolor=ft.colors.WHITE,
                    expand=True,
                    height=1200,
                    offset=ft.transform.Offset(0,0)
                    )
            ]),
            ],spacing=0)  