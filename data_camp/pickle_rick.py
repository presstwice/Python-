import pickle

cucumber = "It's Unpickled Rick!"

pickle.dump(cucumber, open("suprise.p", "wb"))

gerkin = pickle.load(open("surpise.p", "rb"))

print(gerkin)