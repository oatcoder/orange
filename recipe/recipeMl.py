import tensorflow as tf

from tensorflow import keras


class RecipeML:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    def test(self):
        # tensorflow poc
        hello = tf.constant('Hello, TensorFlow!')
        sess = tf.Session()
        
        print(sess.run(hello))