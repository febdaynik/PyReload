PyReload
=====

Библиотека для быстрого взаимодействия с кодом в файле.
PyReload - позволяет обновлять код в реальном времени

Конфигурация
====

Чтобы не следить за всеми файлами их можно поместить в файл игнорирования, по стандарту он '._ingore'. Для этого вам понадобиться:
```
1. Создать файл игнорирования
2. Добавить игнорируемые файлы
3. Запустить скрипт (если файл называется иначе, то передайте его название через параметр 'ignore_file')

ps: Создание файл не является обязательным
```

Примеры
====

## Для aiogram

```python
# update code in framework aiogram

import os
from pyreload import PyReload
async def repeated_task():
	while 1:
		await pr.update_file.hash().async_run()
		await asyncio.sleep(1)

async def on_startup(_):
	logging.info("Bot started")


	logging.info("Started waiting reload")
	asyncio.create_task(repeated_task())

if __name__ == '__main__':
	pr = PyReload(path=os.listdir())
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   
```
