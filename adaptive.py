import flet as ft
from header import header_container,logo_container,ServicesContainer, menu_button,logo_img,our_number,our_services,profile,text_our_services,text_our_number1,text_our_number2,text_profile,photo,header_photo,darkening_photo
from city import city_containers,city1_container,city2_container,city3_container
from body import cityes
from map import info_map,map,map_photo
from reg_and_auth_container import auth_cont, reg_cont,desc_pass_reg,desc_pass_auth
from endheader import end_img,black_container,img_name_site,top_container
from containers_to_scrolling import container_to_profile, container_services, container_to_map
import time


def pc():
    cityes.height = 500
    info_map.size=50
    auth_cont.width=500
    reg_cont.width=500
    auth_cont.height=425
    reg_cont.height=425
    img_name_site.expand=True
    img_name_site.scale=ft.transform.Scale(1)
    container_to_profile.offset=ft.transform.Offset(0.225,0)
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
    desc_pass_auth.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    desc_pass_reg.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    city1_container.on_click=None
    city2_container.on_click=None
    city3_container.on_click=None
    map.height=1000
    end_img.scale=ft.transform.Scale(2.010)
    info_map.offset=ft.transform.Offset(0,0)
    map_photo.offset=ft.transform.Offset(0,0)
    map_photo.opacity = 1
    map.bgcolor=ft.colors.WHITE
    info_map.opacity=1
    map.opacity = 1
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
    img_name_site.offset=ft.transform.Offset(0,-0.5)
    header_photo.scale=ft.transform.Scale(2)
    our_services.opacity = 1
    profile.opacity = 1
    header_container.content=ft.Row([
        logo_container,
        ServicesContainer()
    ],spacing=10)
    end_img.offset=ft.transform.Offset(0,0.5)
    black_container.offset=ft.transform.Offset(0,0)
    black_container.scale=ft.transform.Scale(1)
    
def mobile():
    desc_pass_auth.value = 'Пароль должен состоять из 6 цифр и\nлатинских букв'
    desc_pass_reg.value = 'Пароль должен состоять из 6 цифр и\nлатинских букв'
    info_map.size=25
    img_name_site.offset=ft.transform.Offset(0,0)
    auth_cont.width=300
    reg_cont.width=300
    auth_cont.height=375
    reg_cont.height=375
    map.offset=ft.transform.Offset(0,0)
    map_photo.opacity = 1
    info_map.opacity=1
    map.opacity = 1
    map.bgcolor=None
    map.height=700
    container_to_profile.offset=ft.transform.Offset(0,0)
    end_img.scale=ft.transform.Scale(7.5)
    info_map.offset=ft.transform.Offset(0,0)
    map_photo.offset=ft.transform.Offset(0,0)
    map.content=ft.Column([
        ft.Row([
            ft.Container (
                expand=True,
                height=100
            )
        ]),
        ft.Row([
            info_map
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            map_photo
        ],alignment=ft.MainAxisAlignment.CENTER),
    ])
    city1_container.on_hover=None
    city2_container.on_hover=None
    city3_container.on_hover=None
    city_containers.padding=ft.padding.only(15,0)
    city_containers.content=ft.Column([
        city1_container,
        city2_container,
        city3_container
    ])
    cityes.height = 1100
    cityes.content = ft.Row([
        ft.Column([
            city_containers
        ],alignment=ft.MainAxisAlignment.CENTER)
    ],expand=True)
    header_photo.scale=ft.transform.Scale(3)
    header_photo.offset=ft.transform.Offset(0,1)
    photo.height=500
    darkening_photo.height = 500
    header_container.content=ft.Row([
        logo_container,
        menu_button
    ],spacing=10)
    end_img.offset=ft.transform.Offset(0,3.250)
    black_container.offset=ft.transform.Offset(0,0)
    black_container.scale=ft.transform.Scale(1)
    img_name_site.scale=ft.transform.Scale(3)
    img_name_site.expand=False
    
    top_container.content=ft.Column([
        ft.Row([
            img_name_site
        ],height=75),
        ft.Row([
            ft.Container (
                    width=5,
                    height=35,
                    border_radius=7,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                        3,
                        100,
                        color=ft.colors.WHITE
                    )
            ),
            container_services
        ]),
        ft.Row([
            ft.Container (
                    width=5,
                    height=35,
                    border_radius=7,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                        3,
                        100,
                        color=ft.colors.WHITE
                    )
            ),
            container_to_profile
        ]),
        ft.Row([
            ft.Container (
                    width=5,
                    height=35,
                    border_radius=7,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(
                        3,
                        100,
                        color=ft.colors.WHITE
                    )
            ),
            container_to_map
        ])
    ])
def laptop():
    desc_pass_auth.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    desc_pass_reg.value = 'Пароль должен состоять из 6 цифр и латинских букв'
    photo.height=590
    auth_cont.width=500
    reg_cont.width=500
    auth_cont.height=425
    reg_cont.height=425
    map_photo.opacity = 1
    info_map.opacity=1
    map.opacity = 0
    map.height=1000
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
                width=15,
                height=5,
                
                border_radius=7,
                bgcolor=ft.colors.WHITE,
                shadow=ft.BoxShadow(
                    3,
                    100,
                    color=ft.colors.WHITE
                ),

            ),
            ]),
            ft.Row([
                container_to_map
                
            ])
        ],offset=ft.transform.Offset(0,0.1))
        
    ],spacing=25)
    img_name_site.offset=ft.transform.Offset(0,-0.5)
    map.bgcolor=ft.colors.WHITE
    darkening_photo.height = 590
    info_map.size=50
    city1_container.on_click=None
    city2_container.on_click=None
    city3_container.on_click=None
    cityes.height = 500
    end_img.scale=ft.transform.Scale(2.010)
    info_map.offset=ft.transform.Offset(0,0)
    map_photo.offset=ft.transform.Offset(0,0)
    map.content=ft.Column([
        ft.Row([
            info_map
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            map_photo
        ],alignment=ft.MainAxisAlignment.CENTER),
    ])
    city_containers.padding=ft.padding.only(0,0)
    city_containers.content=ft.Row([
        city1_container,
        city2_container,
        city3_container
    ])
    cityes.content = ft.Row([
        city_containers
    ],alignment=ft.MainAxisAlignment.CENTER)
    header_photo.scale=ft.transform.Scale(1)
    header_photo.offset=ft.transform.Offset(0,0)
    our_services.opacity = 1
    profile.opacity = 1
    header_container.content=ft.Row([
        logo_container,
        ServicesContainer()
    ],spacing=10)
    end_img.offset=ft.transform.Offset(0,0.5)
    black_container.offset=ft.transform.Offset(0,0)
    black_container.scale=ft.transform.Scale(1)
    img_name_site.scale=ft.transform.Scale(1)
    container_to_profile.offset=ft.transform.Offset(0.225,0)
    img_name_site.expand=True