web_development = ["Asha", "Akash", "Renjini"]
data_science = ["Arun", "Sumi", "Mekha"]
ui_ux = ["Archa", "Ganesh", "Nazim"]
print(web_development)
print(data_science)
print(ui_ux)

all_participants = [[web_development], [data_science], [ui_ux]]
print(all_participants)

web_development.append("Rony")
print(web_development)

data_science.insert(1, "Thanseer")
print(data_science)

ui_ux.pop()
print(ui_ux)

new_data_science = data_science.copy()
print(new_data_science)
data_science.clear()
print(data_science)

print(new_data_science[:2])

len_names = [len(x) for x in new_data_science]
print(len_names)

#Check whether “Asha” is in any of the workshop lists.
if "Asha" in web_development:
    print("Asha is in Web Development")
    
if "Asha" in new_data_science:
    print("Asha is in Data Science")
    
if "Asha" in ui_ux:
    print("Asha is in UI/UX")
    
workshop_tuple = (web_development[0], new_data_science[0], ui_ux[0])
print(workshop_tuple)

  

