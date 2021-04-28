import redis

redis_host = 'localhost'
redis_port = 6379  # local port is 6379


def redis_string():
    try:

       # Connection string (connection parameters )

        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)  # Takes difference parameters to persist data in apps

       # What does Decode do? ---> Helps in reading data since python cannot directly read redis

        r.set("message", "Hello World!")

        # get function would help in getting the message from redis

        msg = r.get("message")
        print(msg)

    except Exception as e:
        print(e)


def redis_integer():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        r.set("number", "100")
        o_number = r.get("number")
        r.incr("number")
        incr_number = r.get("number")
        print(o_number)
        print(incr_number)

    except:
        print("Something went wrong")


if __name__ == "__main__":
    redis_string()
    redis_integer()
