valid_alpha_user = "abcdefghijklmnoperstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."

while True:
    user = input("ingrese el nombre de usuario:")
    if(len(user)>4):
        a=set(valid_alpha_user)
        b=set(user)
        if len(b-a)>0:
            print("Usuario invalido.")
            continue
        else:
            print("Usuario valido.")
            break
    else:
        print("Usuario invalido")
