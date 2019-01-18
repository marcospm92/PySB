# MoneyCalc
# v1.1
# 31/10/2018
# Marcos Pérez Martín

# Configuration of the program. On future versions maybe a different file that
# can be changed inside program and loaded to have all variables.

# If config_by_input == 0, the values used will be the included in the code
# If config_by_input == 1, the program will ask the user to introduce the values
config_by_input = 1

if config_by_input == 0 : # config by code

    # Assign names to each different group and subgroup
    # Each group will have two different subgroups. For future versions ask how
    # many subgroups are needed inside any group
    g1 = "Group 1"
    g2 = "Group 2"
    g3 = "Group 3"
    g4 = "Group 4"
    g1_1 = "Subgroup 1 of Group 1"
    g1_2 = "Subgroup 2 of Group 1"
    g2_1 = "Subgroup 1 of Group 2"
    g2_2 = "Subgroup 2 of Group 2"
    g3_1 = "Subgroup 1 of Group 3"
    g3_2 = "Subgroup 2 of Group 3"
    g4_1 = "Subgroup 1 of Group 4"
    g4_2 = "Subgroup 2 of Group 4"

    # Assign number of people on each subgroup.
    n_g1_1 = 10
    n_g1_2 = 10
    n_g2_1 = 10
    n_g2_2 = 10
    n_g3_1 = 10
    n_g3_2 = 10
    n_g4_1 = 10
    n_g4_2 = 10

    # Assign percentage of incoming money for each group
    p_g1 = 50
    p_g2 = 50
    p_g3 = 50
    p_g4 = 50

    # Assign prize to each subgroup
    e_g1_1 = 1
    e_g1_2 = 2
    e_g2_1 = 3
    e_g2_2 = 4
    e_g3_1 = 1
    e_g3_2 = 2
    e_g4_1 = 3
    e_g4_2 = 4

else : # config by input

    # Assign names to each different group and subgroup
    # Each group will have two different subgroups. For future versions ask how
    # many subgroups are needed inside any group
    g1 = input("Enter name for group 1: ")
    g2 = input("Enter name for group 2: ")
    g3 = input("Enter name for group 3: ")
    g4 = input("Enter name for group 4: ")
    g1_1 = input("Enter name for subgroup 1 of group 1: ")
    g1_2 = input("Enter name for subgroup 2 of group 1: ")
    g2_1 = input("Enter name for subgroup 1 of group 2: ")
    g2_2 = input("Enter name for subgroup 2 of group 2: ")
    g3_1 = input("Enter name for subgroup 1 of group 3: ")
    g3_2 = input("Enter name for subgroup 2 of group 3: ")
    g4_1 = input("Enter name for subgroup 1 of group 4: ")
    g4_2 = input("Enter name for subgroup 2 of group 4: ")

    # Assign number of people on each subgroup.
    n_g1_1 = int(input("Enter number of people in subgroup 1 of group 1: "))
    n_g1_2 = int(input("Enter number of people in subgroup 2 of group 1: "))
    n_g2_1 = int(input("Enter number of people in subgroup 1 of group 2: "))
    n_g2_2 = int(input("Enter number of people in subgroup 2 of group 2: "))
    n_g3_1 = int(input("Enter number of people in subgroup 1 of group 3: "))
    n_g3_2 = int(input("Enter number of people in subgroup 2 of group 3: "))
    n_g4_1 = int(input("Enter number of people in subgroup 1 of group 4: "))
    n_g4_2 = int(input("Enter number of people in subgroup 2 of group 4: "))

    # Assign percentage of incoming money for each group
    p_g1 = int(input("Enter percentage of incoming money you earn of group 1: "))
    p_g2 = int(input("Enter percentage of incoming money you earn of group 2: "))
    p_g3 = int(input("Enter percentage of incoming money you earn of group 3: "))
    p_g4 = int(input("Enter percentage of incoming money you earn of group 4: "))

    # Assign prize to each subgroup
    e_g1_1 = int(input("Enter prize of subgroup 1 of group 1: "))
    e_g1_2 = int(input("Enter prize of subgroup 2 of group 1: "))
    e_g2_1 = int(input("Enter prize of subgroup 1 of group 2: "))
    e_g2_2 = int(input("Enter prize of subgroup 2 of group 2: "))
    e_g3_1 = int(input("Enter prize of subgroup 1 of group 3: "))
    e_g3_2 = int(input("Enter prize of subgroup 2 of group 3: "))
    e_g4_1 = int(input("Enter prize of subgroup 1 of group 4: "))
    e_g4_2 = int(input("Enter prize of subgroup 2 of group 4: "))

# ----------------------

money_g1 = (n_g1_1 * e_g1_1 + n_g1_2 * e_g1_2) * (p_g1/100)
money_g2 = (n_g2_1 * e_g2_1 + n_g2_2 * e_g2_2) * (p_g2/100)
money_g3 = (n_g3_1 * e_g3_1 + n_g3_2 * e_g3_2) * (p_g3/100)
money_g4 = (n_g4_1 * e_g4_1 + n_g4_2 * e_g4_2) * (p_g4/100)

print(f"Total {g1} for me: {money_g1} €")
print(f"Total {g2} for me: {money_g2} €")
print(f"Total {g3} for me: {money_g3} €")
print(f"Total {g4} for me: {money_g4} €")
print(f"Total for me: {money_g1+money_g2+money_g3+money_g4} €")

money_g1_pay = (n_g1_1 * e_g1_1 + n_g1_2 * e_g1_2) * ((100 - p_g1)/100)
money_g2_pay = (n_g2_1 * e_g2_1 + n_g2_2 * e_g2_2) * ((100 - p_g2)/100)
money_g3_pay = (n_g3_1 * e_g3_1 + n_g3_2 * e_g3_2) * ((100 - p_g3)/100)
money_g4_pay = (n_g4_1 * e_g4_1 + n_g4_2 * e_g4_2) * ((100 - p_g4)/100)

print(f"Total {g1} to pay: {money_g1_pay} €")
print(f"Total {g2} to pay: {money_g2_pay} €")
print(f"Total {g3} to pay: {money_g3_pay} €")
print(f"Total {g4} to pay: {money_g4_pay} €")
print(f"Total to pay: {money_g1_pay + money_g2_pay + money_g3_pay + money_g4_pay} €")
