# A Project by Nathan, Mathew, Wilbert
# Imports
from time import sleep

from PIL import Image
import random

def slow_typing(sentence):
    for x in sentence:
        print(x, end="")
        sleep(0.25)


# Element Dictionary
M = ["Li","Na","K","Rb","Cs","Be","Mg","Ca","Sr","Ba","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po","At","Cu","Ag","Au","Zn","Cd",
     "Hg","Cn","Sc","Y","La","Ti","Zr","Hf","V","Nb","Ta","Cr","Mo","W","Mn","Tc","Re","Fe","Ru","Os","Co","Rh","Ir","Ni","Pd","Pt"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
electronegativity = {"H":"2.1","He":"no data","Ne":"no data","Ar":"no data","Li":"1.0","Be":"1.5","B":"2.0","C":"2.5","N":"3.0","O":"3.5","F":"4.0","Na":"0.9","Mg":"1.2","Al":"1.5",
                     "Si":"1.8","P":"2.1", "S":"2.5", "Cl":"3.0","K":"0.8","Ca":"1.0","Sc":"1.3","Ti":"1.5","V":"1.6","Cr":"1.6","Mn":"1.5","Fe":"1.8",
                     "Co":"1.8","Ni":"1.8","Cu":"1.9","Zn":"1.6","Ga":"1.6","Ge":"1.8","As":"2.0","Se":"2.4","Br":"2.8","Kr":"3.0",
                     "Rb":"0.8","Sr":"1.0","Y":"1.2","Zr":"1.4","Nb":"1.6","Mo":"1.8","Tc":"1.9","Ru":"2.2","Rh":"2.2",
                     "Pd":"2.2","Ag":"1.9","Cd":"1.7","In":"1.7","Sn":"1.8","Sb":"1.9","Te":"2.1","I":"2.5","Xe":"2.6",
                     "Cs":"0.7","Ba":"0.9","La":"1.1","Hf":"1.3","Ta":"1.5","W":"1.7","Re":"1.9","Os":"2.2","Ir":"2.2",
                     "Pt":"2.2","Au":"2.4","Hg":"1.9","Tl":"1.8","Pb":"1.8",
                     "Bi":"1.9","Po":"2.0","At":"2.2","Rn":"2.4"}
# M = Metal
# Non_M = Non-Metal
# Col = Column
Col_IA = ["H","Li","Na","K","Rb","Cs"]
Col_IIA = ["Be","Mg","Ca","Sr","Ba"]
Col_IIIA = ["B","Al","Ga","In","Tl"]
Col_IVA = ["C","Si","Ge","Sn","Pb"]
Col_VA = ["N","P","As","Sb","Bi"]
Col_VIA = ["O","S","Se","Te","Po"]
Col_VIIA = ["F","Cl","Br","I","At"]
Col_VIIIA = ["He","Ne","Ar","Kr","Xe","Rn"]
Col_IB = ["Cu","Ag","Au"]
Col_IIB = ["Zn","Cd","Hg","Cn"]
Col_IIIB = ["Sc","Y","La"]
Col_IVB = ["Ti","Zr","Hf"]
Col_VB = ["V","Nb","Ta"]
Col_VIB = ["Cr","Mo","W"]
Col_VIIB = ["Mn","Tc","Re"]
Col_VIIIB8 = ["Fe","Ru","Os"]
Col_VIIIB9 = ["Co","Rh","Ir"]
Col_VIIIB10 = ["Ni","Pd","Pt"]

running = True
print("A Project By Nathan, Mathew, Wilbert")
sleep(1)
print("Hello and welcome to the simple element Dictionary or Simulation")
sleep(1)
while running:
    print("1. Dictionary")
    print("2. Simulation")
    user_input = input("Enter the numbers of your choices: ").lower().strip()
    if user_input == "1":
        dictionary_running = True

        # Dictionary
        print("1. Col_IA                            9.  Col_IB")
        print("2. Col_IIA                           10. Col_IIB")
        print("3. Col_IIIA                          11. Col_IIIB")
        print("4. Col_IVA                           12. Col_IVB")
        print("5. Col_VA                            13. Col_VB")
        print("6. Col_VIA                           14. Col_VIB")
        print("7. Col_VIIA                          15. Col_VIIB")
        print("8. Col_VIIIA                         16. Col_VIIIB8")
        print("                                     17. Col_VIIIB9")
        print("                                     18. Col_VIIIB10")
        while dictionary_running:
            print("Type a number to explore the dictionary of element columns")
            user_input = input().lower().strip()
            if user_input == "1":
                print(Col_IA)
            elif user_input == "2":
                print(Col_IIA)
            elif user_input == "3":
                print(Col_IIIA)
            elif user_input == "4":
                print(Col_IVA)
            elif user_input == "5":
                print(Col_VA)
            elif user_input == "6":
                print(Col_VIA)
            elif user_input == "7":
                print(Col_VIIA)
            elif user_input == "8":
                print(Col_VIIIA)
            elif user_input == "9":
                print(Col_IB)
            elif user_input == "10":
                print(Col_IIB)
            elif user_input == "11":
                print(Col_IIIB)
            elif user_input == "12":
                print(Col_IVB)
            elif user_input == "13":
                print(Col_VB)
            elif user_input == "14":
                print(Col_VIB)
            elif user_input == "15":
                print(Col_VIIB)
            elif user_input == "16":
                print(Col_VIIIB8)
            elif user_input == "17":
                print(Col_VIIIB9)
            elif user_input == "18":
                print(Col_VIIIB10)
            elif user_input == "home" or user_input == "back":
                break
            else:
                print("Invalid Input")

    elif user_input == "2":
        simulation_running = True
        print("Welcome to the limited periodic table bonding simulation")
        while simulation_running:
            print("Insert 2 atoms from column IA - VIIIA or IB - VIIIB10")
            atom_1 = input("1st Atom = ").strip()
            atom_2 = input("2nd Atom = ").strip()
            if atom_1.lower() == "home" or atom_2.lower() == "home":
                break
            if atom_1 not in electronegativity or atom_2 not in electronegativity:
                print("Invalid atom input")
                continue
            electro_atom_1 = electronegativity[atom_1]
            electro_atom_2 = electronegativity[atom_2]
            if electro_atom_1 == "no data":
                print(f"The atom {atom_1} does not have data on their electronegativity, and cannot be used in this simulation")
            elif electro_atom_2 == "no data":
                print(f"The atom {atom_2} does not have data on their electronegativity, and cannot be used in this simulation")
            else:
                electro_atom_1 = float(electronegativity[atom_1])
                electro_atom_2 = float(electronegativity[atom_2])
                if (atom_1 in M and atom_2 in Non_M or atom_1 in Non_M and atom_2 in M) and abs(electro_atom_1 - electro_atom_2) >= 1.7:
                    print("This is an Ion Bond")
                    print("It occurs between a Metalic atom and a Non Metalic atom")
                    print(f"You typed {atom_1} and {atom_2}")
                    print("This bond involves giving and taking between the electrons of those atoms")
                    print("The difference in electronegativity between the two atoms is 1.7 or more")
                    print(f"{atom_1} = {electronegativity[atom_1]}, {atom_2} = {electronegativity[atom_2]}")
                    print("A molecule example of an ionic bond would be Li2O: lithium oxide")
                elif atom_1 in Non_M and atom_2 in Non_M and abs(electro_atom_1 - electro_atom_2) < 1.7:
                    print("This is a Covalent Bond")
                    print("It occurs between two Non Metalic atoms")
                    print(f"You typed {atom_1} and {atom_2}")
                    print("This bond involves the sharing of electrons between the atoms")
                    print("The difference in electronegativity between the two atoms is less than 1.7")
                    print(f"{atom_1} = {electronegativity[atom_1]}, {atom_2} = {electronegativity[atom_2]}")
                    if electro_atom_1 != electro_atom_2:
                        print("This is a Polar Covalent Bond because both atoms have a difference in electronegativity")
                    else:
                        print("This is a Non-Polar Covalent Bond because both atoms have no difference in electronegativity")
                    print("A molecule example of a covalent bond would be H2O: water")
                elif atom_1 in M and atom_2 in M:
                    print("This is a Metallic Bond")
                    print("It occurs between two Metallic atoms")
                    print(f"You typed {atom_1} and {atom_2}")
                    print("This bond involves the sharing of electrons between many metallic atoms")
                    print("The metal is held together by strong forces of attraction between delocalized electrons and positive ions")
                else:
                    print("Invalid atom or electronegativity conditions don't meet")

    elif user_input == "exit":
        # Exiting the project
        print("Thank you for using this limited dictionary and simulation")
        sleep(1)
        print("We hope you enjoyed our project")
        slow_typing("~Nathan, Mathew and Wilbert")
        exit()
    else:
        print("Invalid Input...")
        sleep(1)
