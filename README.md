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
async def _reload():
	pr.update_file.hash().run()

def repeat(coro, loop):
	asyncio.ensure_future(coro(), loop=loop)
	loop.call_later(1, repeat, coro, loop)

if __name__ == '__main__':
	pr = PyReload(path=os.listdir())
	executor.start_polling(dp, skip_updates=True, loop=loop)   
```
