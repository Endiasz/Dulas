import mysql.connector


# DB side of program

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()

id = 1111

query = f"SELECT * FROM your_table WHERE id = {id}"

cursor.execute(query)

sklep = cursor.fetchone()
cursor.close()
db.close()

# Print the result
print(sklep)






# sklepy_id = [{'id':'1111','ip':'192.168.12.221'},{'id':'1112','ip':'192.168.12.333'}]

# def get_Shop(id):
#     for sklep in sklepy_id:
#         if(sklep['id']==str(id)):
#             # pass everything from db TO DO
#             return sklep

#     # Only if not found
#     return 'NOT FOUND'

# wybrany_Sklep = {'id':'','ip':''}

# wybrany_Sklep = get_Shop(1112)
# print(wybrany_Sklep)









# # Split the router IP into its octets
# octets = router_ip.split(".")

# # Set the last octet equal to the number of the device
# octets[3] = str(device_number)

# # Join the octets back together to create the new IP address
# device_ip = ".".join(octets)

# # Print the new IP address
# print(device_ip)