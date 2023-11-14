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
        return [value for value in self.client.smembers(key)]
    
    # drop elements
    def drop_elements(self, key, member):
        if self.client.sismember(key, member):
            res = self.client.srem(key, member)
            if res > 0:
                print('Element successfully removed')
        else:
            print(f"Member not in key: {key}")

    # add elements
    def add_elements(self, key, member):
        if self.client.sismember(key, member):
            print(f"Member existed: {member} in key {key}")
        else:
            self.client.sadd(key, member)
            print(f"Member added: {member} to key {key}")

def check_redis_connection():
    redis_connection('6379', 1, 'localhost')

if __name__ == "__main__":
    r = redis_connection('6379', 1, 'localhost')
    # print(r.get_elements('nset'))
    # r.drop_elements('nset', 9)
    # print(r.get_elements('nset'))
    # r.drop_elements('nset', 1)
    print(r.get_elements('nset'))
    # r.add_elements('nset', 3)
    # print(r.get_elements('nset'))
    # r.add_elements('nset', 1)
    # print(r.get_elements('nset'))


