UDebug
=====

Библиотека для быстрого взаимодействия с кодом в файле.
UDebug - позволяет обновлять код в реальном времени

Examples
====

## For aiogram

```python
	# update code in framework aiogram

	from udebug import UDebug
    async def on_startup(x):
		UDebug(os.listdir()).update_file_hash()

	if __name__ == '__main__':
		executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   
```
