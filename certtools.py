import sublime
import sublime_plugin
import subprocess


class ParseCertificateCommand(sublime_plugin.TextCommand):

	supported_extensions = (".crt", ".pem")

	def is_visible(self):
		filename = self.view.file_name()
		return filename.endswith(self.supported_extensions)


	def run(self, edit):
		filename = self.view.file_name()
		print("Will parse certificate for {}".format(filename));
		cert_result = "Error deconding the certificate: {}"
		try:
			cert_result = subprocess.check_output(["openssl", "x509", "-text", "-noout", "-in", filename]).decode('utf-8')
		except Exception as e:
			cert_result = cert_result.format(e)	

		new_buffer = sublime.active_window().new_file()
		new_buffer.insert(edit, 0, cert_result)
