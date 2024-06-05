import flet as ft 

profile_circle = ft.Stack(
        [
            ft.Icon(
                name=ft.icons.ACCOUNT_CIRCLE,
                color=ft.colors.WHITE,
                size=45
            ),
            ft.Container(
                content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                alignment=ft.alignment.bottom_left,
            ),
        ],
        width=40,
        height=40,
        offset=ft.transform.Offset(0,-0.010)
    )

profile_cont = ft.Container(
                border_radius=15,
                width=50,
                height=50,
                padding=ft.padding.only(2.5,0),
                bgcolor=ft.colors.GREY_400,
                content=ft.Row([
                    profile_circle
                ])
            )

navigation_bar = ft.Container(
    width=60,
    height=700,
    bgcolor=ft.colors.GREY_300,
    animate_opacity=1500,
    border_radius=15,
    padding=ft.padding.only(5,5),
    animate_offset=ft.animation.Animation(1500,'ease'),
    content=ft.Column([
        ft.Row([
            profile_cont
            
        ])
    ])
)