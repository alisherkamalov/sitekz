import flet as ft 
from city import city_containers


cityes = ft.Container (
                expand=True,
                height=500,
                bgcolor=ft.colors.WHITE,
                animate=ft.animation.Animation(500,'ease'),
                animate_opacity=500,
                animate_scale=ft.animation.Animation(500,'ease'),
                content=ft.Row([
                    city_containers
                ],alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.alignment.top_center
            )