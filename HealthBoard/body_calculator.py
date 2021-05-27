
BMI = 0
class Parameters:


    def __init__(self, height, weight, age, gender, waist):
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.waist = waist
        
    
    # Body Lean Mass function
    def Lean_Body_Mass(self):
        if self.gender == "man": 
            BLM = (0.3281 * self.weight) + (0.33929 * self.height) - 29.5336
            return round(BLM,2) 
        
        if self.gender == "woman":
            BLM = (0.29569 * self.weight) + (0.41813 * self.height) - 43.2933
            return round(BLM,2) 
        
    # Body Mass Index function
    def Body_Mass_Index(self):
        
        global BMI
        BMI = self.weight / (self.height / 100) **2 
        return round(BMI,2)

    
    # Body Fat Percentage 
    def Body_Fat_Percentage(self):

        if self.gender == "man":
            BFP = 1.20 * BMI + 0.23 * self.age - 16.2
            if self.age <= 15:
                BFP = 1.51 * BMI - 0.70 * self.age - 2.2
            return round(BFP,2) 
        
        
        if self.gender == "woman":
            BFP = 1.20 * BMI + 0.23 * self.age - 5.4
            if self.age <= 15:
                 BFP = 1.51 * BMI - 0.70 * self.age + 1.4
            return round(BFP,2) 

        
    # Basal Metabolic Rate
    def Basal_Metabolic_Rate (self): 
        s = 0
        
        if self.gender == "man":
            s =+ 5
        if self.gender == "woman":
            s =- 161
        
        BMR = (self.weight * 10 ) + (self.height * 6.25) - (self.age * 5) + s 
        return round(BMR,2) 
        

if __name__ == "__main__":
    
    user = Parameters(
        float(input('Height: ')),
        float(input('Weight: ')),
        float(input('Age: ')),
        float(input('Sex (0 = mens / 1 = womens): ')),
        float(input('Waist: '))
    )

    print('Body Lean Mass:',user.Lean_Body_Mass())
    print('Body Mass Index:',user.Body_Mass_Index())
    print('Body Fat Percentage:',user.Body_Fat_Percentage())  
    print('Basal Metabolic Rate:',user.Basal_Metabolic_Rate())


    