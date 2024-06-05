import flet as ft 
from reg_and_auth_container import reg_cont,entry_first_name_reg,entry_last_name_reg,entry_login_reg,entry_pass_reg,entry_phone_num_reg,desc_pass_reg,sign_up2,back

st_reg = ft.Column([
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