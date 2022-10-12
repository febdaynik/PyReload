PyReload
=====

Library for quick interaction with the code in the file.
PyReload - allows you to update the code in real time

`pip install python-reload`

Configuration
====

In order not to keep track of all the files, they can be placed in the ignore file, according to the standard it is '._ingore'. To do this, you will need:
```
1. Create a ignore file
2. Add ignored files
3. Run the script (if the file is called differently, then pass its name through the 'ignore_file' parameter)

ps: Creating a file is optional
```
```python
# Example ignore file
pr = PyReload(ignore_file = 'custom_name_ignore_file.txt')
```

Examples
====

## pyreload + aiogram

```python
# update code in framework aiogram
import os
from pyreload import PyReload

...

async def pyreload_task():
	while 1:
		await pr.update_file.hash().async_run()
		await asyncio.sleep(1)

async def on_startup(_):
	logging.info("Bot started")

	logging.info("Started waiting reload")
	asyncio.create_task(pyreload_task())

if __name__ == '__main__':
	pr = PyReload(path=os.listdir())
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   
```

## pyreload + vkbottle

```python
# update code in framework aiogram
import os
from pyreload import PyReload

...

@bot.loop_wrapper.interval(seconds=1)
async def pyreload_task():
	await pr.update_file.hash().async_run()

if __name__ == '__main__':
	pr = PyReload(path = os.listdir())
	bot.run_forever()
```