import os, re, sys

class clProcCorpus(object):
	'''
	reading corpus, extracting terms with PoS patterns
	'''

	def __init__(self, FileIN):
		self.DTerms = {}
		self.readCorpus(FileIN)


	def readCorpus(self, FileIN):
		LTerm = []
		for SLine in FileIN:
			LLine = re.split('\t', SLine)
			# sys.stderr.write(str(LLine) + '\n')

			try:
				SWord = LLine[0]
				SPoS = LLine[1]
				SLemma = LLine[2]
			except:
				SWord = ''
				SPoS = ''
				SLemma = ''

			if re.match('J.*', SPoS) or re.match('N.*', SPoS):
				LTerm.append(SWord)
			else:
				STerm = ' '.join(LTerm)
				LTerm = []
				try:
					self.DTerms[STerm] += 1
				except:
					self.DTerms[STerm] = 1

		return

	def printData(self):
		for STerm, Frq in sorted(self.DTerms.items(), key=lambda x: x[1], reverse=True):
			sys.stdout.write(STerm + '\t' + str(Frq) + '\n')




if __name__ == '__main__':
	FileIN = open(sys.argv[1], 'r')
	OProcCorpus = clProcCorpus(FileIN)
	OProcCorpus.printData()
