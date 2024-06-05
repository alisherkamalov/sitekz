import flet as ft
from header import header_container,logo_container,ServicesContainer, menu_button,logo_img,our_number,our_services,profile,text_our_services,text_our_number1,text_our_number2,text_profile,photo,header_photo,darkening_photo
from city import city_containers,city1_container,city2_container,city3_container
from body import cityes
from map import info_map,map,map_photo
from reg_and_auth_container import auth_cont, reg_cont,desc_pass_reg,desc_pass_auth
import time
from endheader import end_header,end_img,black_container,img_name_site,top_container
from containers_to_scrolling import container_to_profile,container_to_map,container_services

def big_window():
    cityes.height = 500
    info_map.size=50
    auth_cont.width=500
    reg_cont.width=500
    auth_cont.height=425
    reg_cont.height=425
    img_name_site.scale=ft.transform.Scale(1)
    end_img.scale=ft.transform.Scale(2)
    container_to_profile.offset=ft.transform.Offset(0.225,0)
    desc_pass_auth.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    desc_pass_reg.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    city1_container.on_click=None
    city2_container.on_click=None
    city3_container.on_click=None
    top_container.content=ft.Row([
        ft.Row([
            img_name_site
        ],width=200),
        ft.Column([
            ft.Row([
                
            
                ft.Container (
                    width=150,
                    height=5,
                    border_radius=7,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                        3,
                        100,
                        color=ft.colors.WHITE
                    )
                ),
            ]),
            ft.Row([
                container_services
                
            ])
        ],offset=ft.transform.Offset(0,0.1)),
        ft.Column([
            ft.Row([
                
            
            ft.Container (
                width=150,
                height=5,
                border_radius=7,
                bgcolor=ft.colors.WHITE,
                shadow=ft.BoxShadow(
                    3,
                    100,
                    color=ft.colors.WHITE
                )
            ),
            ]),
            ft.Row([
                container_to_profile
                
            ])
        ],offset=ft.transform.Offset(0,0.1)),
        ft.Column([
            ft.Row([
                
            
            ft.Container (
                width=200,
                height=5,
                border_radius=7,
                bgcolor=ft.colors.WHITE,
                shadow=ft.BoxShadow(
                    3,
                    100,
                    color=ft.colors.WHITE
                )
            ),
            ]),
            ft.Row([
                container_to_map
                
            ])
        ],offset=ft.transform.Offset(0,0.1))
        
    ],spacing=25)
    img_name_site.offset=ft.transform.Offset(0,-0.75)
    map.content=ft.Column([
        ft.Row([
            info_map
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            map_photo
        ],alignment=ft.MainAxisAlignment.CENTER),
    ])
    city_containers.padding=ft.padding.only(0,0)
    header_photo.offset=ft.transform.Offset(0,0)
    city_containers.content=ft.Row([
        city1_container,
        city2_container,
        city3_container
    ])
    cityes.content = ft.Row([
        city_containers
    ],alignment=ft.MainAxisAlignment.CENTER)
    photo.height=732.5
    darkening_photo.height = 732.5
    header_photo.scale=ft.transform.Scale(1)
    our_services.opacity = 1
    profile.opacity = 1
    header_container.content=ft.Row([
        logo_container,
        ServicesContainer()
    ],spacing=10)
    end_img.offset=ft.transform.Offset(0,0.5)
    black_container.offset=ft.transform.Offset(0,0.015)
    black_container.scale=ft.transform.Scale(1.025)
add_home_big1 = ft.Column([
            ft.Stack([
                        photo,
                        ft.Column([
                    
                            ft.Row([
                                header_container
                            ],spacing=10)
                        ]),
                    
            ]),
            ft.Row([
                cityes
            ]),
            ft.Row([
                ft.Container(
                    expand=True,
                    height=300,
                    bgcolor=ft.colors.WHITE
                )
            ]),

            ft.Row([
                map
            ]),
            ft.Row([
                end_header
            ])
            ],spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            animate_opacity=500,
            animate_offset=ft.animation.Animation(500,'ease')
            )


add_home_big2 = ft.Column([
            ft.Stack([
                        photo,
                        ft.Column([
                    
                            ft.Row([
                                header_container
                            ],spacing=10)
                        ]),
                    
            ]),
            ft.Row([
                cityes
            ]),
        
            ft.Row([
                map
            ]),
            ft.Row([
                end_header
            ])
            ],spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            animate_opacity=500,
            animate_offset=ft.animation.Animation(500,'ease')
            )  