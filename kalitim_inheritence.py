class univercity():
    def __init__(self):
        self.FirstName = []
        self.LastName = []
        self.UnivercityNo = [],
    def information(self):
        print("İsim : ",self.FirstName, "\nSoyisim : ",self.LastName, "\nNo : ",self.UnivercityNo)

class Elektrical(univercity):
    def __init__(self):
        self.Lab_information = []
    def kinf_of(self):
        print("Labaratuar bilgileri : ", self.Lab_information)
class ibf(univercity):
    def __init__(self):
        self.Language = []

t = Elektrical()
t.FirstName = "Ahmet"
t.LastName = "Ekici"
t.UnivercityNo = 151106203013
t.Lab_information = "Hepsi alinmistir."

k = ibf()
k.Language = "İngilizce"
k.FirstName = "Ayşe"
k.LastName = "Cambaz"
k.UnivercityNo = 150106203011
t.Lab_information = " Hepsi alınmamıştır."
t.information()
t.kinf_of()

