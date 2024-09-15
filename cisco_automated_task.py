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
show_ip_details_R1 = router1.send_command ['enable',
'configure terminal',
'interface loopback 0',
'ip address 172.16.16.1 255.255.255.255'
                                            ]










