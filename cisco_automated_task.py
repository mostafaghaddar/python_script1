from netmiko import Netmiko

router1 = Netmiko(ip='192.168.99.136',
                 username='cisco',
                 password='cisco@123',
                 device_type='cisco_ios')
router2 = Netmiko(ip='192.168.99.138',
                 username='cisco',
                 password='cisco@1234',
                 device_type='cisco_ios')
router3 = Netmiko(ip='192.168.99.139',
                 username='cisco',
                 password='cisco@12345',
                 device_type='cisco_ios')

print(router1.find_prompt())
print(router2.find_prompt())
print(router3.find_prompt())

show_ip_details_R1 = router1.send_command("show ip interface brief")
show_ip_details_R2 = router2.send_command("show ip interface brief")
show_ip_details_R3 = router3.send_command("show ip interface brief")

print(show_ip_details_R1)
print(show_ip_details_R2)
print(show_ip_details_R3)












