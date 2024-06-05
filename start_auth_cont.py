import flet as ft 
from reg_and_auth_container import entry_login_auth,entry_pass_auth,sign_in,sign_up,desc_pass_auth

st_auth = ft.Column([
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