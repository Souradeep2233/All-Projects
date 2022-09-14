import operator
import pyaudio
import speech_recognition as sr
listener = sr.Recognizer()
my_mic_device = sr.Microphone(device_index=1)
with my_mic_device as source:
    listener.adjust_for_ambient_noise(source)
    audio = listener.listen(source)
my_string=listener.recognize_google(audio)
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,#multiplied bolle o data set e emni x boshay from google
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

print(eval_binary_expr(*(my_string.split())))


