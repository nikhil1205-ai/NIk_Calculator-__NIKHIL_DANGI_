import pandas as pd
import numpy as np
from numpy import *
import sympy as sy
from sympy import *
import scipy
import regex
import streamlit as st

def lower_of_xyza(func_text):
    func_text_m=func_text
    if "X" in func_text:
       func_text_m=func_text.replace("X","x")
    if "Y" in func_text:
        func_text_m=func_text.replace("Y","y")
    if "Z" in func_text:
        func_text_m=func_text.replace("Z","z")
    if "A" in func_text:
        func_text_m=func_text.replace("A","a")
    return func_text_m

class SimpleIntegral:
    def __init__ (self,var):
       self.var=sy.Symbol(var)

    def S_limit_func(self,func_text):
        func_text=lower_of_xyza(func_text)
        try:
            if "^" in func_text:
                      func_text = func_text.replace('^', '**')
            if "|" in func_text:
                l=func_text.split("|")
                for i in range(1,int(len(l)/2)+1):
                    l[i]="abs("+ l[i]
                    l[-1-i]=l[-1-i]+")"
                func_text="".join(l)
            if "π" in func_text:
                func_text = func_text.replace('π', 'pi')
            if "ln" in func_text:
                func_text = func_text.replace('ln', 'log')
            elif "log" in func_text:
                func_text = func_text.replace('log', 'log10')
            if "sinI" in func_text or "cosI" in func_text or "tanI" in func_text:
                if "sinI" in func_text:
                   func_text = func_text.replace('sinI', 'arcsin')
                if "cosI" in func_text:
                   func_text = func_text.replace('cosI', 'arccos') 
                if "tanI" in func_text:
                   func_text = func_text.replace('tanI', 'arctan')  
                
            return True,eval(func_text)
        except:
              return  False,st.error(f"Please Give function except:-   {func_text}", icon="🚨")
        
    def S_No_limit_func(self,func_text):
        func_text=lower_of_xyza(func_text)
        try :
             if "^" in func_text:
                  func_text = func_text.replace('^', '**')
             if "π" in func_text:
                func_text = func_text.replace('π', 'pi')
             if "e" in func_text:
                  if f"e**{self.var}" in func_text:
                      func_text=func_text.replace(f"e**{self.var}",f"exp({self.var})")
                      
                  elif f"e**" in func_text:
                      pattern = r"e\*\*\(([^)]+)\)"
                      func_text = regex.sub(pattern, r"exp(\1)", func_text)
                  else:
                      e=sy.Symbol("e")
                      func_text = func_text.replace('e',f"{e}")        
             if "|" in func_text:
                l=func_text.split("|")
                for i in range(1,int(len(l)/2)+1):
                    l[i]=""+ l[i]
                    l[-1-i]=l[-1-i]+""
                func_text="".join(l)            
             if "sinI" in func_text or "cosI" in func_text or "tanI" in func_text:
                if "sinI" in func_text:
                   func_text = func_text.replace('sinI', 'asin')
                if "cosI" in func_text:
                   func_text = func_text.replace('cosI', 'acos') 
                if "tanI" in func_text:
                   func_text = func_text.replace('tanI', 'atan')  
             return sy.simplify(func_text)
        except:
             return st.error(f"Please Give function except:-   {func_text}", icon="🚨")
    
    def Calculate_Integral(self,func,llim,hlim):
            try:             
                integ_wthout_limit = sy.integrate(func,self.var)
                format_wthout_limit = sy.Integral(func,(self.var,llim,hlim))
                format_limit = sy.Integral(func,self.var)
                return integ_wthout_limit,format_wthout_limit,format_limit
            except :
                try:
                   deri_wth_limit=scipy.integrate.quad(func,llim,hlim)
                   return deri_wth_limit
                except Exception as e:                 
                    if llim==0 or hlim==0:
                       deri_wth_limit=scipy.integrate.quad(func,llim+0.000001,hlim+0.000001)
                       return deri_wth_limit

     
  
class DoubleIntegral(SimpleIntegral):
    def __init__ (self,var0,var1):
       self.var0,self.var1 = sy.symbols(f"{var0} {var1}")
    
    def Intersection_point_l(self,No_limit_func1,No_limit_func2):
        eq1 = sy.Eq(self.var1, No_limit_func1)
        eq2 = sy.Eq(self.var0, No_limit_func2)
        solutions = sy.solve([eq1, eq2], (self.var1,self.var0))
        solutions=[list(i) for i in solutions]
        point_list=[]
        for i in solutions:
           l=[]
           for j in i:
             try: 
              l.append(float(round(eval(str(j)),3)))
             except :
                 break
           if len(l) != 0:
                point_list.append(l)
        return point_list
    
    def Calculate_D_Integral(self,X_low_limit,X_high_limit,point1,point2,var_first,var_second):     
         integral = sy.Integral(1, (sy.symbols(f"{var_first}"), X_low_limit, X_high_limit), (sy.symbols(f"{var_second}"), point1, point2))
         Integration_value = sy.integrate(1, (sy.symbols(f"{var_first}"), X_low_limit, X_high_limit), (sy.symbols(f"{var_second}"), point1, point2))
         return integral,Integration_value