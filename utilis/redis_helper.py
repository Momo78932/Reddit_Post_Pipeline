import redis

# used to interact with local redis client
class redis_connection:
    def __init__(self, port, dbNum, host):
        self.port = port
        self.databaseNumber = dbNum
        self.host = host
        try:
            self.client = redis.Redis(host = self.host, port = self.port,decode_responses=True, db =self.databaseNumber )
            self.client.ping()
        except Exception as e:
            print(f"Error connecting to Redis database at host: {self.host}, port: {self.port}, dbNumber: {self.databaseNumber} \n ")
            print(e)
        print("Successfully connected")
    
    # get elements
    def get_elements(self, key):
        '''
        get_elements(self, key): return list of all items in key
        get_elements: str -> (listof Any)
        '''
        return [value for value in self.client.smembers(key)]
    
    # drop elements
    def drop_elements(self, key, member):
        '''
        drop_elements(self, key, member): delete member from key
        drop_elements: str, Any -> None
        '''
        if self.client.sismember(key, member):
            res = self.client.srem(key, member)
            if res > 0:
                print('Element successfully removed')
        else:
            print(f"Member not in key: {key}")

    # add elements
    def add_elements(self, key, member):
        '''
        add_elements(self, key, member): add member to key
        add_elements: str Any -> None
        '''
        if self.client.sismember(key, member):
            print(f"Member existed: {member} in key {key}")
        else:
            self.client.sadd(key, member)
            print(f"Member added: {member} to key {key}")

def check_redis_connection():
    '''
    check_redis_connection(): for airflow run to check redis connection
    '''
    redis_connection('6379', 1, 'localhost')