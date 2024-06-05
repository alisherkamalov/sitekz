import flet as ft


city1_container = ft.Container (
    animate_offset=ft.animation.Animation(500,'ease'),
    width=300,
    height=350,
    border_radius=15,
    animate=ft.animation.Animation(500,'ease'),
    bgcolor=ft.colors.WHITE,
    shadow=ft.BoxShadow(
        1,
        100
    ),
    content=ft.Row([
        
    ])
)
city2_container = ft.Container (
    animate_offset=ft.animation.Animation(500,'ease'),
    width=300,
    height=350,
    border_radius=15,
    on_click=True,
    animate=ft.animation.Animation(500,'ease'),
    bgcolor=ft.colors.WHITE,
    shadow=ft.BoxShadow(
        1,
        100
    ),
)
city3_container = ft.Container (
    animate_offset=ft.animation.Animation(500,'ease'),
    width=300,
    height=350,
    on_click=True,
    border_radius=15,
    animate=ft.animation.Animation(500,'ease'),
    bgcolor=ft.colors.WHITE,
    shadow=ft.BoxShadow(
        1,
        100
    ),
)



city_containers = ft.Container(
    animate=ft.animation.Animation(500,'ease'),
    animate_opacity=500,
    animate_scale=ft.animation.Animation(500,'ease'),
    content=ft.Row([
        city1_container,
        city2_container,
        city3_container
        
    ],alignment=ft.MainAxisAlignment.CENTER)
    

)
