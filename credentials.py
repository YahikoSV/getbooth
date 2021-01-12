class Credentials:
    def __init__ (self, filename):
        self.filename = filename
        self._username = None
        self._password = None
        self._web_type = None
        self._web_path = None
        self._latency  = None
        self._merch_URL= None
        self._pre_buy  = None
        self.get_credentials (filename)

    def read_file (self) -> list:
        try:
            with open(self.filename, 'r') as input_file:
                data = input_file.readlines ()
        except:
            print ("file not found")
            exit ()
        return data

    def get_credentials (self, filename: str):
        file_data = self.read_file ()
        file_data = [data.rsplit("=")[1].split("\n")[0] for data in file_data]
        self._username = file_data[0]
        self._password = file_data[1]
        self._web_type = file_data[2]
        self._web_path = file_data[3]
        self._merch_URL= file_data[4]
        self._pre_buy  = file_data[5]
        self._latency  = file_data[6]
        
    @property
    def username (self) -> str:
        return self._username

    @property
    def password (self) -> str:
        return self._password

    @property
    def web_type (self) -> str:
        return self._web_type

    @property
    def web_path (self) -> str:
        return self._web_path
    
    @property
    def merch_URL (self) -> str:
        return self._merch_URL
    
    @property
    def pre_purchase (self) -> bool:
        return self._pre_buy
    
    @property
    def latency (self) -> float:
        return self._latency

