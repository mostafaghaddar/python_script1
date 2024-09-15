from netmiko import ConnectHandler

router1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.99.136',
    'username': 'cisco',
    'password': 'cisco@123'
}
router2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.99.138',
    'username': 'cisco',
    'password': 'cisco@1234'
}
router3 = {
    'device_type': 'cisco_ios',
    'host': '192.168.99.139',
    'username': 'cisco',
    'password': 'cisco@12345'
}
net_connect = ConnectHandler(**router1)
net_connect1 = ConnectHandler(**router2)
net_connect2 = ConnectHandler(**router3)

net_connect.enable()
net_connect1.enable()
net_connect2.enable()

config_commands = ['enable',
                   'configure terminal',
    'interface Loopback0',
    'ip address 172.16.16.1 255.255.255.255'
]
config_commands1 = ['enable',
                   'configure terminal',
    'interface Loopback0',
    'ip address 172.16.17.1 255.255.255.255'
]
config_commands2 = ['enable',
                   'configure terminal',
    'interface Loopback0',
    'ip address 172.16.18.1 255.255.255.255'
]
net_connect.send_config_set(config_commands)
net_connect1.send_config_set(config_commands1)
net_connect2.send_config_set(config_commands2)
net_connect.send_command('write memory')
net_connect1.send_command('write memory')
net_connect2.send_command('write memory')







