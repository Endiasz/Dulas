import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sklep"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Define the ID you want to get data for
id = 1

# Construct the query to get data for the specified ID
query = f"SELECT * FROM sklep WHERE id = {id}"

# Execute the query
cursor.execute(query)

# Fetch the result of the query
result = cursor.fetchone()

# Print the result
print(result)

# Close the cursor and the database connection
cursor.close()
db.close()


f'''! U1 setvar "ip.dhcp.enable" "off"
    ! U1 setvar "wlan.ip.protocol" "permanent"
    ! U1 setvar "device.friendly_name" "ZEBRA_{}_{}"
    ! U1 setvar "ip.addr" "10.10.104.240"   
    ! U1 setvar "ip.netmask" "255.255.255.0"
    ! U1 setvar "ip.gateway" "10.10.104.1"  
    ! U1 setvar "wlan.essid" "0337_t"   
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
    ! U1 setvar "wlan.wpa.psk" "46450B75F7C3B07CF89D46EAEF9571B7AB7CAB0A81D959DCD071D53C68963D80"   
    ! U1 do "device.reset" ""'''
