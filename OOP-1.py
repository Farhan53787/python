class Flags:
    def __init__(self, country, color):
        self.country = country
        self.color = color

Iran = Flags("Iran", "Green, White and Red")
Bangladesh = Flags("Bangladesh", "Green and Red")
Pakistan = Flags("Pakistan", "Green and White")
Indonesia = Flags("Indonesia", "Red and White")

print("The flag of {} is made of {}".format(Iran.country, Iran.color))
print("The flag of {} is made of {}".format(Bangladesh.country, Bangladesh.color))
print("The flag of {} is made of {}".format(Pakistan.country, Pakistan.color))
print("The flag of {} is made of {}".format(Indonesia.country, Indonesia.color))