#!/usr/bin/env python3

class MyString:
    def __init__(self, initial_value=""):
      self._value = None
      self.value = initial_value

    def get_value(self):
      print("retrieving the value")
      return self._value
    
    def set_value(self, new_value):
       if isinstance(new_value, str):
          self._value = new_value

       else:  
          print('The value must be a string.')

    value = property(get_value, set_value)  

    def is_sentence(self):
       if self._value and isinstance(self._value, str):
            return self._value.endswith('.')
       else:
            return False 

    def is_question(self):
       if self._value and isinstance(self._value, str):
          return self._value.endswith('?') 
       else:
          return False   
       
    def is_exclamation(self):
       if self._value and isinstance(self._value, str):
          return self._value.endswith('!')  
       else:
          return False  
       
    def count_sentences(self):
       if self._value and isinstance(self._value, str):
           sentence_count = sum(1 for sentence in self._value if sentence in ('.', '!', '?'))
           return sentence_count
       else:
          return 0
       
     
      
  
