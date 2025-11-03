class hiding:
    __hidden_variable = "This is a hidden variable"

    def __hidden_method(self):
      return "This is a hidden method"

    def reveal(self):
        return (self.__hidden_variable, self.__hidden_method())
obj = hiding()
print(obj.reveal())    