import unittest

# Author: Zubery Msemo


# Create a empty list
frequency_of_string = {}


# def the function to calculate the occurance of Strings
def Occurance_of_String(name):
    # iterate the inputs to count the occurance of each string
    for i in Inputs:
        if i in frequency_of_string:
            frequency_of_string[i] += 1
        else:
            frequency_of_string[i] = 1

        # User Inputs


Inputs = "Mambo"
Occurance_of_String(Inputs)


# printing result
# print("Count of all characters in your String is :\n " + str(frequency_of_string))


class MyTestCase(unittest.TestCase):
    def test_Occurance(self):
        self.assertEqual(Occurance_of_String("Mambo"), None)

    def test_not_equal(self):
        self.assertIsNot(Occurance_of_String(name="Mambo"), "Mambo")

    def test_is_none(self):
        self.assertIsNone(Occurance_of_String(name="Ugly"))

    def test_is_number(self):
        self.assertIsNot(Occurance_of_String(123), 123)


if __name__ == '__main__':
    unittest.main()
