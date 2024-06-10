import flet as ft

text_our_services = ft.Text('Наши Услуги', size=20, color=ft.colors.BLACK)
our_services = ft.Container(
        on_click=True,
        animate_opacity=500,
        animate_offset=ft.animation.Animation(500, 'ease'),
        content=ft.Row([
            text_our_services 
        ])
)
text_profile = ft.Text('Профиль', size=20, color=ft.colors.BLACK)
profile = ft.Container (
        on_click=True,
        animate_opacity=500,
        animate_offset=ft.animation.Animation(500, 'ease'),
        content=ft.Row([
            text_profile
        ])
)     
text_our_number1 = ft.Text(' Наш Номер', size=20, color=ft.colors.BLACK)
text_our_number2 = ft.Text('+77478150828', size=20, color=ft.colors.BLUE_300)
our_number = ft.Container (
        height = 100,
        animate_offset=ft.animation.Animation(500, 'ease'),
        offset = ft.transform.Offset(0,0.120),
        content=ft.Column([
            text_our_number1,
            text_our_number2
        ])
    
)
class ServicesContainer(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand=True
        self.height = 100
        
        self.alignment = ft.alignment.center_left
        self.content=ft.Row([
            our_services,
            profile,
            our_number
        ],spacing=35)

logo_img = ft.Image(
        src = 'https://raw.githubusercontent.com/alisherkamalov/sitekz/main/logo.png',
        scale=ft.transform.Scale(1.070),
        animate_opacity=500
        
)
    

logo_container = ft.Container (
    animate=ft.animation.Animation(500,'ease'),
    alignment=ft.alignment.top_left,
    animate_opacity=500,
    padding=0,
        content = ft.Row([
            logo_img
        ])
    )
header_container = ft.Container (
    expand=True,
    height=90,
    bgcolor='white',
    animate_opacity=500,
    opacity=0.9,
    animate_offset=ft.animation.Animation(500,'ease'),
    animate=ft.animation.Animation(500,'ease'),
    alignment=ft.alignment.top_left,
    content=ft.Row([
            logo_container,
            ServicesContainer()
        ],spacing=10),
)
        

        
menu_button = ft.IconButton(
    icon=ft.icons.MENU,
    icon_color=ft.colors.BLACK,
    width=50,
    height=50,
    animate_opacity=500
    
    )
        
        
header_photo = ft.Image (
                src='end_header.jpg',
            )

darkening_photo = ft.Container (
                bgcolor=ft.colors.BLACK45,
                expand=True,
                animate_opacity=500
            )

photo = ft.Container (
    height=732.5,
    content=ft.Stack([
        ft.Row([
            header_photo,
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            darkening_photo,
        ],),
                
            
        
    ])
)
