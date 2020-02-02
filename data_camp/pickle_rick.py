import pickle

cucumber = "It's Unpickled Rick!"

pickle.dump(cucumber, open("save.p", "wb"))

gerkin = pickle.load( open("save.p", "rb"))

print(gerkin)