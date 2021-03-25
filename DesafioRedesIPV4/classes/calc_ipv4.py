import re


class CalcIPV4:
    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        self._set_broadcast()
        self._set_rede()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @ip.setter
    def ip(self, value):
        if not self._valida_ip(value):
            raise ValueError('IP Inválido')

        self._ip = value
        self._ip_bin = self._ip_binario(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._valida_ip(value):
            raise ValueError('Máscara Inválida')

        self._mask = value
        self._mask_bin = self._ip_binario(value)

        if not hasattr(self, 'prefix'):
            self.prefix = self._mask_bin.count('1')

    @prefix.setter
    def prefix(self, value):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError('Prefixo precisa ser um valor inteiro')

        if value > 32:
            raise TypeError('Valor precisa ter 32 bits')

        self._prefix = value
        self._mask_bin = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self._binario_ip(self._mask_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'  # validando o ip ou máscara
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_binario(ip):  # converte ip ou mascara para binário
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_bin)

    @staticmethod
    def _binario_ip(ip):  # converte binário para ip ou mascara
        n = 8
        blocos = [str(int(ip[i: i + n], 2)) for i in range(0, 32, n)]  # dividindo o ip binario em blocos de 8
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[:self.prefix] + (host_bits) * '1'
        self._broadcast = self._binario_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefix
        self._rede_bin = self._ip_bin[:self.prefix] + (host_bits) * '0'
        self._rede = self._binario_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefix)
