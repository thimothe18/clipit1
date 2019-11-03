
class cheval:

	def test(self):
		self.poney = 'poney'

	def test1(self):
		self.cheval = 'cheval'

	def tout(self):
		p.test()
		p.test1()
		print(self.cheval)
		print(self.poney)

p = cheval()
p.tout()