import logging
import os, sys, time
import hashlib, traceback

logging.getLogger('pyreload').setLevel(logging.DEBUG)

class PyreloadPermissionError(PermissionError):
	pass

class PyReload(object):
	def __init__(self, ignore_file: str = "._ignore", path: list() = [os.path.basename(__file__)]):
		if type(path) != list:
			self.path = [path]
		else:
			self.path = path

		self.ignore_file = ignore_file
		self._ignore(self.ignore_file)

		self.timestamp = self.get_timestamp()
		self.hash_text = [{file:self.get_hash_text(path=file)} for file in self.path]

	def _ignore(self, ignore_file):
		try:
			with open(ignore_file, encoding="utf-8") as conf_ign: ign = conf_ign.readlines()
		except FileNotFoundError:
			with open(ignore_file, 'a+', encoding="utf-8") as conf_ign: ign = conf_ign.readlines()

		for file in ign:
			try:
				self.path.remove(file.replace("\n",""))
			except FileNotFoundError: pass
			except ValueError: pass

	def encode_md5(self, data):
		h = hashlib.md5(data)
		return h.hexdigest()

	def get_hash_text(self, path):
		try:
			with open(path, "rb") as file:
				return self.encode_md5(file.read())
		except PermissionError as e:
			raise PyreloadPermissionError('%s. Add this file to %s, then the error will disappear.' % (e, self.ignore_file)) 
		except FileNotFoundError as e:
			logging.error(f"Файл {path} не был найден")
			self.path.remove(e.filename)

	def get_timestamp(self):
		try:
			return [{file:os.stat(file).st_mtime} for file in self.path]
		except FileNotFoundError as e: 
			print(os.path.basename(__file__))
			print("ERROR:",traceback.format_exc())
			logging.error(f"Файл {e.filename} не был найден")
			self.path.remove(e.filename)
	
	@property
	def update_file(self):
		return UpdateFile(self)

	def _reload_script_(self):
		logging.info("[+] Reloading script")
		os.execl(sys.executable, sys.executable, *sys.argv)



class UpdateFile(object):
	def __init__(self, pr: PyReload = None):
		self.pr = pr
		self.func = None

	# Проверяет обновление файлов исходя из их содержания
	def hash(self):
		self.func = "hash"
		for name,index in zip(self.pr.path, range(len(self.pr.path))): 
			text_hash = self.pr.get_hash_text(path=name)
			if self.pr.hash_text[index][name] != text_hash:
				self.pr.hash_text[index][name] = text_hash
				logging.info("[Update] Файл был изменён!")
				self.pr._reload_script_()

		return self

	# Проверяет обновление файлов исходя из времени обновления
	def timestamp(self):
		self.func = "timestamp"
		for name,index in zip(self.pr.path, range(len(self.pr.path))):
			if self.pr.timestamp[index][name] != os.stat(name).st_mtime:
				self.pr.timestamp[index][name] = os.stat(name).st_mtime
				logging.info("[Update timestamp] Файл был изменён!")
				self.pr._reload_script_()
		return self

	def run(self):
		try: eval("self.%s()" % self.func)
		except KeyboardInterrupt: logging.info("[-] Stopped PyReload")

	async def async_run(self):
		try: eval("self.%s()" % self.func)
		except KeyboardInterrupt: logging.info("[-] Stopped PyReload")
