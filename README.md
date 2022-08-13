# uart-base-on-python
This is a application which receive and send data using uart

install pyserial library before using the program

def port_available() is to find available port number

def send(data_s,port_num,baudrate) is to send data via uart
data_s: can be any data type (tested: int float str)
port_number: port_number in str type ( eg: 'COM2')
baudrate: baudrate in int type (eg:132500)

def receive(port_num,baudrate) is a infinite loop which receive data from uart
port_number: port_number in str type ( eg: 'COM2')
baudrate: baudrate in int type (eg:132500)
.inWaiting(): a flag which indicates #bytes are in buffer needed to collect
.readall(): read all data from buffer
.read(a = #): read # bytes data from buffer
