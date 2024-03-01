class Calculatrice:
    """Paramètres :
    à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    def __init__(self,x):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        self.x=x
        
    def __add__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        return self.x + autre.x
    
    def __sub__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        
        return self.x - autre.x
    
    def __mul__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        return self.x * autre.x
    
    def __div__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        return self.x/autre.x
    

    def calculer(self,choix):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        while choix!="quitter":
            if choix=='addition':
                autre=Calculatrice(int(input("Entrez un nombre pour l'addition:")))
                print(input(f"La somme de {self.x} et {autre.x} vaut: {self.x+autre.x}"))
            elif choix=='soustraction':
                autre=Calculatrice(int(input("Entrez un nombre pour la soustraction:")))
                print(input(f"La différence entre {self.x} et {autre.x} vaut : {self.x-autre.x}"))
            elif choix == 'multiplication':
                autre=Calculatrice(int(input("Entrez un nombre pour la multiplication:")))
                print(input(f"Le produit de {self.x} et {autre.x} vaut : {self.x*autre.x}"))
            elif choix =='division':
                autre=Calculatrice(int(input("Entrez un nombre pour la division:")))
                print(input(f"La division vaut :{self.x/autre.x}")).lower()
            else:
                print("Cette opération n'est pas disponible. Veuillez essayer une autre opération.")
            choix=input("Veuillez choisir une opération (addition/soustractio/multiplication/division)").lower()

num1=Calculatrice(2)
operation= input("Choisissez une opération (addition/soustraction/multiplication/division/quitter) : ").lower()

num1.calculer(operation)

