#ApertureTestMath = '2 million + 1 million + 3 billion + 1 trillion + 91203912 + 19999 + 9250 - 100 / 30.991 * 9'

newText = ''
newMathEquationMillion = ''
newMathEquationBillion = ''
newMathEquationTillion = ''
finalEquation = ''


def DoMath(text):
    newText = text.replace(" ", "")
    newMathEquationMillion = newText.replace('million', '000000')
    newMathEquationBillion = newMathEquationMillion.replace('billion', '000000000')
    newMathEquationTillion = newMathEquationBillion.replace('trillion', '000000000000')
    finalEquation = newMathEquationTillion

    print(finalEquation)
    print(eval(finalEquation))


#DoMath(ApertureTestMath)
