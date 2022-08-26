
import pickle
sc = pickle.load(open('pickle/scaler.pk1', 'rb'))
model = pickle.load(open('pickle/model.pk1', 'rb'))
print("model ready")
