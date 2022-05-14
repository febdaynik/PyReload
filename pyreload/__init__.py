import logging
import os, sys, time
import hashlib

# logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class PyReload:
	def __init__(self, path = list()):
		if type(path) != list:
			self.path = [path]
		else:
			self.path = path

		self._ignore()
		
		self.timestamp = self.get_timestamp()
		self.hash_text = [{file:self.get_hash_text(path=file)} for file in self.path]
		logging.info("[+] Started PyReload")

	def _ignore(self):
		with open("._ignore", encoding="utf-8") as conf_ign: ign = conf_ign.readlines()
		[ self.path.remove(file.replace("\n","")) for file in ign ]

	def get_timestamp(self):
		try:
			return [{file:os.stat(file).st_mtime} for file in self.path]
		except FileNotFoundError as e: 
			logging.error(f"[-] Файл {e.filename} не был найден")
			self.path.remove(e.filename)


	def encode_md5(self, data):
		h = hashlib.md5(data)
		return h.hexdigest()

	def get_hash_text(self, path):
		try:
			with open(path, "rb") as file:
				return self.encode_md5(file.read())
		except FileNotFoundError as e: 
			logging.error(f"[-] Файл {path} не был найден")
			self.path.remove(e.filename)

	# Проверяет обновление файлов исходя из их содержания
	def update_file_hash(self):
		while True:
			for name,index in zip(self.path, range(len(self.path))): 
				text_hash = self.get_hash_text(path=name)
				# print(self.hash_text[index][name])
				if self.hash_text[index][name] != text_hash:
					self.hash_text[index][name] = text_hash
					logging.info("[Update] Файл был изменён!")
					self._reload_script_()

			# Задержка стоит для того, чтобы файл два раза не сохранялся (не знаю почему так работает)
			time.sleep(.1)

	# Проверяет обновление файлов исходя из времени обновления
	def update_file_timestamp(self):
		while True:
			for name,index in zip(self.path, range(len(self.path))):
				if self.timestamp[index][name] != os.stat(name).st_mtime:
					self.timestamp[index][name] = os.stat(name).st_mtime
					logging.info("[Update timestamp] Файл был изменён!")
					self._reload_script_()

	def _reload_script_(self):
		logging.info("[+] Reloading script")
		os.execl(sys.executable, sys.executable, *sys.argv)
