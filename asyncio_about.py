import asyncio

import aiohttp

# EXPR must have .__aexit__ and .__aenter__
EXPR = aiohttp.request('POST', 'http://127.0.0.1')
BLOCK = 2





async def new_syntax():
    async with EXPR as VAR:
        BLOCK
        foo = VAR

    return str(foo)






if __name__ == '__main__':
    # async requires 2 things:
    # 1: async wait : function that can suspend and resume



    # 2: loop is scheduler: knows what tasks are running, selects task to be run next.
    loop = asyncio.get_event_loop()

    loop.run_until_complete(new_syntax())
    loop.close()



# MUST HAVE



'''
when web.app gets a request,
server needs to react.
this is called 'event handling'
server will call one or more ;eventhandlers'
once those event handlers are done,
they need to give control back to the event loop
here 'asyncio' uses 'coroutines'
'courutine' = special function tht can give up control to its caller without loosing its state.
'''


