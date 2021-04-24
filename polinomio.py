import math

class Polinomio:
    def __init__(self, coefs, grado):
        """
        coefs: Coeficientes del polinomio, se deben pasar de menor
               a mayor grado.
        grado: Grado del polinomio
        """
        self.coefs = coefs
        self.grado = grado
        self.deriv = []
        self.long_arc = 0

    def obtener_deriv(self):
        return self.__deriv()

    def __deriv(self):
        """
        Calcula los coeficientes de la derivada del polinomio
        """
        if not self.deriv:
            # Deriva cada término y coloca el 
            # coeficiente en la lista d_coeficientes
            for i in range(1, len(self.coefs)):
                self.deriv.append(self.coefs[i]*i)

        return self.deriv

    def evaluar(self, x):
        """
        Evaluar polinomio por Horner. \n
        x: Valor a evaluar en el polinomio. 
        """
        p_x = self.coefs[self.grado]
        k = self.grado - 1
        while (k >= 0):
            p_x = self.coefs[k] + (p_x * x)
            k = k - 1

        # P(x)
        return p_x

    def evaluar_deriv(self, x):
        """
        Evaluar derivada del polinomio por Horner. \n
        x: Valor a evaluar en el polinomio. 
        """
        self.__deriv()

        p_x = self.deriv[self.grado-1]
        k = self.grado - 2
        while (k >= 0):
            p_x = self.deriv[k] + (p_x * x)
            k = k - 1

        # P(x)
        return p_x

    def long_arc_trapecio(self, a, b, tol):
        """
        Calcula la longitud de arco del polinomio en el intervalo cerrado [a,b] \n
        por medio del método del trapecio. \n
        a: Inicio del intervalo. \n
        b: Fin del intervalo. \n
        tol: Tolerancia al error relativo normalizado porcentual ERNP. \n
        """    
        n = 1
        valor_actual = 0
        valor_anterior = 0
        ernp = 1

        while ernp >= tol:
            delta = (b-a)/n
            valor_actual = math.sqrt(1 + math.pow(self.evaluar_deriv(a), 2))

            for i in range(1, n):
                valor_actual += 2*math.sqrt(1 + 
                               math.pow(self.evaluar_deriv(a + i*delta), 2))

            valor_actual += math.sqrt(1+ math.pow(self.evaluar_deriv(b), 2))
            valor_actual = delta*valor_actual/2


            ernp = abs((valor_actual - valor_anterior)/valor_actual)
            valor_anterior = valor_actual
            n *= 2

        return valor_actual, n

    def long_arc_simpson13(self, a, b, tol):
        """
        Calcula la longitud de arco del polinomio en el intervalo cerrado [a,b] \n
        por medio de la regla de Simpson 1/3. \n
        a: Inicio del intervalo. \n
        b: Fin del intervalo. \n
        tol: Tolerancia al error relativo normalizado porcentual ERNP. \n
        """    
        n = 2
        valor_actual = 0
        valor_anterior = 0
        ernp = 1

        while ernp >= tol:
            delta = (b-a)/n
            valor_actual = math.sqrt(1 + math.pow(self.evaluar_deriv(a), 2))

            for i in range(1, n-1, 2):
                valor_actual += 4*math.sqrt(1 + 
                               math.pow(self.evaluar_deriv(a + i*delta), 2)) + 2*math.sqrt(1 + 
                               math.pow(self.evaluar_deriv(a + (i+1)*delta), 2))

            valor_actual += 4*math.sqrt(1 + 
                            math.pow(self.evaluar_deriv(a + (n-1)*delta), 2)) + math.sqrt(1 + 
                            math.pow(self.evaluar_deriv(b), 2))

            valor_actual = delta*valor_actual/3

            ernp = abs((valor_actual - valor_anterior)/valor_actual)
            valor_anterior = valor_actual
            n *= 2

        return valor_actual, n

    def __str__(self):
        cadena = ""

        # Termino independiente
        if self.coefs[0] != 0:
            cadena += f"{self.coefs[0]}"

        if self.grado > 0:
                cadena += " + "

        for i in range(1, len(self.coefs)):
            if self.coefs[i] != 0:           
                if i != 1:
                    cadena += f"{self.coefs[i]}x^{i}"
                else:
                    cadena += f"{self.coefs[i]}x"

                if i != self.grado:
                    cadena += " + "

        return cadena

            

    
