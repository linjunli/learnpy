def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCTER]Producting %s...' % n)
        r = c.send(n)
        print('[PRODUCTER]Consuming return: %s' % r)
    c.close()

c = consumer()
produce(c)

# asyncio
import asyncio
async def hello():
    print('Hello coroutine!')
    # 异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print('again!')
# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()