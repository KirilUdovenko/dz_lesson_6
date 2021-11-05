# def create_domains(domains):
#     list_str = domain_name
#     return list_str
#
# with open("domains.txt", "r") as txt_file:
#     domains = txt_file.read()
#     domain_name = domains.replace(".", '')
# list_str = create_domains(domains)
# print(list_str)
#

##############
import re
# def name_file(names):



with open("names.txt", "r") as txt_file:
    name = txt_file.read()
    str_1 = ''.join(name)
    # numbers = re.findall(r"[0-9]+", str_1)
    str_2 = re.sub(r'[^\w\s]+|[\d]+', r'', str_1).strip().split("\n")
    print(str_2)
with open("names_2.txt", "w") as txt_file:
    txt_file.writelines(str_2)
with open("names_2.txt", "r") as txt_file:
    second_name = txt_file.readlines()


