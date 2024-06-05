from supabase import create_client
from reg_and_auth_container import sign_up,back,sign_up2,entry_pass_reg,desc_pass_reg,desc_pass_auth,auth_cont,reg_cont,sign_in,entry_pass_auth,entry_first_name_reg,entry_last_name_reg,entry_login_auth,entry_login_reg,entry_phone_num_reg
import uuid

url = 'https://crohfqrvihedoxvksmpc.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNyb2hmcXJ2aWhlZG94dmtzbXBjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTczNTAxOTAsImV4cCI6MjAzMjkyNjE5MH0.k_-el1npvcpfgdRjOFkpDoZg7rheMbDD03miChH966g'
user_id = str(uuid.uuid4())
supabase = create_client(url, key)

def add_account_to_base():

    fields = [
        entry_first_name_reg.value, 
        entry_last_name_reg.value, 
        entry_phone_num_reg.value, 
        entry_login_reg.value, 
        entry_pass_reg.value,
        user_id,
    ]

    if all(field != '' for field in fields):
        add_user = supabase.table('users').insert({
            'firstname':entry_first_name_reg.value,
            'lastname':entry_last_name_reg.value,
            'login': entry_login_reg.value,
            'password': entry_pass_reg.value,
            'phonenumber':entry_phone_num_reg.value,
            'id':user_id,
        
        }).execute()
    else:
        pass
    
