import re #to 
import ctypes

# Class created to calculate the IPv4


class IPv4Calculator:
    def __init__(self, ip='', cidr=0, mask='', network='', broadcast='', number_ips=0):
        #Constructor of the Calculator class, to initialize and validate all the attributes of the class
        self.ip = ip
        self.cidr = cidr
        self.mask = mask
        self.network = network
        self.broadcast = broadcast
        self.number_ips = number_ips

        #verifying if the IP address and CIDR number is valid
        if self.ip == '' and not self.is_valid_ip():
            raise ValueError("Not a valid IP address.")
        if not self.is_cidr_valid():
            raise ValueError("Not a valid CIDR.")


    def calculate(self):
        #method made justo to encapsulate the methods of the class
        self.cidr_to_binary_mask()
        self.binary_mask_to_decimal()
        self.get_network_broadcast_addr()
        self.get_number_ips()


    def is_valid_ip(self) -> bool:
        #method to verify if the IP address is like "000.000.000.000"
        ip_exemple = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$') #string like "000.000.000.000"

        if ip_exemple.search(self.ip): #search for a sting like above
            return True
        return False


    def is_cidr_valid(self) -> bool:
        #method to verify if the CIDR is between 0 and 32
        if 0 <= self.cidr <= 32:
            return True
        return False


    def cidr_to_binary_mask(self):
        #method to create the netmask from the CIDR number
        for i in range(32):
            if i == 8 or i == 16 or i == 24: #make the mask like "000.000.000.000"
                self.mask += '.'
            if i < self.cidr:
                self.mask += '1'
            else:
                self.mask += '0'
        

    def binary_mask_to_decimal(self):
        #method to convert the binary mask to a integer mask
        decimal = []
        for aux in self.mask.split('.'):
            decimal.append(str(int(aux, 2))) #convert the binary to integer, to string and put on the list
        
        self.mask = '.'.join(decimal) #make the mask like "000.000.000.000"
    

    def get_network_broadcast_addr(self):
        #method to find the network and broadcast IP address
        network = []
        broadcast = []
        for m, i in zip(self.mask.split('.'), self.ip.split('.')): #split both mask and ip address by '.'
            int_i, int_m = int(i), int(m) #convert the strings to integers
            network.append( str( int_i & int_m ) ) #make the bitwise operation i AND m; convert back to string
            broadcast.append( str( int_i | ctypes.c_uint8(~int_m).value ) ) #convert the int_m to unsigned int8, make the bitwise operation i AND NOT m, convert back to string

        self.network = '.'.join(network) #make the network like "000.000.000.000"
        self.broadcast = '.'.join(broadcast) #make the broadcast like "000.000.000.000"
    

    def get_number_ips(self):
        #method to get the nuber of IP in the CIDR
        n = 32 - self.cidr
        self.number_ips = 2**n


    def __str__(self):
        #method to return the string form of the class
        return f"IP: {self.ip};\n" \
               f"Mask: {self.mask};\n" \
               f"Network: {self.network};\n" \
               f"Broadcast: {self.broadcast};\n" \
               f"Number IPs: {self.number_ips} (2 for network and broadcast, and {self.number_ips-2} for hosts)"