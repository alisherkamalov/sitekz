import flet as ft 
end_img = ft.Image(
                                    src='https://raw.githubusercontent.com/alisherkamalov/sitekz/main/end_image.jpg',
                                    expand=True
                                )
cont_img = ft.Container (
    expand=True,
    content=ft.Row([
        end_img
    ],alignment=ft.MainAxisAlignment.CENTER)
)

black_container = ft.Container (
                                    expand=True,
                                    height=290,
                                    bgcolor=ft.colors.BLACK45
                                )



img_name_site = ft.Image(
            src='thebestkazakhstan.png',
            width=200,
            offset=ft.transform.Offset(0,-0.5)
        )

top_container = ft.Container (
    expand=True,
    height=290,
    padding=10,
    content=ft.Row([
        ft.Row([
            img_name_site
        ],width=200),
        ft.Column([
            ft.Row([
                
            
                ft.Container (
                    width=150,
                    height=5,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                        3,
                        100,
                        color=ft.colors.WHITE
                    )
                ),
            ]),
            ft.Row([
                ft.Container(
                    on_click=True,
                    content=ft.Text(
                    'Наши услуги',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.1,0)
                )
                )
                
            ])
        ],offset=ft.transform.Offset(0,0.1)),
        ft.Column([
            ft.Row([
                
            
            ft.Container (
                width=150,
                height=5,
                bgcolor=ft.colors.WHITE,
                shadow=ft.BoxShadow(
                    3,
                    100,
                    color=ft.colors.WHITE
                )
            ),
            ]),
            ft.Row([
                ft.Container(
                    on_click=True,
                    content=ft.Text(
                    'Профиль',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.3,0)
                )
                )
                
            ])
        ],offset=ft.transform.Offset(0,0.1)),
        ft.Column([
            ft.Row([
                
            
            ft.Container (
                width=200,
                height=5,
                bgcolor=ft.colors.WHITE,
                shadow=ft.BoxShadow(
                    3,
                    100,
                    color=ft.colors.WHITE
                )
            ),
            ]),
            ft.Row([
                ft.Container(
                    on_click=True,
                    content=ft.Text(
                    'Карта Казахстана',
                    size=20,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    offset=ft.transform.Offset(0.1,0)
                )
                )
                
            ])
        ],offset=ft.transform.Offset(0,0.1))
        
    ],spacing=25)
)
end_header = ft.Container(
                    expand=True,
                    height=290,
                    padding=0,
                    shadow=ft.BoxShadow(
                        1,
                        100
                    ),
                    content=ft.Stack([
                            ft.Row([
                                cont_img,
                            ]),
                            
                            ft.Row([
                                black_container
                            ]),
                            ft.Row([
                                top_container
                            ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER
)
)
