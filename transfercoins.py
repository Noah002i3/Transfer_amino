import aminofix as amino, threading, json
import colorama, pyfiglet

print(colorama.Fore.GREEN)
print(pyfiglet.figlet_format("Transfer", font="slant"))
print("      [Creditos] [Noah] ")

client = amino.Client()

vip = input("\n - Usuario con el vip: ")
url = client.get_from_code(vip)
userId = url.objectId
comId = url.path[1:url.path.index('/')]

def transfer():
    print("""\nTipo de login:
1.Email
2.Sid""")
    metodo = input(" - Opción: ")
    if metodo == "1":
        client.login(email=input(" - Email: "), password=input(" - Contraseña: "))
    elif metodo == "2":
        client.login_sid(SID=input(" - Sid:"))
    print("""\nUnirse a la comunidad:
          1.Si
          2.No""")
    unirse = input(" - Opcion: ")
    if unirse == "1":
        client.join_community(comId=comId)
        print(" - Me he unido a la comunidad")
    elif unirse == "2":
        print(" - Opcion saltada")
    sub_client=amino.SubClient(comId=comId, profile=client.profile)
    tuscoins = client.get_wallet_info().totalCoins
    print(f" - Cuentas con {tuscoins} para enviar")
    coins = int(input(" - Cantidad a enviar: "))
    coinsdiv = coins // 500
    for i in range(coinsdiv):
        threading.Thread(target=sub_client.subscribe, args=(userId, )).start()
        print(" - Enviando coins")
    print(f"Se han enviado {coins}")
    
def transfercuentas():
    with open('account.json', 'r') as f:
        account_data = json.load(f)
        for account in account_data:
            client.login(email=account["email"], password= account["password"])
            eu = account["email"]
            print(f" - Dentro de {eu}")
            sub_client=amino.SubClient(comId=comId, profile=client.profile)
            tuscoins = client.get_wallet_info().totalCoins
            print(f" - Cuentas con {tuscoins} para enviar")
            coins = int(input(" - Cantidad a enviar: "))
            coinsdiv = coins // 500
            for i in range(coinsdiv):
                threading.Thread(target=sub_client.subscribe, args=(userId, )).start()
                print(" - Enviando coins")
            print(f"Se han enviado {coins}")
            
print("""\nMetodo de envio:
1.Inicio de sesion desde tu cuenta
2.Inicio de sesion usando un accounts.json
                    """)
metodoenvio = input(" - Opción:")

if metodoenvio == "1":
    transfer()
elif metodoenvio == "2":
    transfercuentas()

        
            
            
        
        
    
    

