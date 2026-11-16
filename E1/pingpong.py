def ping(n):
    if n == 0: return
    print("ping",end=" ")
    pong(n-1)


def pong(n):
    if n == 0: return 
    print("pong",end=" ")
    ping(n-1)

print(ping(5))