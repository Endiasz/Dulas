import tkinter as tk
import binascii
import hashlib
import csv


# Create the main window
window = tk.Tk()
window.title("Configurator")
window.geometry("300x200")


# Create the input fields
id_sklep_label = tk.Label(window, text="ID Sklepu:")
id_sklep = tk.Spinbox(window)
id_dev_label = tk.Label(window, text="ID drukarki:")
id_dev = tk.Spinbox(window, from_=1, to=6)

# Create the output label
output_label = tk.Label(window, text="")

# Create a function to compute the output


def get_values():
    # Get the values from the input fields
    sklep_id = str(id_sklep.get())
    user_id = str(id_dev.get())
    formatted_shop_id = "{:04d}".format(int(sklep_id))
    # formatted_shop_id+='_t'

    # Convert the input to numbers (if possible)
    result = None
    try:
        # Open the CSV file
        with open('data.csv', 'r') as csv_file:
          # Create a CSV reader object
          reader = csv.reader(csv_file)
        #   row_number = sklep_id
          # Loop through the rows
          for row in reader:
            if(row[0]==formatted_shop_id):
                result = row
                print(result)
                break
    except:
        output_label.config(text="Nie otwieranie pliku, sprawdź nazwę pliku, plik powinien nazywać się data.csv")
        exit()

    if result == None:
        output_label.config(text="Nie ma takiego id")
    else:

        router_ip = result[1]
        octets = router_ip.split(".")
        octets[3] = str(int(user_id) + 239)
        device_ip = ".".join(octets)


        # wps psk
        string_bytes = result[3].encode()
        salt_bytes = (formatted_shop_id+'_t').encode()

        hashed_string = hashlib.pbkdf2_hmac("sha1", string_bytes, salt_bytes, 4096,64)

        wpa_psk_coded_128 = hashed_string.hex()
        # length = len(string)
        wpa_psk_coded = wpa_psk_coded_128[:len(wpa_psk_coded_128) // 2]
        try:

            complete_data = f'''
! U1 setvar "ip.dhcp.enable" "off"
! U1 setvar "wlan.ip.protocol" "permanent"
! U1 setvar "device.friendly_name" "ZEBRA_{formatted_shop_id}_0{user_id}"
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
! U1 setvar "wlan.wpa.psk" "{wpa_psk_coded.upper()}"   
! U1 do "device.reset" ""\n'''

            output_window = tk.Toplevel(window)
            output_window.title("Do skopiowania")
            output_window.geometry("1000x500")

    # Create a label to display the output in the new window
            output_text = tk.Text(output_window,  height=1000, width=500)
            output_text.pack()
            output_text.insert(tk.END, complete_data)

        except:
            output_label.config(text="Error przy tworzeniu tekstu")
            input("Kliknij enter aby kontynuowac")

# Create a button to trigger the computation
get_output = tk.Button(window, text="Compute", command=get_values)

# Place the input fields and button in the window
id_sklep_label.pack()
id_sklep.pack()
id_dev_label.pack()
id_dev.pack()

get_output.pack()
output_label.pack()

# Run the main loop
window.mainloop()
