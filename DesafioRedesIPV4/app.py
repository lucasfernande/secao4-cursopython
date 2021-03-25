from classes.calc_ipv4 import CalcIPV4

calcIPV4 = CalcIPV4(ip='192.168.0.1', mask='255.255.255.192')

print(f'IP: {calcIPV4.ip}')
print(f'Máscara: {calcIPV4.mask}')
print(f'Rede: {calcIPV4.rede}')
print(f'Broadcast: {calcIPV4.broadcast}')
print(f'Prefixo: {calcIPV4.prefix}')
print(f'Número de ips: {calcIPV4.numero_ips}(Total) / {calcIPV4.numero_ips - 2}(Disponíveis)')
