class StringManipulator:
    @staticmethod
    def reverse(input_string):
        return input_string[::-1]


string1 = input("Введите строку: ")
string2 = StringManipulator.reverse(string1)
print("Ваша строка наоборот: ", string2)