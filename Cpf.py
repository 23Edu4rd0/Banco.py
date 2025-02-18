from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.Cpf_Valido(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF Invalido!!!")
        
    def __str__(self):
        return self.Cpf_Formatado()

    def Cpf_Valido(self, cpf):
        cpf_validator = CPF()
        return cpf_validator.validate(cpf)

    def Cpf_Formatado(self):
        cpf_validator = CPF()
        return cpf_validator.mask(self.cpf)

class DataNascimento:
    def __init__(self, data):
        data = str(data)
        if self.Data_Validada(data):
            self.data = data
        else:
            raise ValueError("Data Invalida!!!")
        
    def __str__(self):
        return self.Data_Formatada()
    
    def Data_Validada(self, data):
        if len(data) != 8:
            return False
        else:
            return True
        
    def Data_Formatada(self):
        fatia_um = self.data[:2]
        fatia_dois = self.data[2:4]
        fatia_tres = self.data[4:]
        return "{}/{}/{}".format(fatia_um, fatia_dois, fatia_tres)