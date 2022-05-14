PyReload
=====

Библиотека для быстрого взаимодействия с кодом в файле.
PyReload - позволяет обновлять код в реальном времени

Examples
====

## For aiogram

```python
# update code in framework aiogram

import os
from pyreload import PyReload
async def on_startup(x):
	PyReload(os.listdir()).update_file_hash()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   
```
