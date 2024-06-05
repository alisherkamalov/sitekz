import flet as ft

container_services = ft.Container(
                    on_click=True,
                    content=ft.Text(
                    'Наши услуги',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.1,0)
                )
)


container_to_profile = ft.Container(
                    on_click=True,
                    content=ft.Text(
                    value='Профиль',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.15,0)
                )
                )

container_to_map = ft.Container(
                    on_click=True,
                    content=ft.Text(
                    'Карта Казахстана',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.075,0)
                )
                )