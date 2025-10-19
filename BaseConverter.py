import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.scrolled import ScrolledText
from tkinter import StringVar
import math
import os
import sys
import random
import clipboard
import smtplib
import pyqrcode
import png
from pyqrcode import QRCode
import socket

# getting whare script runs
main_path = os.path.abspath(sys.argv[0])
adding_path = main_path.split("\\")[:-1]
usersPath = "\\".join(adding_path)

# getting font.txt path
path0 = usersPath + "\\font.txt"

with open(path0, "r") as file:
    data = file.read()

selectedFontSize = data[:2]
isRounding = data[4:8]
isAutoCoping = data[10:13]
selectedFontFace = data[15:]

letters_to_int_conversion_dict = {

    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35

}

int_to_letters_conversion_dist = {

    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z"

}


def convert_to_any_number_system_function(con_base_param=None, number=None, base_cal=None):

    try:

        error_collector = []
        usingBaseConverter = isNegative = decimalPoint = False

        try:
            if entry_num.get() == "DEVELOPER":
                developerDis()
            elif entry_num.get() == "Out of the blue":
                outOfTheBlue()
        except Exception:
            pass

        if number is None:
            num = entry_num.get()
            usingBaseConverter = True
        else:
            num = number
        num = num.upper()

        if num[0] == "-":
            num = num[1:]
            isNegative = True

        if base_cal is None:
            base = entry_base.get()

            if base[0] == "-":
                Messagebox.show_info("Ran into a trouble that the developer did not except for :(", "Unknowen Error !", alert=True)
            
            if base != "":
                try:
                    base = int(base)
                except ValueError:
                    Messagebox.show_error("You can only enter integers for the base entry :(", "Error Occurred", alert=True)
            else:
                Messagebox.show_error("Empty Space !", "Opps !", alert=True)
        else:
            if base_cal == "":
                base = 10
            else:
                try:
                    base = int(base_cal)
                except ValueError:
                    Messagebox.show_error("You can only enter integers for the base entry :(", "Error Occurred", alert=True)

        checker = []
        counter_all = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        can_go = None

        # gathering number that are belong to current base
        for i in range(0, base, 1):
            if i <= 35:
                checker.append(counter_all[i])
            else:
                break

        # checking whether all characters are valid
        for i in range(0, len(num)):
            error_collector.append(num[i]) if num[i] not in checker else None

        # checking whether it's a floating number
        if len(error_collector) == 1 and error_collector[0] == ".":
            error_collector.clear()
            decimalPoint = True

        if len(error_collector) == 0:
            can_go = True
        else:
            can_go = False

        if num == "" or base == -1:
            Messagebox.show_error("You must have forgotten to enter number(s) for the entry :(", "Error Occurred", alert=True)
        elif can_go is False and len(error_collector) == 1:
            Messagebox.show_error(f"The digit you\'ve entered which is \n {error_collector} \n"
                                  f" is not belong to {base} based number system. :(", "Error", alert=True)
        elif can_go is False and len(error_collector) != 1:
            Messagebox.show_error(f"The digits you\'ve entered which are \n {error_collector} \n"
                                  f" aren't belong to base {base} number system. :(", "Error", alert=True)
        else:

            final = []
            ans = answer = ""
            y = 0
            letter_int = []
            value_list = []
            decimalNumbersArray = []
            indicator = decimalFinder = decimal = afterDecimal = isDecimal = total = 0

            if con_base_param == None:
                try:
                    con_base = int(entry_con_base.get())
                except ValueError:
                    if entry_con_base.get() == "":
                        isStupid = Messagebox.yesno("Have you filled the convert base input ?", "Error Occurred !", alert=True)
                        if isStupid == "Yes":
                            Messagebox.show_error("Please Check it again.", "Don't be stupid", alert=True)
                        else:
                            Messagebox.show_error("To get the answer you want you have to either fill the blak or click a button which has \nBinary, Decimal, etc. on it...", "Help", alert=True)
                    else:
                        Messagebox.show_error("You can only enter integers for the convert base entry :(", "Error Occurred", alert=True)
            else:
                con_base = int(con_base_param)

            # Converting letters to numbers
            for letter in num:
                if letter in letters_to_int_conversion_dict:
                    letter_int.append(letters_to_int_conversion_dict.get(letter))
                else:
                    letter_int.append(letter)

            # Finding the decimal value
                # if this isn't a decimal
            if decimalPoint is not True:
                for i in range(len(num)-1, -1, -1):
                    number = int(letter_int[i])
                    x = number * pow(base, indicator)
                    decimal = decimal + x
                    indicator += 1
                # if this is a non integer
            else:
                indexOfPoint = letter_int.index(".")
                decimalNumbers = str(num[indexOfPoint+1:])
                integer = num[:indexOfPoint]
                escapeIndex = str(convert_to_any_number_system_function(con_base, integer, base))
                integerNumbers = float(convert_to_any_number_system_function(10, integer, base)) 
                for i in range(0, len(decimalNumbers)):
                    decimalNumbersArray.append(decimalNumbers[i])

                for i in range(-1, -len(decimalNumbersArray)-1, -1):
                    if decimalNumbersArray[indicator] in letters_to_int_conversion_dict:
                        decimalNumbersArray[indicator] = letters_to_int_conversion_dict.get(decimalNumbersArray[indicator])
                    y = int(decimalNumbersArray[indicator])
                    decimal_point = y * math.pow(base, i)
                    integerNumbers += decimal_point
                    indicator += 1
                y = 0
                decimal = integerNumbers * pow(con_base, len(str(decimalNumbers)))

                if  decimal.is_integer():
                    decimal = int(decimal)
                else:
                    decimal = math.floor(float(integerNumbers) * pow(con_base, 7))

            # devide the decimal number by following conversion base to convert it to the needed base
            while decimal != 0:
                con_num = decimal % con_base
                decimal = decimal / con_base
                decimal = math.floor(decimal)
                value_list.append(con_num)

            # Replacing the needed number with a letter
            for j in range(0, len(value_list)):
                if value_list[j] in int_to_letters_conversion_dist:
                    replacer = int_to_letters_conversion_dist.get(value_list[j])
                    value_list[j] = replacer

            # Turning the array upside down
            for i in range(len(value_list) - 1, -1, -1):
                final.append(str(value_list[i]))
            
            # removing .0
            final.pop() if decimalPoint is True and final[len(final)-1] == 0 else None

            # Inserting the decimal point
            final.insert(len(str(escapeIndex)), ".") if decimalPoint is True else None

            # Converting array to a string
            answer = str("".join(final))

            # adding minus sign
            if isNegative is True:
                answer = "-" + answer

            if usingBaseConverter is False:
                return answer
            else:
               
                SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                con_base = str(con_base)
                SUP = con_base.translate(SUB)
                
                if SUP == "₁₀":
                    SUP = ""

                if isAutoCoping == " On":
                    clipboard.copy(answer)
                    messageAutoCopyMain(answer, None, True)
                else:    
                    responce = Messagebox.yesno(f"The Value Is {answer} {SUP} \n\nDo you want to copy the answer ?", "Answer",  alert=True)
                    if responce == "Yes":
                        clipboard.copy(answer)

            entry_num.delete(0, END)
            entry_con_base.delete(0, END)
            entry_base.delete(0, END)
    except TypeError as e:
        pass
    except IndexError as e:
        pass
    except UnboundLocalError as e:
        pass
    except Exception as e:
        Messagebox.show_info("The program just ran into an error that the developer did not expect for :(", "Unknowen Error !", alert=True)
        pass

# Functions for buttons
def convert_any_number_system_to_binary():
    convert_to_any_number_system_function(2, None, None)


def convert_any_number_system_to_octal():
    convert_to_any_number_system_function(8, None, None)


def convert_any_number_system_to_decimal():
    convert_to_any_number_system_function(10, None, None)


def convert_any_number_system_to_hex():
    convert_to_any_number_system_function(16, None, None)


def convert_any_number_system_to_ternary():
    convert_to_any_number_system_function(3, None, None)


def convert_any_number_system_to_quaternary():
    convert_to_any_number_system_function(4, None, None)


def convert_any_number_system_to_quinary():
    convert_to_any_number_system_function(5, None, None)


def convert_any_number_system_to_senary():
    convert_to_any_number_system_function(6, None, None)


def convert_any_number_system_to_septenary():
    convert_to_any_number_system_function(7, None, None)


rel_X0 = 1.5
randomRuns = True
runsOnesBlue = False
randomStarters = []
randomThemes = []

def outOfTheBlue():
    global rel_X0, frame0, runsOnesBlue, randomRuns, randomStarters, randomThemes
    starters = [0.5, 1.1, 1.6, 2.2, 1.5, 2.0, 0.3, 2.5]
    themes = ["DARK", "SUCCESS", "DANGER", "WARNING", "LIGHT", "INFO"]
    if randomRuns:

        randomStarters.clear()
        randomThemes.clear()

        for i in range(0, 8):
            randomStarters.append(random.choice(starters))
            randomThemes.append(random.choice(themes))

        randomRuns = False

    if runsOnesBlue is False:
        frame0.configure(bootstyle=(randomThemes[0]))
        frame1.configure(bootstyle=(randomThemes[1]))
        frame2.configure(bootstyle=(randomThemes[2]))
        frame3.configure(bootstyle=(randomThemes[3]))
        frame4.configure(bootstyle=(randomThemes[4]))
        if rel_X0 <= 1.5 and rel_X0 >= -4:
            rel_X0 -= 0.01
            frame0.place(relx=rel_X0, rely=0.05, relwidth=0.7, relheight=0.1)
            frame1.place(relx=( rel_X0 + randomStarters[0] ), rely=0.25, relwidth=0.7, relheight=0.1)
            frame2.place(relx=( rel_X0 + randomStarters[1] ), rely=0.45, relwidth=0.7, relheight=0.1)
            frame3.place(relx=( rel_X0 + randomStarters[2] ), rely=0.65, relwidth=0.7, relheight=0.1)
            frame4.place(relx=( rel_X0 + randomStarters[3] ), rely=0.85, relwidth=0.7, relheight=0.1)
            app.after(4, outOfTheBlue)
        else:
            runsOnesBlue = randomRuns = True
    else:
        frame0.configure(bootstyle=(randomThemes[5]))
        frame1.configure(bootstyle=(randomThemes[6]))
        frame2.configure(bootstyle=(randomThemes[7]))
        frame3.configure(bootstyle=(randomThemes[2]))
        frame4.configure(bootstyle=(randomThemes[1]))
        if rel_X0 <= 1.4:
            rel_X0 += 0.01
            frame0.place(relx=rel_X0, rely=0.05, relwidth=0.7, relheight=0.1)
            frame1.place(relx=( rel_X0 + randomStarters[4] ), rely=0.25, relwidth=0.7, relheight=0.1)
            frame2.place(relx=( rel_X0 + randomStarters[5] ), rely=0.45, relwidth=0.7, relheight=0.1)
            frame3.place(relx=( rel_X0 + randomStarters[6] ), rely=0.65, relwidth=0.7, relheight=0.1)
            frame4.place(relx=( rel_X0 + randomStarters[7] ), rely=0.85, relwidth=0.7, relheight=0.1)
            app.after(4, outOfTheBlue)
        else:
            runsOnesBlue = False
            randomRuns = True


rel_x = 1.4
forwards = 1

forwardAuto = True
XAxis = 1.5

def calculater():
    global rel_x, selectedFontFace, selectedFontSize, frameMessageAutoCopy
    operators = []
    convertedNumbers = []
    bases = []
    base = 0
    x = 0
    idk = False

    def messageAutoCopyCal():
        global XAxis, forwardAuto, frameMessageAutoCopy
        if forwardAuto:
            XAxis -= 0.01
            if XAxis > 0.73:
                autoMessageLabelCal = ttk.Label(frameMessageAutoCopy, text="Answer Copied !", bootstyle=("success-inverse"))
                autoMessageLabelCal.place(relx=0.1, rely=0.2)
                frameMessageAutoCopy.place(relx=XAxis, rely=0.05, relwidth=0.25, relheight=0.1)
                cal.after(4, messageAutoCopyCal)
            else:
                forwardAuto = False
                cal.after(1000, messageAutoCopyCal)
        else:
            XAxis += 0.01
            if XAxis < 1.5:
                frameMessageAutoCopy.place(relx=XAxis, rely=0.05, relwidth=0.25, relheight=0.1)
                cal.after(4, messageAutoCopyCal)
            else:
                forwardAuto = True

    def delete():
        convertedNumbers.clear()
        operators.clear()
        entryBase.delete(0, END)
        bases.clear()        

    def clear():
        operatorLabel.config(text="")
        entryNum.delete(0, END)
        delete()

    def converter():
        global base, x
        number = entryNum.get()
        base = entryBase.get()
        if number == "":
            Messagebox.show_error("You have not input any number yet !", "Opps !", alert=True)
            idk = True
            clear()
        bases.append(base)
        try:
            convertedNumbers.append(float(convert_to_any_number_system_function(10, number, base))) if number != "" else operators.pop()
        except IndexError:
            pass
        except TypeError:
            delete()
            clear()
        for i in range(0, len(convertedNumbers)):
            if convertedNumbers[i].is_integer():
                convertedNumbers[i] = int(convertedNumbers[i])  
        entryNum.delete(0, END)

    def addition():
        global x
        x = 0
        operatorLabel.config(text="+",font=(f"{selectedFontFace}", 25))
        operators.append("+")
        converter()

    def substraction():
        global x
        x = 0
        operatorLabel.config(text="-", font=(f"{selectedFontFace}", 25))
        operators.append("-")
        converter()

    def division():
        global x
        x = 0
        operatorLabel.config(text="/", font=(selectedFontFace, 14))
        operators.append("/")
        converter()

    def multipication():
        global x
        x = 0
        operatorLabel.config(text="x", font=(selectedFontFace, 18))
        operators.append("*")
        converter()

    def mod():
        global x
        x = 0
        operatorLabel.config(text="mod", font=(selectedFontFace, 18))
        operators.append("%")
        converter()

    def squareRoot():
        global x
        x = 1
        operatorLabel.config(text=f"sqr({entryNum.get()})", font=(selectedFontFace, 18))
        operators.append("√")
        converter()
        try:
            result = math.sqrt(convertedNumbers[len(convertedNumbers)-1])
            if bases[0] != "":
                if bases[0] == bases[len(bases)-1]:
                    result = convert_to_any_number_system_function(bases[0], str(result), 10)
                    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                    showingBase = str(bases[0])
                    SUP = showingBase.translate(SUB)
                else:
                    SUP = ""
            else:
                SUP = ""
                if isRounding == "True":
                    result = round(result)
                result = str(result)

            if SUP != "₁₀":
                SUP = SUP
            else:
                SUP = ""
            
            if result[len(result)-1] == ".":
                result = result[:len(result)-1]

            if isAutoCoping == " On":
                messageAutoCopyCal()
                clipboard.copy(result)
            else:
                if Messagebox.yesno(f"The value is {result} {SUP} \n\nDo you want to copy the answer ?", "Answer", alert=True):
                    clipboard.copy(result)
            operatorLabel.config(text="")
        except Exception:
                Messagebox.show_info("Ran into an exception that developer didn't look up for !", "Error Occurred !", alert=True)
        delete()

    def power():
        global x
        x = 0
        power = powEnter.get()
        if power == "":
            power = 2
        else:
            power = int(powEnter.get())
            operatorLabel.config(text=f"{entryNum.get()} \u00b2", font=(selectedFontFace, 14))
            operators.append("2X")
            converter()
            number = convertedNumbers[0]
            try:
                RaiseToPower = 1
                if number != 1 or power != 0:
                    for i in range(0, power):
                        RaiseToPower *= number
                if bases[0] != "":
                    if bases[0] == bases[len(bases)-1]:
                        RaiseToPower = convert_to_any_number_system_function(bases[0], str(RaiseToPower), 10) 
                        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                        showingBase = str(bases[0])
                        SUP = showingBase.translate(SUB)
                    else:
                        SUP = ""
                else:
                    SUP = ""
                if SUP != "₁₀":
                    SUP = SUP
                else:
                    SUP = ""
                    if isRounding == "True":
                        RaiseToPower = round(RaiseToPower)
                    RaiseToPower = str(RaiseToPower)
                if isAutoCoping == " On":
                    clipboard.copy(RaiseToPower)
                    messageAutoCopyCal()
                else:
                    if Messagebox.yesno(f"The value is {RaiseToPower} {SUP} \n\nDo you want to copy the answer ?", "Answer", alert=True):
                        clipboard.copy(RaiseToPower)
                operatorLabel.config(text="")
                powEnter.delete(0, END)
            except Exception as e:
                Messagebox.show_info("Ran into an exception that developer didn't look up for !", "Error Occurred !", alert=True)
            delete()
            
        
    def equal():
        try:
            global base, x
            temp = 0
            if x != 1:
                converter()
            operatorLabel.config(text="")
            result = arrayIndexFinder = 0
            for operator in range(0, len(operators)):
                if operators[operator] == "*":
                    x = 6
                elif operators[operator] == "/":
                    x = 5
                elif operators[operator] == "+":
                    x = 1
                elif operators[operator] == "-":
                    x = 2
                elif operators[operator] == "√":
                    x = 10
                elif operators[operator] == "%":
                    x = 9

                if arrayIndexFinder == 0:
                    if x == 1:
                        result = convertedNumbers[0] + convertedNumbers[1]
                    elif x == 2:
                        result = convertedNumbers[0] - convertedNumbers[1]
                    elif x == 5:
                        result = convertedNumbers[0] / convertedNumbers[1]
                    elif x == 6:
                        result = convertedNumbers[0] * convertedNumbers[1]
                    elif x == 9:
                        result = convertedNumbers[0] % convertedNumbers[1]
                    else:
                        pass
                    arrayIndexFinder = 2
                else:
                    for number in range(2, 3):
                        if x == 1:
                            result += convertedNumbers[arrayIndexFinder]
                        elif x == 2:
                            result -= convertedNumbers[arrayIndexFinder]
                        elif x == 5:
                            result /= convertedNumbers[arrayIndexFinder]
                        elif x == 6:
                            result *= convertedNumbers[arrayIndexFinder]
                        elif x == 9:
                            result %= convertedNumbers[arrayIndexFinder]
                        elif x == 11:
                            result **= convertedNumbers[arrayIndexFinder]
                        arrayIndexFinder += 1

                if result.is_integer():
                    result = int(result)
            if x == 9 and result == 0:
                Messagebox.show_info(f"The remain is none. ", "Answer", alert=True)
            else:
                if bases[0] != "":
                    if bases[0] == bases[len(bases)-1]:
                        result = convert_to_any_number_system_function(bases[0], str(result), 10) 
                        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                        showingBase = str(base)
                        SUP = showingBase.translate(SUB)
                    else:
                        SUP = ""
                else:
                    SUP = ""
                
                if isRounding == "True":
                    result = round(result)
                result = str(result)

            if SUP != "₁₀":
                SUP = SUP 
            else:
                SUP = ""
            if idk is False:
                if x != 9:
                    if isAutoCoping == " On":
                        clipboard.copy(result)
                        messageAutoCopyCal()
                    else:
                        calResponce = Messagebox.yesno(f"The value is {result} {SUP} \n\nDo you want to copy the answer ?", "Answer", alert=True)
                else:
                    if isAutoCopy == "Off":
                        clipboard.copy(result)
                        messageAutoCopyCal()
                    else:
                        try:
                            calResponce = Messagebox.yesno(f"The remainder is {result} {SUP} \n\nDo you want to copy the answer ?", "Answer", alert=True)
                        except UnboundLocalError:
                            pass
                try:
                    if calResponce == "Yes":
                        clipboard.copy(result)
                except:
                    pass
        except ZeroDivisionError:
            Messagebox.show_info("You can not divide by ZERO :(", "Division By Zero", alert=True)
        except IndexError or NameError:
            Messagebox.show_info("Empty Space !", "Opps !", alert=True)
        except TypeError:
            pass
        except Exception as e:
            Messagebox.show_info(f"Ran into an error that the developer did not excepted :(", "Error Occurred", alert=True)
        delete()

    def calHelp():
        global rel_x, forwards
        if forwards == 1:
            rel_x -= 0.1
            if rel_x > 0.6:
                frameHelp.place(anchor="center", relx=rel_x, rely=0.5, relwidth=0.5, relheight=0.95)
                cal.after(32, calHelp)
                forwards = 1
            else:
                forwards = 0
        else:
            rel_x += 0.1
            if rel_x <= 1.4:
                frameHelp.place(anchor="center", relx=rel_x, rely=0.5, relwidth=0.5, relheight=0.95)
                cal.after(32, calHelp)
                forwards = 0
            else:
                forwards = 1


    cal = ttk.Toplevel()
    cal.title("Calculator")
    cal.geometry("600x400")
    cal.minsize(400, 250)
    cal.maxsize(650, 450)
    cal.iconbitmap(usersPath + "\\Icons\\cal.ico")

    # Frames
    frameEntry = ttk.Frame(cal)
    frameBTNS = ttk.Frame(cal)
    frameHelp = ttk.Frame(cal)
    frameMessageAutoCopy = ttk.Frame(cal, bootstyle=(SUCCESS))

    # Frames configure
    frameEntry.rowconfigure((0), weight=1, uniform="a")
    frameEntry.columnconfigure((0, 1), weight=1, uniform="a")

    frameBTNS.rowconfigure((0, 1), weight=1, uniform="a")
    frameBTNS.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

    # widgets
    entryNum = ttk.Entry(frameEntry, bootstyle=(CalEntry))
    entryLab = ttk.Label(frameEntry, text="Number", bootstyle=(CalEntry))
    entryBase = ttk.Entry(frameEntry, bootstyle=(CalEntry))
    baseLab = ttk.Label(frameEntry, text="Base", bootstyle=(CalEntry))

    helpLabel1 = ttk.Label(master=frameHelp, text="G U I D E")
    helpLabel2 = ttk.Label(master=frameHelp, text="-------------------------")
    helpLabel3 = ttk.Label(master=frameHelp, text="• This calculater can do:\n"
                                                    "  - Addition\n"
                                                    "  - Substraction\n"
                                                    "  - Multiplication\n"
                                                    "  - Division\n"
                                                    "  - Squred\n"
                                                    "  - SquareRoot\n"
                                                    "  - MOD"
                                                    )
    helpLabel4 = ttk.Label(master=frameHelp, text="• Speciality")
    helpLabel5 = ttk.Label(master=frameHelp, text="     - The speciality about this calculater is\n  that you could"
                                                    "   calculate not only\n decimal based numbers but also many more. \n"
                                                    "   - Also you can calculate numbers in between\n  different based too.\n"
                                                    "  In that way the answer always will be in 10 !\n"
                                                    "   - You do not want to use the base entry\n  if you claculate in decimal."
                                                    )
    backBtn = ttk.Button(master=frameHelp, text="Back", bootstyle=(OUTLINE), command=calHelp)

    operatorLabel = ttk.Label(cal, text="", bootstyle=(SECONDARY), font=(selectedFontFace, 10))

    equalBtn = ttk.Button(frameBTNS, text="=", bootstyle=(SUCCESS), command=equal)
    checkAdd = ttk.Button(frameBTNS, text="+",bootstyle=(CalAdd, OUTLINE), command=addition)
    checkSub = ttk.Button(frameBTNS, text="-",bootstyle=(CalSub, OUTLINE), command=substraction)
    checkDiv = ttk.Button(frameBTNS, text="/",bootstyle=(CalDiv, OUTLINE), command=division)
    checkMulti = ttk.Button(frameBTNS, text="x",bootstyle=(CalMult, OUTLINE), command=multipication)
    checkMod = ttk.Button(frameBTNS, text="mod",bootstyle=(CalMod, OUTLINE), command=mod)
    checkSquareRoot = ttk.Button(frameBTNS, text="√",bootstyle=(CalSquare, OUTLINE), command=squareRoot)
    checkwar = ttk.Button(frameBTNS, text="X",bootstyle=(CalPow, OUTLINE), command=power)
    btnhelp = ttk.Button(cal, text="Help", bootstyle=(HelpBtn, OUTLINE), command=calHelp)
    btnClear = ttk.Button(master=cal, text="C", bootstyle=(CalC, OUTLINE), command=clear)
    powEnter = ttk.Entry(frameBTNS, bootstyle=(CalPow), width=2, font=(selectedFontFace, 9))

    # layout
    frameEntry.place(anchor="center", relx=0.5, rely=0.2, height=59, width=300)
    frameBTNS.place(anchor="center", relx=0.5, rely=0.7, height=140, width=400)
    frameHelp.place(anchor="center", relx=rel_x, rely=0.5, relwidth=0.5, relheight=0.98)
    frameMessageAutoCopy.place(relx=XAxis, rely=0.05, relwidth=0.25, relheight=0.1)

    entryNum.grid(row=0, column=0, sticky=S)
    entryLab.grid(row=0, column=0, sticky=NW)
    entryBase.grid(row=0, column=1, sticky=S)
    baseLab.grid(row=0, column=1, sticky=NW)

    checkAdd.grid(row=0, column=0, sticky=NSEW, padx=3, pady=3)
    checkSub.grid(row=0, column=1, sticky=NSEW, padx=3, pady=3)
    checkDiv.grid(row=0, column=2, sticky=NSEW, padx=3, pady=3)
    checkMulti.grid(row=0, column=3, sticky=NSEW, padx=3, pady=3)
    checkMod.grid(row=1, column=1, sticky=NSEW, padx=3, pady=3)
    checkSquareRoot.grid(row=1, column=0, sticky=NSEW, padx=3, pady=3)
    equalBtn.grid(row=1, column=3, sticky=NSEW, padx=3, pady=3)
    checkwar.grid(row=1, column=2, sticky=NSEW, padx=3, pady=3)
    btnhelp.place(anchor=CENTER, relx=0.95, rely=0.95)
    operatorLabel.place(anchor="center", relx=0.25, rely=0.15)
    btnClear.place(relx=0.22, rely=0.46, anchor="center", relheight=0.1, relwidth=0.1)
    powEnter.place(relx=0.68, rely=0.66, anchor="center", relheight=0.18)

    helpLabel1.place(anchor="center", relx=0.5, rely=0.1)
    helpLabel2.place(anchor="center", relx=0.5, rely=0.15)
    helpLabel3.place(relx=0.1, rely=0.2)
    helpLabel4.place(relx=0.1, rely=0.57)
    helpLabel5.place(relx=0.03, rely=0.62)
    backBtn.place(anchor="center", rely=0.1, relx=0.1, relheight=0.1)

    cal.mainloop()

backwords = 1
x_axis = 1.5

def how_to():
    Messagebox.show_info("Step 1 •\n Convert from source base to decimal (base 10) by muitiplying"
                        " each digit with the base raised to the power of the digit number"
                        " (starting from right digit number 0)\n"
                        "\n\n"
                        "Step 2 •\n Convert from decimal to destination base: divide the decimal with the" 
                        "base until the quotient is 0 and calculate the remainder each time. The destination base "
                        "digits are the calculated remainders.","How to convert any base to any base...", alert=True)

def help_user():
    global x_axis, backwords
    if backwords == 1:
        x_axis -= 0.1
        if x_axis >= 0.4:
            app.after(30, help_user)
            frame_help.place(relx=x_axis, rely=0.5, relheight=0.8, relwidth=0.7, anchor="center")
        else:
            backwords = 0
    else:
        x_axis += 0.1
        if x_axis <= 2:
            app.after(30, help_user)
            frame_help.place(relx=x_axis, rely=0.5, relheight=0.8, relwidth=0.7, anchor="center")
        else:
            backwords = 1


pathData = usersPath + "\\data.txt"
with open(pathData, "r") as file:
    userSelected = file.read()

currentAppearance = userSelected[:5]
currentTheme = userSelected[7:]


def settings():
    global location, currentAppearance, currentTheme
    settings = ttk.Toplevel()
    settings.geometry("600x520")
    settings.maxsize(1000, 1000)
    settings.minsize(500, 500)
    settings.title("Settings")
    settings.iconbitmap(usersPath + "\\Icons\\settings.ico")

    def restart():
        python = sys.executable
        script = sys.argv[0]

        os.execv(python, [python, script])
    
    def cancel():
        settings.destroy()

    def apply():
        path = usersPath + "\\data.txt"
        selectedTheme = themevar.get()
        selectedAppearance = appearanceVar.get()
        fontFace = fontFaceVar.get()
        fontSize = fontSizeVar.get()
        isAutoCoping = AutoCopyVar.get()
        isRounding = roundCheckVar.get()
        
        with open(path0, "w") as file:
            file.write(f"{fontSize}, {isRounding}, {isAutoCoping}, {fontFace}")

        if selectedAppearance == "Tiles":
            if selectedTheme == "DARK":
                with open(path, "w") as file:
                    file.write("Tiles, DARK")
            elif selectedTheme == "LIGHT":
                with open(path, "w") as file:
                    file.write("Tiles, LIGHT")
            elif selectedTheme == "BLUE":
                with open(path, "w") as file:
                    file.write("Tiles, BLUE")
            else:
                pass
        else:
            if selectedTheme == "DARK":
                with open(path, "w") as file:
                    file.write("  Art, DARK")
            elif selectedTheme == "LIGHT":
                with open(path, "w") as file:
                    file.write("  Art, LIGHT")
            elif selectedTheme == "BLUE":
                with open(path, "w") as file:
                    file.write("  Art, BLUE")
            else:
                pass

        Messagebox.show_info("Application will be restart to apply the new settings.", "Appling Settings", alert=True)
        restart()

    # Widgets
    labelBg = ttk.Label(settings, text="", bootstyle=(SUCCESS, INVERSE))
    labelBg1 = ttk.Label(settings, text="", bootstyle=(WARNING, INVERSE))
    themeText = ttk.Label(settings, text="Theme", bootstyle=(SUCCESS, INVERSE))
    appearanceText = ttk.Label(settings, text="Appearance", bootstyle=(WARNING, INVERSE))

    themevar = StringVar(value=currentTheme)
    themex = 0.05
    for theme in ["DARK", "LIGHT", "BLUE"]:
        themeRadio = ttk.Radiobutton(settings, bootstyle=(SUCCESS, TOOLBUTTON, OUTLINE),  variable=themevar, text=theme, value=theme)
        themeRadio.place(relx=themex, rely=0.1)
        themex += 0.15

    appearanceVar = StringVar(value=currentAppearance)
    appeax = 0.63
    for appearance in ["Tiles", "  Art"]:
        appearanceRadio = ttk.Radiobutton(master=settings, bootstyle=(WARNING, TOOLBUTTON, OUTLINE), variable=appearanceVar, text=appearance, value=appearance)
        appearanceRadio.place(relx=appeax, rely=0.1)
        appeax += 0.15
    
    # Font Face Menubutton
    fontFaceVar = StringVar(value=selectedFontFace)
    fontBg = ttk.Label(settings, text="", bootstyle=(DANGER, INVERSE))
    fontLabel = ttk.Label(settings, text="Font", bootstyle=(DANGER, INVERSE))
    fontMenuBTN = ttk.Menubutton(settings, bootstyle=(DANGER), text=f"{fontFaceVar.get()}")
    fontMenu = ttk.Menu(fontMenuBTN)
    for fontFace in ["Helvetica", "Comic Sans Ms", "Arial Black", "Times New Roman", "High Tower Text", "Harrington"]:
        fontMenu.add_radiobutton(label=fontFace, variable=fontFaceVar)
    fontMenuBTN["menu"] = fontMenu

    # Font Size MenuButton
    fontSizeVar = StringVar(value=selectedFontSize)
    fontSizeBg = ttk.Label(settings, text="", bootstyle=(font_size, INVERSE))
    fontSize = ttk.Label(settings, text="Font Size", bootstyle=(font_size, INVERSE))
    fontSizeMenuBTN = ttk.Menubutton(settings, bootstyle=f"{font_size}", text=f"{fontSizeVar.get()}")
    fontSizeMenu = ttk.Menu(fontSizeMenuBTN)
    for fontSizeList in [" 4", " 6", " 8", " 9", "10", "11", "12", "13"]:
        fontSizeMenu.add_radiobutton(label=fontSizeList, variable=fontSizeVar)
    fontSizeMenuBTN["menu"] = fontSizeMenu

    roundBg1 = ttk.Label(settings, bootstyle=(INFO, INVERSE))
    roundBg2 = ttk.Label(settings, bootstyle=(INFO, INVERSE))
    roundText = ttk.Label(settings, text="Round the answer when using the calculater", font=(selectedFontFace, 12))
    roundBg3 = ttk.Label(settings, bootstyle=(INFO, INVERSE))
    roundBg4 = ttk.Label(settings, bootstyle=(INFO, INVERSE))
    roundCheckVar = StringVar(value=isRounding)
    roundCheckBTN = ttk.Checkbutton(settings, bootstyle=(INFO, "round-toggle"), variable=roundCheckVar, onvalue="True", offvalue="NotT")

    def autoCopy():
        if AutoCopyVar.get() == " On":
            AutoCopy.config(text=f"Auto Copy Any Result is On")
        else:
            AutoCopy.config(text=f"Auto Copy Any Result is Off")

    AutoCopyVar = StringVar(value=isAutoCoping)
    AutoCopy = ttk.Checkbutton(settings, text=f"Auto Copy Any Result is {isAutoCoping}", bootstyle=(SECONDARY, TOOLBUTTON, OUTLINE), onvalue=" On", offvalue="Off", variable=AutoCopyVar, command=autoCopy)

    applyBTN = ttk.Button(settings, text="Apply", bootstyle=(SUCCESS), command=apply)
    cancelBTN = ttk.Button(settings, text="Cancel", bootstyle=(DANGER), command=cancel)

    # layout
    themeText.place(relx=0.25, rely=0.05, anchor="center")
    appearanceText.place(relx=0.75, rely=0.05, anchor="center")
    cancelBTN.place(relx=0.98, rely=0.98, anchor="se")
    applyBTN.place(relx=0.71, rely=0.98, anchor="sw")
    labelBg.place(relx=0.01, rely=0.01, relheight=0.2, relwidth=0.49)
    labelBg1.place(relx=0.51, rely=0.01, relheight=0.2, relwidth=0.48)
    fontBg.place(relx=0.01, rely=0.22, relheight=0.1, relwidth=0.6)
    fontLabel.place(relx=0.05, rely=0.25)
    fontMenuBTN.place(relx=0.25, rely=0.24)
    fontSizeBg.place(relx=0.62, rely=0.22, relwidth=0.37, relheight=0.1)
    fontSize.place(relx=0.64, rely=0.25)
    fontSizeMenuBTN.place(relx=0.85, rely=0.24)
    roundBg1.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.005)
    roundText.place(relx=0.15, rely=0.346)
    roundBg2.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.005)
    roundCheckBTN.place(relx=0.75, rely=0.355)
    roundBg3.place(relx=0.01, rely=0.335, relwidth=0.005, relheight=0.07)
    roundBg4.place(relx=0.984, rely=0.335, relheight=0.07, relwidth=0.005)
    AutoCopy.place(relx=0.01, rely=0.42, relwidth=0.35, relheight=0.2)

    settings.mainloop()

def otherMenuCmd():
    converter = OtherVar.get()
    
    def deleteOut():
        OutputText.delete("1.0", "end-1c")
        inputText.delete("1.0", "end-1c")
        OutputText.insert(tk.END, "# Output Text will be displayed here...")
        
    def copyOut():
        clipboard.copy(OutputText.get("1.0", "end-1c"))

    if converter == "Convert ASCII Text To Binary, Hex, Decimal":
                    # Hex    Binary    Decimal ASCII
        SpaceHBD = [" 20", " 00100000", " 32", " "]
        EnterHBD = [" 0D", " 00001010", " 13", "\n"]
        addSpace = addEnter = ""
        
        def getText():
            OutputText.delete("1.0", "end-1c")
            combo01 = combo1.get()
            combo02 = combo2.get()
            word = inputText.get("1.0", "end-1c")
            pathASCII = usersPath + "\\ASCIIDataBase.txt"
            collecterForASCII = []
            array = []
            enterIndex = []
            final = ""
            z = e = 0
            runsOnce = False
            spaceList = []
            HexCollector = []
            errors = []

            def inserting(spaceList, array, enterIndex):
                for i in spaceList:
                    array.insert(i, addSpace) 
                
                for i in enterIndex:
                    array.insert(i, addEnter)
                return array

            if combo01 == "ASCII":
                for letter in word:
                    if letter == " ":
                        spaceList.append(z)
                    if letter == "\n":
                        z -= 1
                    z += 1
            
                for enter in word:
                    if enter == "\n":
                        enterIndex.append(e)
                    e += 1

                with open(pathASCII, "r") as file:
                    for i in range(0, 129):
                        x = file.readline()
                        for letter in word:
                            if letter == x[:1]:
                                collecterForASCII.append(x)

                for letter in word:
                    for i in collecterForASCII:
                        if i[:1] == letter and runsOnce is False:
                            if combo02 == "Hexadecimal":
                                array.append(i[4:7])
                                addSpace = SpaceHBD[0]
                                addEnter = EnterHBD[0]
                            elif combo02 == "Binary":
                                array.append(i[13:22])
                                addSpace = SpaceHBD[1]
                                addEnter = EnterHBD[1]
                            elif combo02 == "Decimal":
                                array.append(i[24:28])
                                addSpace = SpaceHBD[2]
                                addEnter = EnterHBD[2]
                            runsOnce = True
                    runsOnce = False

                array = inserting(spaceList, array, enterIndex)

                array[0] = array[0][1:]

            elif combo01 == "Binary":
                        
                binaryCollector = []
                binCode = ""
                
                for i in word:
                    if i != "0" and i != "1" and i != " ":
                        errors.append(i)
                        break

                Messagebox.show_error(f"{errors}", "Invalid character !", alert=True) if len(errors) != 0 else None
                if len(errors) == 0:
                    counting = 0
                    collecterForBinary = []
                    wordloop = word + " "
                    for i in wordloop:
                        if i == " ":
                            binaryCollector.append(binCode)
                            binCode = ""
                        else:
                            binCode += i

                    with open(pathASCII, "r") as file:
                        for i in range(0, 129):
                            x = file.readline()
                            for i in binaryCollector:
                                if i == x[14:22]:
                                    collecterForBinary.append(x)

                    # Space
                    for i in binaryCollector:
                        if i == "00100000":
                            spaceList.append(z)
                        if i == "00001010":
                            z -= 1
                        z += 1

                    # Enter
                    for i in binaryCollector:
                        if i == "00001010":
                            enterIndex.append(e)
                        e += 1

                    for code in binaryCollector:
                        for i in collecterForBinary:
                            if i[14:22] == code and runsOnce is False:
                                if combo02 == "Hexadecimal":
                                    array.append(i[4:7])
                                    addSpace = SpaceHBD[0]
                                    addEnter = EnterHBD[0]
                                elif combo02 == "Decimal":
                                    array.append(i[24:28])
                                    addSpace = SpaceHBD[2]
                                    addEnter = EnterHBD[2]
                                elif combo02 == "ASCII":
                                    array.append(i[:1])
                                    addSpace = SpaceHBD[3]
                                    addEnter = EnterHBD[3]
                                else:
                                    array.append(i[14:22])
                                    addSpace = SpaceHBD[1]
                                    addEnter = EnterHBD[1]
                                runsOnce = True
                        runsOnce = False
                    
                    array = inserting(spaceList, array, enterIndex)

            elif combo01 == "Hexadecimal":
                HexCollector = []
                HexCode = ""
                collecterForHexadecimal = []
                Hexloop = word + " "
                errorsHex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", " "]

                for i in word:
                    isWrong = True
                    for j in errorsHex:
                        if i == j:
                            isWrong = False
                    if isWrong is True:
                        errors.append(i)
                        break

                Messagebox.show_error(f"{errors}", "Invalid Character !", alert=True) if len(errors) != 0 else None

                if len(errors) == 0:
                    for i in Hexloop:
                        if i == " ":
                            HexCollector.append(HexCode)
                            HexCode = ""
                        else:
                            HexCode += i
                
                    with open(pathASCII, "r") as file:
                        for i in range(0, 129):
                            x = file.readline()
                            for i in HexCollector:
                                if i == x[5:7]:
                                    collecterForHexadecimal.append(x)

                # Space
                    for i in HexCollector:
                        if i == "20":
                            spaceList.append(z)
                        if i == "0D":
                            z -= 1
                        z += 1
                
                # Enter
                    for i in HexCollector:
                        if i == "0D":
                            enterIndex.append(e)
                        e += 1

                    for code in HexCollector:
                        for i in collecterForHexadecimal:
                            if i[5:7] == code and runsOnce is False:
                                if combo02 == "Decimal":
                                    array.append(i[24:28])
                                    addSpace = SpaceHBD[2]
                                    addEnter = EnterHBD[2]
                                elif combo02 == "ASCII":
                                    array.append(i[:1])
                                    addSpace = SpaceHBD[3]
                                    addEnter = EnterHBD[3]
                                elif combo02 == "Binary":
                                    array.append(i[13:22])
                                    addSpace = SpaceHBD[1]
                                    addEnter = EnterHBD[1]
                                else:
                                    array.append(i[5:7])
                                    addSpace = SpaceHBD[0]
                                    addEnter = EnterHBD[0]
                                runsOnce = True
                        runsOnce = False

                    array = inserting(spaceList, array, enterIndex)

            elif combo01 == "Decimal":
                DecCollector = []
                DecCode = ""
                collectorForDecimal = []
                Decloop = word + " "

                for i in Decloop:
                    if i == " ":
                        DecCollector.append(DecCode)
                        DecCode = ""
                    else:
                        DecCode += i

                try:
                    DecCollector.remove("")
                except ValueError:
                    pass

                for i in range(0, len(DecCollector)):
                    if len(DecCollector[i]) == 2:
                        DecCollector[i] = DecCollector[i] + " "

                with open(pathASCII, "r") as file:
                    for i in range(0, 129):
                        x = file.readline()
                        for i in DecCollector:
                            if i == x[25:28]:
                                collectorForDecimal.append(x)
                            if i == " ":
                                break
                
                # Space
                for i in DecCollector:
                    if i == "32 ":
                        spaceList.append(z)
                    if i == "13 ":
                        z -= 1
                    z += 1
                
                # Enter
                for i in DecCollector:
                    if i == "13 ":
                        enterIndex.append(e)
                    e += 1

                for code in DecCollector:
                    for i in collectorForDecimal:
                        if i[25:28] == code and runsOnce is False:
                            if combo02 == "Hexadecimal":
                                array.append(i[5:7])
                                addSpace = SpaceHBD[0]
                                addEnter = EnterHBD[0]
                            elif combo02 == "Binary":
                                array.append(i[13:22])
                                addSpace = SpaceHBD[1]
                                addEnter = EnterHBD[1]
                            elif combo02 == "ASCII":
                                array.append(i[:1])
                                addEnter = EnterHBD[3]
                                addSpace = SpaceHBD[3]
                            else:
                                array.append(i[25:28])
                                addEnter = EnterHBD[2]
                                addSpace = SpaceHBD[2]
                            runsOnce = True
                    runsOnce = False
            
                if combo02 == "Hexadecimal":
                    for i in range(0, len(array)):
                        if len(array[i]) != 0 and array[i][len(array[i])-1] != " " :
                            p = array[i] + " "
                            array.remove(array[i])
                            array.insert(i, p)

                if combo02 == "Hexadecimal":
                    addSpace += " "
                    addEnter += " "

                array = inserting(spaceList, array, enterIndex) 

            for character in range(0, len(array)):
                final = final + array[character]
        
            if final[:1] == "":
                final = final[1:]

            OutputText.insert(tk.END, final)
            if isAutoCoping == " On":
                clipboard.copy(final)


        Tbhd = ttk.Toplevel()
        Tbhd.geometry("900x900")
        Tbhd.minsize(900,900)
        Tbhd.maxsize(900,900)
        Tbhd.title("Convert ASCII Text To Binary, Hex, Decimal")
        Tbhd.iconbitmap(usersPath + "\\Icons\\Ascii.ico")

        comboList = ["Hexadecimal", "Decimal", "Binary", "ASCII"]
        combo1 = ttk.Combobox(Tbhd, bootstyle=(Entry), values=comboList)
        combo1.current(3)
        toLabel = ttk.Label(Tbhd, text="TO")
        combo2 = ttk.Combobox(Tbhd, bootstyle=(Entry), values=comboList)
        combo2.current(2)
        label = ttk.Label(Tbhd, text="Enter the converting text here...", bootstyle=(Entry))
        inputText = ScrolledText(Tbhd, height=20, width=98, wrap=WORD, autohide=True, bootstyle=(Entry))
        convertBtn = ttk.Button(Tbhd, text=f"Convert", bootstyle=(Entry, OUTLINE), command=getText)
        OutputText = ScrolledText(Tbhd, height=20, width=98, wrap=WORD, autohide=True, bootstyle=(Entry))
        btnOutputCopy = ttk.Button(Tbhd, text="Copy Text", bootstyle=(SUCCESS, OUTLINE), command=copyOut)
        btnOutdelete = ttk.Button(Tbhd, text="Delete All Text", bootstyle=(DANGER, OUTLINE), command=deleteOut)
        OutputText.insert(tk.END, "# Output Text will be displayed here...")

        combo1.place(relx=0.3, rely=0.05, anchor="center")
        toLabel.place(relx=0.5, rely=0.05, anchor="center") 
        combo2.place(relx=0.7, rely=0.05, anchor="center")
        label.place(relx=0.01, rely=0.1)
        inputText.place(relx=0.495, rely=0.32, anchor="center", relwidth=0.98)
        convertBtn.place(relx=0.5, rely=0.55, relwidth=0.8, anchor="center")
        OutputText.place(anchor="s", relx=0.45, rely=0.98)
        btnOutputCopy.place(anchor="center", relx=0.93, rely=0.8)
        btnOutdelete.place(anchor="center", rely=0.85, relx=0.92)
        
        Tbhd.mainloop()

    elif converter == "QR Code Generator":

        def messageQR(mode=None):
            global relxqr, forwardqr
            if mode != None:
                boot = mode 
                
                if mode == "success":
                    labelQR.configure(text=f"File saved to my QR's", bootstyle=f"{mode}-inverse")
                    frameMG.configure(bootstyle=f"{mode}")
                    
                elif mode == "name":
                    labelQR.configure(text=f"You have to fill the entry to save the image", bootstyle="danger-inverse")
                    frameMG.configure(bootstyle=f"danger")
                elif mode == "dot":
                    labelQR.configure(text=f"Invalid character in name ' . '", bootstyle="danger-inverse")
                    frameMG.configure(bootstyle=f"danger")
                else:
                    labelQR.configure(text="Somthing went wrong !", bootstyle=f"{mode}-inverse")
                    frameMG.configure(bootstyle=f"{mode}")

            if forwardqr:
                if relxqr > 0.3:
                    relxqr -= 0.01
                    frameMG.place(relx=relxqr, rely=0.02, relwidth=0.68, relheight=0.1)
                    qr.after(3, messageQR)
                else:
                    forwardqr = False
                    qr.after(2000, messageQR)
            else:
                if relxqr >= 0.2 and relxqr < 1.9:
                    relxqr += 0.01
                    frameMG.place(relx=relxqr, rely=0.02, relwidth=0.68, relheight=0.1)
                    qr.after(3, messageQR)
                else:
                    forwardqr = True


        def createQR():
            
            try:
                if len(saveEntry.get()) != 0:

                    dot = False
                    for i in saveEntry.get():
                        if i == ".":
                            dot = True

                    if dot is False:
                        name = saveEntry.get()
                        text = insert.get("1.0", "end-1c")
                        QRCode = pyqrcode.create(text)
                        QRCode.png(f"{usersPath}\\My_QR's\\{name}.jpg", scale=8)
                        messageQR("success")
                    else:
                        messageQR("dot")
                else:
                    messageQR("name")
            except Exception as e:
                messageQR("danger")

        qr = ttk.Toplevel()
        qr.geometry("500x500")
        qr.maxsize(500,500)
        qr.minsize(500,500)
        qr.title("QR Code Generator")
        qr.iconbitmap(usersPath + "\\Icons\\QR.ico")

        insert = ScrolledText(qr, height=20, width=70, wrap=WORD, autohide=True, bootstyle=(WARNING))
        generateBTN = ttk.Button(qr, text="Generate & Save QR", bootstyle=(SUCCESS, OUTLINE), command=createQR)
        frameMG = ttk.Frame(qr, bootstyle=(SUCCESS))
        labelQR = ttk.Label(frameMG)
        saveLabel = ttk.Label(qr, text="Save Image As")
        saveEntry = ttk.Entry(qr)

        frameMG.place(relx=relxqr, rely=0.02, relwidth=0.68, relheight=0.1)
        insert.place(relx=0.5, rely=0.35, anchor="center")
        labelQR.place(anchor="w", relx=0.05, rely=0.5)
        generateBTN.place(anchor="center", relx=0.5, rely=0.9)
        saveLabel.place(anchor="center", relx=0.3, rely=0.75)
        saveEntry.place(anchor="center", relx=0.6, rely=0.75)

        qr.mainloop()


relxqr = 1.2
forwardqr = True

if currentTheme == "BLUE":

    font_size = "LIGHT"

    BinaryBTN = "INFO"
    DecimalBTN = "DANGER"
    OctalBTN = "LIGHT"
    HexadecimalBTN = "WARNING"
    TernaryBTN = "SUCCESS"
    QuaternaryBTN = "DANGER"
    QuinaryBTN = "LIGHT"
    SenaryBTN = "WARNING"
    SeptenaryBTN = "SUCCESS"
    CalculaterBTN = "DARK"
    
    Entry = "SUCCESS"
    OkBtn = "SUCCESS"

    CalEntry = "SUCCESS"

    CalC = "WARNING"
    CalAdd = "LIGHT"
    CalSub = "LIGHT"
    CalDiv = "LIGHT"
    CalMult = "LIGHT"
    CalSquare = "DANGER"
    CalMod = "LIGHT"
    CalPow = "DANGER"
    Method = "INFO"
    SettingBTN = "INFO"
    HelpBtn = "INFO"
    Back = "INFO"

elif currentTheme == "DARK":

    font_size = "LIGHT"

    BinaryBTN = "LIGHT"
    DecimalBTN = "LIGHT"
    OctalBTN = "LIGHT"
    HexadecimalBTN = "LIGHT"
    TernaryBTN = "LIGHT"
    QuaternaryBTN = "LIGHT"
    QuinaryBTN = "LIGHT"
    SenaryBTN = "LIGHT"
    SeptenaryBTN = "LIGHT"
    CalculaterBTN = "LIGHT"

    Entry = "LIGHT"
    OkBtn = "LIGHT"

    CalEntry = "INFO"

    CalC = "WARNING"
    CalAdd = "LIGHT"
    CalSub = "LIGHT"
    CalDiv = "LIGHT"
    CalMult = "LIGHT"
    CalSquare = "WARNING"
    CalMod = "LIGHT"
    CalPow = "WARNING"
    Method = "INFO"
    SettingBTN = "INFO"
    HelpBtn = "INFO"
    Back = "INFO"

else:

    font_size = "DARK"

    BinaryBTN = "SUCCESS"
    DecimalBTN = "SUCCESS"
    OctalBTN = "SUCCESS"
    HexadecimalBTN = "DARK"
    TernaryBTN = "DARK"
    QuaternaryBTN = "SUCCESS"
    QuinaryBTN = "SUCCESS"
    SenaryBTN = "DARK"
    SeptenaryBTN = "DARK"
    CalculaterBTN = "DARK"

    Entry = "DARK"
    OkBtn = "SUCCESS"

    CalEntry = "DARK"

    CalC = "DARK"
    CalAdd = "SUCCESS"
    CalSub = "SUCCESS"
    CalDiv = "DARK"
    CalMult = "DARK"
    CalSquare = "SUCCESS"
    CalMod = "DARK"
    CalPow = "DARK"
    Method = "DARK"
    SettingBTN = "DARK"
    HelpBtn = "DARK"
    Back = "DARK"

if currentTheme == "BLUE":
    ThemeName = "superhero"
elif currentTheme == "DARK":
    ThemeName = "darkly"
else:
    ThemeName = "cosmo"

xAxis = 1.5
forward = True
autoCopy = textMessage = bootMsg = ""
def messageAutoCopyMain(autoCopiedAnswer=None, message=None, runsOnce=False):
    global xAxis, forward, autoCopy, textMessage, bootMsg

    if runsOnce:
        if autoCopiedAnswer is not None and message is None:
            textMessage = f"{autoCopiedAnswer}, Answer copied to clipboard !\t\t\t"
            bootMsg = "success-inverse"
            frameAutoCopy.configure(bootstyle=(SUCCESS))
        elif autoCopiedAnswer is None and message == "Network Error":
            textMessage = "You are not connected to internet.\t\t\t"
            bootMsg = "warning-inverse"
            frameAutoCopy.configure(bootstyle=(WARNING))

    count = 0
    
    if forward is True:
        xAxis -= 0.01
        if xAxis > 0.78:
            app.after(4, messageAutoCopyMain)
            copyLabel = ttk.Label(master=frameAutoCopy, text=f"{textMessage}", bootstyle=(f"{bootMsg}"))
            copyLabel.place(relx=0.1, rely=0.2)
            frameAutoCopy.place(relx=xAxis, rely=0.04, relheight=0.05, relwidth=0.4, anchor="center")
        else:
            forward = False
            app.after(2000, messageAutoCopyMain)
    else:
        xAxis += 0.01
        if xAxis < 1.5:
            forward = False
            app.after(4, messageAutoCopyMain)
            frameAutoCopy.place(relx=xAxis, rely=0.04, relheight=0.05, relwidth=0.4, anchor="center")
        else:
            forward = True

devAxis = 1.5
devFor = True

def developerDis():
    global devAxis, devFor, developerFrame
    if devFor:
        devAxis -= 0.01
        if devAxis > 0.5:
            developerFrame.place(anchor="center", relx=devAxis, rely=0.08)
            app.after(15, developerDis)
        else:
            devFor = False
            app.after(3000, developerDis)
    else:
        devAxis += 0.01
        if devAxis < 1.5:
            developerFrame.place(anchor="center", relx=devAxis, rely=0.08)
            app.after(15, developerDis)
        else:
            devFor = True

# main window
app = ttk.Window(themename=ThemeName)
app.title("Base Converter")
app.geometry("900x900")
app.minsize(550, 350)
app.maxsize(1500, 1500)
app.iconbitmap(usersPath + "\\Icons\\favicon.ico")
app.iconbitmap(default=usersPath + "\\Icons\\favicon.ico")

# styling
buttonStyle = ttk.Style()
buttonStyle.configure('TButton', font=(selectedFontFace, selectedFontSize))
labelStyle = ttk.Style()
labelStyle.configure('TLabel', font=(selectedFontFace, selectedFontSize))
menuStyle = ttk.Style()
menuStyle.configure('TMenubutton', font=(selectedFontFace, selectedFontSize))
comboStyle = ttk.Style()
comboStyle.configure('TCombobox', font=(selectedFontFace, selectedFontSize))
checkStyle = ttk.Style()
checkStyle.configure('TCheckbutton', font=(selectedFontFace, selectedFontSize))

# frames
frame = ttk.Frame(app)
if currentAppearance == "  Art" and currentTheme == "darkly":
    frame_btns = ttk.Frame(app, bootstyle=(DARK)) 
else:
    frame_btns = ttk.Frame(app)
frame_help = ttk.Frame(app)
frameAutoCopy = ttk.Frame(app, bootstyle=(SUCCESS))
developerFrame = ttk.Frame(app)

# frame grid configure
frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="s")
frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

frame_help.place(relx=x_axis, rely=0.5, relheight=0.8, relwidth=0.75, anchor="center")
frameAutoCopy.place(relx=xAxis, rely=0.04, relheight=0.05, relwidth=0.4, anchor="center")
developerFrame.place(relx=devAxis, rely=0.08, relheight=0.08, relwidth=0.4)

developerText = ttk.Label(developerFrame, text="Hey you just found me, my name is GETHMIN")
developerText.place(anchor="center", relx=0.5, rely=0.5)


# widgets in app
help_btn = ttk.Button(app, text="HELP", bootstyle=(HelpBtn, OUTLINE), command=help_user)
how_to = ttk.Button(app, text="Method used in this application.", bootstyle=(Method, LINK), command=how_to)
settingsBTN = ttk.Button(master=app, text="Settings", bootstyle=(SettingBTN, OUTLINE), command=settings)
OtherVar = StringVar()
OtherMenuButton = ttk.Menubutton(app, text="Other Converters", bootstyle=(INFO))
OtherMenu = ttk.Menu(OtherMenuButton)
for other in ["Convert ASCII Text To Binary, Hex, Decimal", "QR Code Generator"]:
    OtherMenu.add_radiobutton(label=other, variable=OtherVar, command=otherMenuCmd)
OtherMenuButton["menu"] = OtherMenu
labelMSG = ttk.Label(app, text="Answer copied to your clipboard !", bootstyle=(PRIMARY))

# widgets in frame_btns
btn_hex = ttk.Button(frame_btns, text="Hexadecimal", bootstyle=(HexadecimalBTN, OUTLINE), command=convert_any_number_system_to_hex)
btn_binary = ttk.Button(frame_btns, text="Binary", bootstyle=(BinaryBTN, OUTLINE), command=convert_any_number_system_to_binary)
btn_decimal = ttk.Button(frame_btns, text="Decimal", bootstyle=(DecimalBTN, OUTLINE), command=convert_any_number_system_to_decimal)
btn_octal = ttk.Button(frame_btns, text="Octal", bootstyle=(OctalBTN, OUTLINE), command=convert_any_number_system_to_octal)
btn_ternary = ttk.Button(frame_btns, text="Ternary", bootstyle=(TernaryBTN, OUTLINE), command=convert_any_number_system_to_ternary)
btn_quaternary = ttk.Button(frame_btns, text="Quaternary", bootstyle=(QuaternaryBTN, OUTLINE), command=convert_any_number_system_to_quaternary)
btn_senary = ttk.Button(frame_btns, text="Senary", bootstyle=(SenaryBTN, OUTLINE), command=convert_any_number_system_to_senary)
btn_septenary = ttk.Button(frame_btns, text="Septenary", bootstyle=(SeptenaryBTN, OUTLINE), command=convert_any_number_system_to_septenary)
btn_quinary = ttk.Button(frame_btns, text="Quinary", bootstyle=(QuinaryBTN, OUTLINE), command=convert_any_number_system_to_quinary)

if currentAppearance != "  Art":
    btn_base = ttk.Button(frame_btns, text="Calculater", bootstyle=(CalculaterBTN), command=calculater)
else:
    btn_baseart = ttk.Button(app, text="Cal", bootstyle=(CalculaterBTN), command=calculater)  

# widgets in frame
label_num = ttk.Label(frame, text="Number", bootstyle=(Entry))
entry_num = ttk.Entry(frame, bootstyle=(Entry), width=50)
label_base = ttk.Label(frame, text="Base", bootstyle=(Entry))
entry_base = ttk.Entry(frame, bootstyle=(Entry), width=50)
label_entry = ttk.Label(frame, text="Convert this to base ", bootstyle=(Entry))
entry_con_base = ttk.Entry(frame, bootstyle=(Entry), width=21)
btn = ttk.Button(frame, text="Ok", bootstyle=(OkBtn, OUTLINE), command=convert_to_any_number_system_function)

# widgets in frame help
label1 = ttk.Label(master=frame_help, text="G U I D E", font=(selectedFontFace, 10))
label2 = ttk.Label(master=frame_help, text="-----------------------------------------------------")
labelDetails = ttk.Label(master=frame_help, text="• This program converts bases.\n"
                                                "   You just have to fill the blanks correctly.\n\n"
                                                "• If you use those buttons in the program, you just have to fill the \n"
                                                "  \"Number\" entry and \"Base\" entry only. Even though if you fill\n  the"
                                                "   other entry which is \"Convert base\" that won't be a matter\n  at all."
                                                " \n\n• Before using the program you should know that, \n\n"
                                                "  • Ternary number system uses 3 digits which are 0, 1, 2\n\n"
                                                "  • Quaternary number system uses 4 digits which are 0, 1, 2, 3\n\n"
                                                "  • Quinary number system uses 5 digits which are 0, 1, 2, 3, 4\n\n"
                                                "  • Senary number system uses 6 digits which are 0, 1, 2, 3, 4, 5\n\n"
                                                "  • Septenary number system uses 7 digits which are 0, 1, 2, 3, 4, 5, 6")
backButton = ttk.Button(master=frame_help, text="Back", command=help_user, bootstyle=(OUTLINE, Back))

# frame help layouts
label1.place(relx=0.5, rely=0.1, anchor="center")
label2.place(relx=0.5, rely=0.7, anchor="center")
labelDetails.place(anchor="center", relx=0.5, rely=0.4)
backButton.place(anchor="center", relx=0.9, rely=0.8)

# grid configure
app.columnconfigure(0, weight=1)
app.rowconfigure((0, 1, 2, 3, 4), weight=1)

# widgets layouts in app
help_btn.place(relx=0.91, rely=0.95)
how_to.place(relx=0.01, rely=0.95)
settingsBTN.place(relx=0.80, rely=0.95)
OtherMenuButton.place(relx=0.01, rely=0.01)

# frame layouts
frame.grid(row=1, column=0, sticky=NSEW, padx=50)

if currentAppearance == "Tiles":
    frame_btns.rowconfigure((0, 1), weight=1, uniform="a")
    frame_btns.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

    # widgets layouts in frame_btns
    btn_binary.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
    btn_decimal.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)
    btn_octal.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)
    btn_hex.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
    btn_ternary.grid(row=0, column=4, sticky=NSEW, padx=5, pady=5)
    btn_quaternary.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
    btn_quinary.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)
    btn_senary.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)
    btn_septenary.grid(row=1, column=3, sticky=NSEW, padx=5, pady=5)
    btn_base.grid(row=1, column=4, sticky=NSEW, padx=5, pady=5)
    frame_btns.grid(row=2, column=0, sticky=NSEW, rowspan=2, padx=40, pady=20)
else:
    btn_ternary = ttk.Button(frame_btns, text="T\ne\nr\nn\na\nr\ny", bootstyle=(TernaryBTN, OUTLINE), command=convert_any_number_system_to_ternary)
    btn_quaternaryart = ttk.Button(frame_btns, text="Q\nu\na\nt\ne\nr\nn\na\nr\ny", bootstyle=(SUCCESS, OUTLINE), command=convert_any_number_system_to_quaternary)
    frame_btns.place(relx=0.5, rely=0.71, relheight=0.4, relwidth=0.85, anchor="center")

    # widget layout
    btn_hex.place(relx=0.0, rely=0.4, relwidth=0.4, relheight=0.6)
    btn_decimal.place(relx=0.0, rely=0.0, relheight=0.4, relwidth=0.2)
    btn_octal.place(relx=0.2, rely=0.0, relheight=0.4, relwidth=0.2)
    btn_quaternaryart.place(relx=0.4, rely=0.0, relwidth=0.1, relheight=1.0)
    btn_binary.place(relx=0.69, rely=0.17, relheight=0.33, relwidth=0.4, anchor="center")
    btn_senary.place(relx=0.69, rely=0.5, relheight=0.33, relwidth=0.4, anchor="center")
    btn_baseart.place(relx=0.832, rely=0.82, relheight=0.09, relwidth=0.093)
    btn_septenary.place(relx=0.69, rely=0.83, relheight=0.33, relwidth=0.4, anchor="center")
    btn_ternary.place(relx=1.0, rely=0.0, relheight=1.0, relwidth=0.11, anchor="ne")

# widgets layouts in frame
label_num.grid(row=0, column=1, sticky=SW, padx=5)
entry_num.grid(row=1, column=1, sticky=NE, padx=5)
label_base.grid(row=0, column=2, sticky=SW, padx=5)
entry_base.grid(row=1, column=2, sticky=NE, padx=5)
label_entry.grid(row=1, column=1, sticky=SE, pady=5)
entry_con_base.place(relx=0.51, rely=0.4)
btn.grid(row=2, column=1, columnspan=2, sticky=NSEW, pady=10)

# outOfTheBlue
frame0 = ttk.Frame(app, bootstyle=(DANGER))
frame1 = ttk.Frame(app, bootstyle=(WARNING))
frame2 = ttk.Frame(app, bootstyle=(SUCCESS))
frame3 = ttk.Frame(app, bootstyle=(LIGHT))
frame4 = ttk.Frame(app, bootstyle=(INFO))

frame0.place(relx=rel_X0, rely=0.05, relwidth=0.7, relheight=0.1)
frame1.place(relx=(rel_X0+1.2), rely=0.25, relwidth=0.7, relheight=0.1)
frame2.place(relx=(rel_X0+2.2), rely=0.45, relwidth=0.7, relheight=0.1)
frame3.place(relx=(rel_X0+3.2), rely=0.65, relwidth=0.7, relheight=0.1)
frame4.place(relx=(rel_X0+4.2), rely=0.85, relwidth=0.7, relheight=0.1)


app.mainloop()
