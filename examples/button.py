class Controller:
    def __init__(self, com, baud):
        try:
            import serial
            self.__ser = serial.Serial(com, baud)
            self.__found = True
        except:
            print('No controller found. Or pyserial is not installed')
            self.__found = False
            
        self.Button = 0
        
        self.X = 0
        self.Y = 0
        
    def __decode(self, data):
        decoded_str = data.decode('utf-8').strip()
        decoded_str = decoded_str.rstrip()
        return decoded_str
        
    def Get_Data(self):
        if self.__found:
            try:
                read = self.__decode(self.__ser.readline(1000))
                data = read.split(',')
                
                self.Button = int(data[2])
                
                self.X = data[0]
                self.Y = data[1]
            except:
                self.Button = 0
                self.X = 0
                self.Y = 0
                
    def Set_Text(self, text):
        if self.__found:
            self.__ser.write(str(text).encode())
            
    def Close_Port(self):
        self.__ser.close()
        self.__found = False


#Connect to the controller.
controller = Controller('COM4', 115200)

#Show a title on the Micro:Bit.
controller.Set_Text('Button Example')

while True:
    #Get data from the Micro:Bit
    controller.Get_Data()
    
    #Check wich button is pressed.
    match controller.Button:
        case 1:
            print('Button A is pressed.')
        case 2:
            print('Button B is pressed.')
        case 3:
            print('Button C is pressed.')
        case 4:
            print('Button D is pressed.')
        case 5:
            print('Button F is pressed.')
        case 6:
            print('Button E is pressed.')
            
        case 0:
            print('No button is pressed.')
