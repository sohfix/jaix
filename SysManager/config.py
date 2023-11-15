import configparser

config = configparser.ConfigParser()
config.read("example.ini")

# Accessing values
section = "SectionName"
option = "OptionName"
value = config[section][option]
print(value)

# Adding a section and some values
config["SectionName"] = {"OptionName1": "value1", "OptionName2": "value2"}

# Writing to a file
with open("example.ini", "w") as configfile:
    config.write(configfile)

# Modifying a value
config["SectionName"]["OptionName1"] = "NewValue"

# Saving the changes
with open("example.ini", "w") as configfile:
    config.write(configfile)
