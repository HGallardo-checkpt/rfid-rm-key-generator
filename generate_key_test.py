from key import KeyEngine



keyEngineGenerator = KeyEngine("3e4acc4f5a9b4ada" ,  1690754602)
jwt = keyEngineGenerator.create()


#print(jwt)
print("-----------------------")
data = keyEngineGenerator.decoder(jwt)
print(data)
