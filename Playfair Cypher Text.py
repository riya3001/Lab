#Converting plaintext into diagraphs 
def convertPlainTextToDiagraphs (plainText):
    
        # append X if Two letters are being repeated
    for s in range(0,len(plainText)+1,2):
        if s<len(plainText)-1:
            if plainText[s]==plainText[s+1]:
                plainText=plainText[:s+1]+'X'+plainText[s+1:]

    