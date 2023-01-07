import binascii
import hashlib
import pymysql


print("=================================================")
print("=================================================")
print("----------------- Nice program ------------------")
print("=================================================")
print("=================================================")

#  user input
sklep_id = int(input('Pass shop id '))
while sklep_id < 1:
    input('Pass corect value, only numbers')

user_id = int(input('Pass computer id '))
while (user_id < 0 and user_id > 7):
    user_id = int(input('Pass computer id (betwen 1 and 6)'))

print('Using database to search for info')

# db side
try:
    conn = pymysql.connect(user="root", password="",
                           host="localhost", database="sklep")

except:
    print("Failed to get to database")
    input("Pres enter to try again")
    exit()

cursor = conn.cursor()

cursor.execute("SELECT * FROM sklep WHERE id=%s", (sklep_id,))
result = cursor.fetchone()
conn.close()

print(result)

# check if data is avaible 
if result is None:
    print("ID not found!")
    input("Press enter to exit and try again")
    exit()
else:


    router_ip = result[1]
    octets = router_ip.split(".")
    octets[3] = str(user_id+ 239)
    device_ip = ".".join(octets)

    formatted_shop_id = "{:04d}".format(sklep_id)
    # print(formatted_shop_id)


    # wps psk
    def wpa_psk(ssid, password):
        dk = hashlib.pbkdf2_hmac(
            'sha1',
            str.encode(password),
            str.encode(ssid),
            4096,
            256
        )
        return (binascii.hexlify(dk))

    wpa_psk_coded = (wpa_psk(formatted_shop_id, result[3])[0:64].decode('utf8'))
    # wpa_psk_coded = (wpa_psk(formatted_shop_id, "nuBz")[0:64].decode('utf8'))

    print('\n Text to copy\n')

    try:

        complete_data = f'''! U1 setvar "ip.dhcp.enable" "off"
        ! U1 setvar "wlan.ip.protocol" "permanent"
        ! U1 setvar "device.friendly_name" "ZEBRA_{formatted_shop_id}_{user_id}"
        ! U1 setvar "ip.addr" "{device_ip}"   
        ! U1 setvar "ip.netmask" "255.255.255.0"
        ! U1 setvar "ip.gateway" "{result[1]}"  
        ! U1 setvar "wlan.essid" "{formatted_shop_id}_t"   
        ! U1 setvar "wlan.leap_mode" "off"
        ! U1 setvar "wlan.kerberos.mode" "off"
        ! U1 setvar "wlan.encryption_mode" "off"
        ! U1 setvar "wlan.8021x.enable" "off"
        ! U1 setvar "wlan.operating_mode" "infrastructure"
        ! U1 setvar "wlan.user_channel_list" "36,38,40,42,44,46,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140"
        ! U1 setvar "wlan.country_code" "europe"
        ! U1 setvar "wlan.allowed_band" "5"
        ! U1 setvar "wlan.international_mode" "off"
        ! U1 setvar "wlan.wpa.authentication" "psk"
        ! U1 setvar "wlan.wpa.enable" "on"
        ! U1 setvar "wlan.wpa.psk" "{wpa_psk_coded}"   
        ! U1 do "device.reset" ""\n'''

        print(complete_data)

    except:
        print("Error while asembling output string")
    input("Press enter to exit")


    #  Dorobić żeby wiedziało jak user udczyta nieistniejący rekord