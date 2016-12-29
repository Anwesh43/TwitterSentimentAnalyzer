class DataExtractor:
    def __init__(self,txtFile):
        self.txtFile = txtFile
    def parseTextFile(self):
        with open(self.txtFile) as f:
            textMessages = f.read()
            msgs = []
            outputs = []
            for textMessage in textMessages.split('\n'):
                if(not(textMessage.strip() == '')):
                    words = textMessage.split('\t')
                    outputs.append(words[0])
                    msgs.append(words[1].replace('.','').replace(',',''))
        return (msgs,outputs)
