import flet as ft 

entry_first_name_reg = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Имя",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

entry_last_name_reg = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Фамилия",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

entry_login_reg = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Логин",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

entry_pass_reg = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Пароль",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

entry_phone_num_reg = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Номер телефона",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

desc_pass_reg = ft.Text(
        'Пароль должен состоять из 6 цифр и латинских букв',
        color=ft.colors.BLACK,
        size=15,
        offset=ft.transform.Offset(0.050,0),
        animate_opacity=500
)

desc_pass_auth = ft.Text(
        'Пароль должен состоять из 6 цифр и латинских букв',
        color=ft.colors.BLACK,
        size=15,
        offset=ft.transform.Offset(0.050,0),
        animate_opacity=500
)

entry_login_auth = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Логин",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)

entry_pass_auth = ft.CupertinoTextField(
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    border=ft.border.all(0,color=ft.colors.WHITE),
    placeholder_text="Пароль",
    placeholder_style=ft.TextStyle(color=ft.colors.GREY_400)
)


sign_up2 = ft.Container (
    expand=True,
    height=50,
    bgcolor=ft.colors.GREY_200,
    scale=ft.transform.Scale(0.950),
    on_click=True,
    border_radius=7,
    content=ft.Row([
        ft.Text(
            'зарегистрироваться'.upper(),
            color=ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=20,
        )
    ],alignment=ft.MainAxisAlignment.CENTER)
)

sign_in = ft.Container (
    expand=True,
    height=50,
    bgcolor=ft.colors.GREY_200,
    scale=ft.transform.Scale(0.950),
    on_click=True,
    border_radius=7,
    content=ft.Row([
        ft.Text(
            'авторизоваться'.upper(),
            color=ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=20,
        )
    ],alignment=ft.MainAxisAlignment.CENTER)
)

back = ft.Container (
    expand=True,
    height=50,
    bgcolor=ft.colors.GREY_200,
    scale=ft.transform.Scale(0.950),
    on_click=True,
    border_radius=7,
    content=ft.Row([
        ft.Text(
            'назад'.upper(),
            color=ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=20,
        )
    ],alignment=ft.MainAxisAlignment.CENTER)
)

sign_up = ft.Container (
    expand=True,
    height=50,
    bgcolor=ft.colors.GREY_200,
    scale=ft.transform.Scale(0.950),
    on_click=True,
    border_radius=7,
    content=ft.Row([
        ft.Text(
            'зарегистрироваться'.upper(),
            color=ft.colors.BLACK,
            weight=ft.FontWeight.W_700,
            size=20,
        )
    ],alignment=ft.MainAxisAlignment.CENTER)
)


auth_cont = ft.Container (
    width=500,
    height=425,
    bgcolor=ft.colors.WHITE,
    border_radius=7,
    animate_opacity=500,
    animate_scale=ft.animation.Animation(500,'ease'),
    padding=ft.padding.only(0,15),
    shadow=ft.BoxShadow(
        1,
        100
    ),
    content=ft.Column([
        ft.Row([
            ft.Text('Авторизация'.upper(), size=20, weight=ft.FontWeight.W_800)
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Container (
                expand=True,
                height=175,
                scale=ft.transform.Scale(0.9),
                border_radius=7,
                border=ft.border.all(0.5,color=ft.colors.GREY_400),
                padding=ft.padding.only(0,10),
                content=ft.Column([
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.ACCOUNT_CIRCLE,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_login_auth
                            ])
                        )
                    ]),
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.PASSWORD,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_pass_auth
                            ])
                        )
                    ]),
                    ft.Row([
                        desc_pass_auth
                    ]),
                    
                ])
            )
        ]),
        ft.Row([
            sign_in
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            sign_up
        ],alignment=ft.MainAxisAlignment.CENTER),
    ],scroll='auto')
)

reg_cont = ft.Container (
    width=500,
    height=425,
    bgcolor=ft.colors.WHITE,
    border_radius=7,
    animate_opacity=500,
    animate_scale=ft.animation.Animation(500,'ease'),
    padding=ft.padding.only(0,15),
    shadow=ft.BoxShadow(
        1,
        100
    ),
    content=ft.Column([
        ft.Row([
            ft.Text('Регистрация'.upper(), size=20, weight=ft.FontWeight.W_800)
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Container (
                expand=True,
                height=350,
                scale=ft.transform.Scale(0.9),
                border_radius=7,
                border=ft.border.all(0.5,color=ft.colors.GREY_400),
                padding=ft.padding.only(0,10),
                content=ft.Column([
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.ACCOUNT_CIRCLE,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_first_name_reg
                            ])
                        )
                    ]),
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.ACCOUNT_CIRCLE,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_last_name_reg
                            ])
                        )
                    ]),
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.ACCOUNT_CIRCLE,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_login_reg
                            ])
                        )
                    ]),
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.PASSWORD,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_pass_reg
                            ])
                        )
                    ]),
                    ft.Row([
                        desc_pass_reg
                        
                    ]),
                    ft.Row([
                        ft.Container (
                            expand=True,
                            height=50,
                            border=ft.border.all(0.5,color=ft.colors.GREY_400),
                            border_radius=7,
                            
                            scale=ft.transform.Scale(0.950),
                            content=ft.Row([
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(
                                            name=ft.icons.PHONE,
                                            color=ft.colors.GREY_400,
                                            size=25,
                                            offset=ft.transform.Offset(0.275,0.425)
                                        ),
                                    ]),
                                    
                                ]),
                                entry_phone_num_reg
                            ])
                        )
                    ]),
                    
                ])
            )
        ]),
        ft.Row([
            sign_up2
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            back
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Text()
        ])
    ],scroll='auto')
)