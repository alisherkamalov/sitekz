import flet as ft

map_photo = ft.Image(
    expand=True,
    src='map.png',
    animate_opacity=500,
)

info_map = ft.Text(
                'карта казахстана'.upper(),
                color=ft.colors.BLACK,
                weight=ft.FontWeight.W_700,
                animate_opacity=500
            )


map = ft.Container (
    animate_offset=ft.animation.Animation(500,'ease'),
    animate_opacity=500,
    expand=True,
    opacity=1,
    height=1000,
    bgcolor=ft.colors.WHITE,
    offset=ft.transform.Offset(0,0.1),
    content=ft.Column([
        ft.Row([
            ft.Column([
                ft.Row([
                    info_map,
                ]),
                ft.Row([
                    map_photo
                ])
            ],alignment=ft.MainAxisAlignment.START)
            
        ],alignment=ft.MainAxisAlignment.CENTER),
        
        
        
    ],alignment=ft.MainAxisAlignment.CENTER)
)