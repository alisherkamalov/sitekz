import flet as ft
import re
import time
from header import menu_button,our_number,our_services,profile,photo,darkening_photo,logo_container,header_photo,header_container
from city import city1_container,city2_container,city3_container,city_containers
from body import cityes
from addhome import add_home
from map import map,map_photo,info_map
from addauth import add_auth
from addreg import add_reg
from addprofile import add_profile
from start_reg_cont import st_reg
from start_auth_cont import st_auth
from endheader import end_header,black_container,top_container
from profilecontainers import navigation_bar,profile_cont
from adaptive_for_big_window import add_home_big1,big_window,add_home_big2
from reg_and_auth_container import sign_up,back,sign_up2,entry_pass_reg,desc_pass_reg,desc_pass_auth,auth_cont,reg_cont,sign_in,entry_pass_auth,entry_first_name_reg,entry_last_name_reg,entry_login_auth,entry_login_reg,entry_phone_num_reg
from adaptive import pc,mobile,laptop
from mho import menu_header_open_part1_init, menu_header_open_part2_init, menu_header_open_part3_init, menu_header_open_part4_init, menu_header_open_part5_init
from mhc import menu_header_close_part1_init,menu_header_close_part2_init,menu_header_close_part3_init,menu_header_close_part4_init,menu_header_close_part5_init


def main(page: ft.Page):
        page.route = f'/home/'
        page.bgcolor='white'
        page.scroll = 'auto'
        page.padding = 0
        page.spacing = 0
        page.clean()
        adaptive_text = ft.Text(f'{page.width}',color=ft.colors.RED,bottom=50,right=50, size=50,opacity=0)
        page.overlay.append(adaptive_text)
        
        def routing_to_auth(event):
            
            page.route = f'/authorization/'
            city_containers.opacity = 0
            city_containers.scale=ft.transform.Scale(0.9)
            reg_cont.opacity = 0
            reg_cont.scale=ft.transform.Scale(0.9)
            page.update()
            time.sleep(0.5)
            
            page_adaptive(None)
            page.update()
            
        def home_view(event):
            page.clean()
            page.route = f'/home/'
            auth_cont.opacity = 0
            auth_cont.scale=ft.transform.Scale(0.9)
            reg_cont.opacity = 0
            reg_cont.scale=ft.transform.Scale(0.9)
            city_containers.opacity = 1
            city_containers.scale=ft.transform.Scale(1)
            page.update()
            time.sleep(0.5)
            
            page_adaptive(None)
            page.update()
            
        def hover_white_line(event):
            
            if event.data == 'true':
                event.control.width=250
            elif event.data == 'false':
                event.control.width=15
            page.update()
            
        def routing_to_reg(event):
            reg_cont.content = st_reg
            page.route = f'/registration/'
            auth_cont.opacity = 0
            auth_cont.scale=ft.transform.Scale(0.9)
            page.update()
            time.sleep(0.5)
            page.clean()
            page_adaptive(None)
            page.update()
            
        def back_to_auth(event):
            routing_to_auth(None)
            page.update()
            
        def hover_profile(event):
            if event.data == 'true':
                event.control.offset=ft.transform.Offset(0,-0.025)
            elif event.data == 'false':
                event.control.offset=ft.transform.Offset(0,0)
            page.update()
            
        def hover(event):
            if event.data == 'true':
                event.control.offset=ft.transform.Offset(0,-0.1)
            elif event.data == 'false':
                event.control.offset=ft.transform.Offset(0,0)
            page.update()
            
        def container1(_):
            city1_container.offset=ft.transform.Offset(0,-0.1)
            city2_container.offset=ft.transform.Offset(0,0)
            city3_container.offset=ft.transform.Offset(0,0)
            page.update()
            
        def container2(_):
            city1_container.offset=ft.transform.Offset(0,0)
            city2_container.offset=ft.transform.Offset(0,-0.1)
            city3_container.offset=ft.transform.Offset(0,0)
            page.update()
            
        def container3(_):
            city1_container.offset=ft.transform.Offset(0,0)
            city2_container.offset=ft.transform.Offset(0,0)
            city3_container.offset=ft.transform.Offset(0,-0.1)
            page.update()
            
        def route_profile():
            page.clean()
            navigation_bar.opacity = 0
            navigation_bar.offset = ft.transform.Offset(-0.5,0)
            page.route = "/profile/"
            page.add(add_profile)
            header_container.opacity = 1
            page.update()
            time.sleep(0.5)
            navigation_bar.opacity = 1
            navigation_bar.offset = ft.transform.Offset(0,0)
            page.update()
            time.sleep(0.5)
            
            
        def registration_to_supabase(event):
            
            pattern = r'^[a-zA-Z0-9]{6,}$'
            
            passw_reg = entry_pass_reg.value
            
            login_reg = entry_login_reg.value
    
            # Проверяем, соответствует ли пароль шаблону
            if re.match(pattern,passw_reg):
                desc_pass_reg.opacity = 0
                page.update()
                time.sleep(0.5)
                desc_pass_reg.color=ft.colors.GREEN
                desc_pass_reg.opacity = 1
                page.update()
                
                

                 # Проверка, найден ли пользователь
                
                reg_cont.opacity = 0
                page.update()
                time.sleep(0.5)
                reg_cont.content=ft.Column([
                    ft.Row([
                        ft.Image(
                                src='not new account.png'
                        )
                    ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Text(
                            f'Данный аккаунт уже\n       существует!',
                            weight=ft.FontWeight.W_700,
                            size=20,
                            color=ft.colors.BLACK,
                            offset=ft.transform.Offset(0,-1)
                        ),
                    ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                ])
                page.update()
                reg_cont.opacity = 1
                page.update()
                time.sleep(2)
                reg_cont.opacity = 0
                page.update()
                time.sleep(0.5)
                reg_cont.content=st_reg
                page.update()
                reg_cont.opacity = 1
                page.update()
                time.sleep(0.5)
            else: 
                    reg_cont.opacity = 0
                    page.update()
                    time.sleep(0.5)
                    reg_cont.content=ft.Column([
                        ft.Row([
                            ft.Image(
                                src='new account.png'
                            )
                        ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Text(
                                f'Вы успешно создали\nаккаунт {entry_login_reg.value}',
                                weight=ft.FontWeight.W_700,
                                size=20,
                                color=ft.colors.BLACK,
                                offset=ft.transform.Offset(0,-1)
                            ),
                        ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                    ])
                    page.update()
                    reg_cont.opacity = 1
                    page.update()
                    time.sleep(2)
                    reg_cont.opacity = 0
                    page.update()
                    time.sleep(0.5)
                    reg_cont.content=st_reg
                    auth_cont.opacity = 0
                    auth_cont.scale=ft.transform.Scale(0.9)
                    page.update()
                    page.clean()
                    page.add(add_auth)
                    page.update()
                    time.sleep(0.1)
                    auth_cont.opacity = 1
                    auth_cont.scale=ft.transform.Scale(1)
                    page.update()
                    time.sleep(0.5)
            desc_pass_reg.opacity = 0
            page.update()
            time.sleep(0.5)
            desc_pass_reg.color=ft.colors.RED
            desc_pass_reg.opacity = 1
            page.update()
                
            page.update()
            
        def authorization_to_supabase(event):
            
            pattern = r'^[a-zA-Z0-9]{6,}$'
            
            passw_auth = entry_pass_auth.value
            
            login_auth = entry_login_auth.value
    
            # Проверяем, соответствует ли пароль шаблону
            if re.match(pattern,passw_auth):
                desc_pass_auth.opacity = 0
                page.update()
                time.sleep(0.5)
                desc_pass_auth.color=ft.colors.GREEN
                desc_pass_auth.opacity = 1
                page.update()
                
                # Проверка, найден ли пользователь
                darkening_photo.opacity = 0
                auth_cont.opacity = 0
                header_photo.opacity = 0
                city_containers.opacity = 0
                map.opacity = 0
                header_container.opacity = 0
                page.update()
                time.sleep(0.5)
                route_profile()
                 
                auth_cont.opacity = 0
                page.update()
                time.sleep(0.5)
                auth_cont.content=ft.Column([
                        ft.Row([
                            ft.Image(
                                src='not new account.png'
                            )
                        ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Text(
                                f'Аккаунт не найден!',
                                weight=ft.FontWeight.W_700,
                                size=25,
                                color=ft.colors.BLACK,
                                offset=ft.transform.Offset(0,-1)
                            ),
                        ],expand=True,alignment=ft.MainAxisAlignment.CENTER),
                    ])
                page.update()
                time.sleep(0.5)
                auth_cont.opacity = 1
                page.update()
                time.sleep(2)
                auth_cont.opacity = 0
                page.update()
                time.sleep(0.5)
                auth_cont.content=st_auth
                page.update()
                auth_cont.opacity = 1
                page.update()
                time.sleep(0.5)
                
            desc_pass_auth.opacity = 0
            page.update()
            time.sleep(0.5)
            desc_pass_auth.color=ft.colors.RED
            desc_pass_auth.opacity = 1
            page.update()
                
            page.update()
            
        def page_adaptive(event):
            page.clean()
            adaptive_text.value=f'{page.width}'
            adaptive_text.update
            if page.route == f'/home/':
                        if 1301 <= page.width <= 2544:
                            header_photo.opacity = 1
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            big_window()
                            map_photo.offset=ft.transform.Offset(0,-0.300)
                            info_map.offset=ft.transform.Offset(0,-3)
                            header_photo.scale=ft.transform.Scale(3)
                            map.offset=ft.transform.Offset(0,0)
                            end_header.offset=ft.transform.Offset(0,0)
                            page.add(add_home_big1)
            if page.route == f'/home/':
                        if 2545 <= page.width <= 6000:
                            header_photo.opacity = 1
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            big_window()
                            map_photo.offset=ft.transform.Offset(0,-0.300)
                            info_map.offset=ft.transform.Offset(0,0)
                            header_photo.scale=ft.transform.Scale(4)
                            map.offset=ft.transform.Offset(0,0)
                            map.height = 1600
                            end_header.height=400
                            black_container.height=410
                            top_container.height=400
                            page.add(add_home_big2)
            if page.route == f'/home/':
                        if 3800 <= page.width <= 3900:
                            header_photo.opacity = 1
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            big_window()
                            map.height=1100
                            map_photo.offset=ft.transform.Offset(0,-0.300)
                            info_map.offset=ft.transform.Offset(0,0)
                            header_photo.scale=ft.transform.Scale(4)
                            end_header.offset=ft.transform.Offset(0,0)
                            map.offset=ft.transform.Offset(0,0)
                            page.add(add_home_big2)
            if page.route == f'/home/':
                        if 920 <= page.width <= 1300 and page.width != 1024:
                            header_photo.opacity = 1
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            pc()
                            map.opacity = 1
                            map.offset=ft.transform.Offset(0,-0.010)
                            header_photo.scale=ft.transform.Scale(2)
                            map.height = 1100
                            end_header.height=290
                            black_container.height=300
                            top_container.height=290
                            page.add(add_home)
            if page.route == f'/home/':
                        if page.width <= 909:
                            header_photo.opacity = 1
                            darkening_photo.opacity = 1
                            city1_container.on_click=container1
                            city2_container.on_click=container2
                            city3_container.on_click=container3
                            map.on_hover=None
                            page.add(add_home)
                            mobile()
            if page.route == f'/home/':
                        if page.width == 912:
                            photo.height=590
                            header_photo.opacity = 1
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            mobile()
                            header_photo.scale=ft.transform.Scale(2)
                            map.height += 100
                            page.add(add_home)
                            
            if page.route == f'/home/':
                        if page.width == 1024:
                            photo.height=590
                            header_photo.opacity = 1
                            darkening_photo.opacity = 1
                            city1_container.on_hover=hover
                            city2_container.on_hover=hover
                            city3_container.on_hover=hover
                            mobile()
                            header_photo.scale=ft.transform.Scale(2)
                            map.height += 200
                            page.add(add_home)
            if page.route == f'/authorization/':
                        if 1410 <= page.width <= 2544:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            big_window()
                            header_photo.scale=ft.transform.Scale(3)
                            page.add(add_auth)
            if page.route == f'/authorization/':
                        if 2545 <= page.width <= 6000:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            big_window()
                            header_photo.scale=ft.transform.Scale(4)
                            page.add(add_auth) 
                            
                        
            if page.route == f'/authorization/':
                        if 920 <= page.width <= 1300 and page.width != 1024:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_auth)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            pc()
                            
                        
                            
            if page.route == f'/authorization/':
                        if page.width == 820 and page.width == 768:
                            
                            darkening_photo.opacity = 0
                            darkening_photo.height += 300
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_auth)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            mobile()
                            
            if page.route == f'/authorization/':
                        if page.width <= 919:
                            darkening_photo.opacity = 0
                            darkening_photo.height += 300
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_auth)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            mobile()
            if page.route == f'/authorization/':
                        if page.width == 1024:
                            darkening_photo.opacity = 1
                            darkening_photo.scale=ft.transform.Scale(1)
                            darkening_photo.height = 500
                            darkening_photo.height += 100
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            photo.height=590
                            auth_cont.opacity = 0
                            auth_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_auth)
                            page.update()
                            time.sleep(0.1)
                            auth_cont.opacity = 1
                            auth_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            laptop()
                            page.update()
                    
            if page.route == f'/registration/':
                        if 1410 <= page.width <= 2544:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            pc()
                            header_photo.scale=ft.transform.Scale(3)
                            page.add(add_reg)
                            
            if page.route == f'/registration/':
                        if 2545 <= page.width <= 6000:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            pc()
                            header_photo.scale=ft.transform.Scale(4)
                            page.add(add_reg)
            if page.route == f'/registration/':
                        if 920 <= page.width <= 1300 and page.width != 1024:
                            cityes.height = 500
                            darkening_photo.opacity = 1
                            darkening_photo.height = 732.5
                            darkening_photo.scale=ft.transform.Scale(1)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_reg)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            pc()
            if page.route == f'/registration/':
                        if page.width <= 919:
                            darkening_photo.opacity = 0
                            darkening_photo.height = 300
                            darkening_photo.height += 1000
                            darkening_photo.scale=ft.transform.Scale(2)
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_reg)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            mobile()
                            
            if page.route == f'/registration/':
                        if page.width == 820 and page.width == 768:
                            darkening_photo.opacity = 0
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_reg)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            mobile()
            if page.route == f'/registration/':
                        if page.width == 1024:
                            darkening_photo.opacity = 1
                            darkening_photo.scale=ft.transform.Scale(1)
                            darkening_photo.height = 500
                            darkening_photo.height += 100
                            city1_container.on_hover=None
                            city2_container.on_hover=None
                            city3_container.on_hover=None
                            map.on_hover=None
                            photo.height=590
                            page.clean()
                            reg_cont.opacity = 0
                            reg_cont.scale=ft.transform.Scale(0.9)
                            page.add(add_reg)
                            page.update()
                            time.sleep(0.1)
                            reg_cont.opacity = 1
                            reg_cont.scale=ft.transform.Scale(1)
                            page.update()
                            time.sleep(1)
                            laptop()
            
            
                    
                
            
            page.update()

        def hover(event):
            if event.data == 'true':
                event.control.offset=ft.transform.Offset(0,-0.2)
                page.update()
            elif event.data == 'false':
                event.control.offset=ft.transform.Offset(0,0)
                page.update()
            page.update()
            
        def hover_our_num(event):
            if event.data == 'true':
                event.control.offset=ft.transform.Offset(0,0.020)
                page.update()
            elif event.data == 'false':
                event.control.offset=ft.transform.Offset(0,0.120)
                page.update()
            page.update()
        our_services.on_hover=hover
        our_number.on_hover=hover_our_num
        profile.on_hover=hover
        
        def menu_header_close(self):
            
            menu_header_close_part1_init()
            page.update()
            menu_header_close_part2_init()
            page.update()
            menu_header_close_part3_init()
            page.update()
            menu_header_close_part4_init()
            page.update()
            menu_header_close_part5_init()
            page.update()
            time.sleep(0.5)
            menu_button.on_click = menu_header_open
            page.update()
        
        def menu_header_open(self):
            menu_header_open_part1_init()
            page.update()
            menu_header_open_part2_init()
            page.update()
            menu_header_open_part3_init()
            page.update()
            menu_header_open_part4_init()
            page.update()
            menu_header_open_part5_init()
            page.update()
            time.sleep(0.5)
            menu_button.on_click = menu_header_close
            page.update()
            
            
            
        menu_button.on_click = menu_header_open
        profile.on_click = routing_to_auth      
        page.on_resize = page_adaptive
        logo_container.on_click = home_view
        sign_up.on_click = routing_to_reg
        back.on_click=back_to_auth
        sign_up2.on_click = registration_to_supabase
        sign_in.on_click = authorization_to_supabase
        profile_cont.on_hover=hover_profile
        map.opacity = 1
        map.offset=ft.transform.Offset(0,1)
        page_adaptive(None)
        page.update()
if __name__ == '__main__':
    ft.app(
        main,
        assets_dir='assets',
        view=ft.WEB_BROWSER,
        port=5252
    )
