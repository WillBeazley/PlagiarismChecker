class text:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def get_text1(self):
        return self.text1
    
    def get_text2(self):
        return self.text2


class checker:
    def __init__(self, text):
        self.text = text

    def split_text1(self):
        return self.text.get_text1().split(" ")
    
    def split_text2(self):
        return self.text.get_text2().split(" ")
    
    def output_text(self):
        return [self.split_text1(), self.split_text2()]
    
    def check_text(self):
        counter = 0
        words = []

        for i in self.output_text()[0]:
            for f in self.output_text()[1]:
                if i.lower() == f.lower():
                    counter += 1
                    words.append(i)

        percentage = (counter / len(self.output_text()[0])) * 100

        return percentage


print("----Plagiarism Chceker----")
text1 = input("Please input your text: ")
text2 = input("Please input text you want to check it against: ")

ob1 = text(text1, text2)

ob1Checker = checker(ob1)

print(f"Similarity percentage: {ob1Checker.check_text()}")