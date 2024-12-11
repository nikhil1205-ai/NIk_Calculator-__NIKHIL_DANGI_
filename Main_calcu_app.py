import streamlit as st
import sympy as sy
import Main_calcu_plot
import Main_calculation
import Main_support


st.set_page_config(
    page_title="Nik Calculator",
    layout="wide",
    initial_sidebar_state="expanded")

st.sidebar.title("Nik Calculator 📟📟")
st.sidebar.write("")
category=st.sidebar.selectbox(label="Types of Calculation",options=("Select on this","Integral"))

if category=="Integral":
   st.sidebar.write("")
   sub_cate=st.sidebar.selectbox("Types of Calculation",("Select integral type","Simple-Integral","Double-Integral","Triple-Integral"))

   if sub_cate=="Simple-Integral":
           st.sidebar.write("")
           var=st.sidebar.segmented_control("Choose Variable",options=["x","y","z","a"],selection_mode="single")
           if var in ["x","y","z","a"]:
             SI=Main_calculation.SimpleIntegral(var)
             func_text=st.sidebar.text_input(f"Enter cool function in :red[{var}] Term 👇 ")
             if func_text!="":
                check,limit_func=SI.S_limit_func(f"lambda {var}:"+func_text)
                No_limit_func=SI.S_No_limit_func(func_text)

                if check:
                     llim,hlim=st.sidebar.slider(label="Select limit of function",min_value=-100, max_value=100, value=(0,8),key=256)
                     llim=st.sidebar.number_input(label="Enter The Lower Limit",value=float(llim),key=124)
                     hlim=st.sidebar.number_input(label="Enter The High limit",value=float(hlim),key=451)
                     with st.container():                  
                        st.plotly_chart(Main_calcu_plot.SimpleIntegrateplot(limit_func,llim,hlim))
                     
                     
                     no_limit_integ,format_witout_limit,format_limit=SI.Calculate_Integral(No_limit_func,llim,hlim)
                     limit_integ=SI.Calculate_Integral(limit_func,llim,hlim)[0]
                     Main_support.progress_bar()
                     col1, col2,col3= st.columns([2,0.5,2],gap="small")
                     with col1:
                        st.write(format_limit)
                        st.divider()
                        st.write(format_witout_limit)
         
                     with col3:
                        st.write(no_limit_integ)
                        st.divider()
                        st.write("")
                        st.write("")
                        st.write(f"### :green[{limit_integ}]")  


   if sub_cate=="Double-Integral":
      sub_cate=st.sidebar.selectbox("Types of Calculation",("Select function type","y=X^2 , x=Y^2","f(x,y)=X^2+Y^2","x^2+y^2=0"))

      if sub_cate=="y=X^2 , x=Y^2":
         var=st.sidebar.segmented_control("Select variable ",["x","y","z"],selection_mode="multi")
         if len(var)!=0:
            func1_text=st.sidebar.text_input(f"Enter cool function in :red[{var[0]}] Term 👇",key=123)
         if len(var)>1:
            func2_text=st.sidebar.text_input(f"Enter cool function in :red[{var[1]}] Term 👇",key=478)
            DI=Main_calculation.DoubleIntegral(var[0],var[1])
            if func1_text!="" and func2_text!="":
                     check,d_limit_func1=DI.S_limit_func(f"lambda {var[0]}:"+func1_text)
                     check1,d_limit_func2=DI.S_limit_func(f"lambda {var[1]}:"+func2_text)
                     No_limit_func1=DI.S_No_limit_func(func1_text)
                     No_limit_func2=DI.S_No_limit_func(func2_text)
                     
                     if check and check1:
                           llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-90,90),key=256)
                           with st.container():             
                              st.plotly_chart(Main_calcu_plot.doubleIntegrateplot(d_limit_func1,d_limit_func2,llim,hlim),use_container_width=False)               
                           
                           to_respect=st.sidebar.segmented_control("To respect want First Integration ",["dx","dy","dz"],selection_mode="single")
                           if to_respect!=None:
                                 var_first=Main_support.to_respect_first_second(to_respect)
                                 var_second=[var[1] if var[0]==var_first else var[0]][0]
                                 solve_points=DI.Intersection_point_l(No_limit_func1,No_limit_func2) 
                                 col1, col2 = st.columns(2)
                                 
                                 low_limit = st.sidebar.text_input(f"Low Limit in :red[{var_second}] Term", placeholder="Enter text here")
                                 high_limit = st.sidebar.text_input(f"High Limit in :red[{var_second}] Term", placeholder="Enter text here")
                                 if low_limit!="" and high_limit!="":
                                    X_low_limit=DI.S_No_limit_func(low_limit)
                                    X_high_limit=DI.S_No_limit_func(high_limit)
                                    points=st.sidebar.segmented_control(f"Choose :red[d{var_second}] limits",[f"{i}" for i in solve_points],
                                                                        selection_mode="multi")
                                    if len(points)>1:

                                       point1,point2=(eval(points[0]),eval(points[1]))
                                       if var_second=="x" or var_first=="z":
                                          integral,integration_value=DI.Calculate_D_Integral_X_y(X_low_limit,X_high_limit,point1[0],point2[0],var_first,var_second)
                                       if var_second=="y" or var_second=="z":
                                          integral,integration_value=DI.Calculate_D_Integral_X_y(X_low_limit,X_high_limit,point1[1],point2[1],var_first,var_second)
                                       Main_support.progress_bar()                     
                                       st.write(integral,unsafe_allow_html=True)
                                       st.write("")
                                       st.write("")
                                       st.write("#### :blue[Integration value is:]",integration_value)
      if sub_cate=="f(x,y)=X^2+Y^2":
         var=st.sidebar.segmented_control("Given variable ",["x","y","z"],selection_mode="multi")
         if len(var)>1:
            func_text=st.sidebar.text_input(f"Enter cool function in :red[{var[0],var[1]}]👇 Term",key=123)
            DI=Main_calculation.DoubleIntegral(var[0],var[1])
            if func_text!="":
                  check,d_limit_func=DI.S_limit_func(f"lambda {var[0]},{var[1]}:"+func_text)
                  d_No_limit_func=DI.S_No_limit_func(func_text)
                  llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-30,30),key=256)
                  with st.container():            
                     st.plotly_chart(Main_calcu_plot.doubleIntegrate_Fxy_plot(d_limit_func),use_container_width=False)               
                  to_respect=st.sidebar.segmented_control("To respect want First Integrationt ",["dx","dy","dz"],selection_mode="single")
                  if to_respect!=None:
                              var_first=Main_support.to_respect_first_second(to_respect)
                              var_second=[var[1] if var[0]==var_first else var[0]][0]

                              low_limit_func_var0 = st.sidebar.text_input(f"Low Limit in :red[{var_second}] Term", placeholder="Enter text here")
                              high_limit_func_var0  = st.sidebar.text_input(f"High Limit in :red[{var_second}] Term", placeholder="Enter text here")
                              st.sidebar.divider()
                              low_limit_func_var1 = st.sidebar.text_input(f"Low Limit of :red[d{var_second}] ", placeholder="Enter text here")
                              high_limit_func_var1  = st.sidebar.text_input(f"High Limit in :red[d{var_second}] ", placeholder="Enter text here")                     
                              if high_limit_func_var0!="" and high_limit_func_var1!="":
                                 X_low_limit=DI.S_No_limit_func(low_limit_func_var0)
                                 X_high_limit=DI.S_No_limit_func(high_limit_func_var0)
                     
                                 integral,integration_value=DI.Calculate_D_Integral_Fxy(d_No_limit_func,low_limit_func_var0,high_limit_func_var0,
                                                                                    low_limit_func_var1,high_limit_func_var1,var_first,var_second)  
                                 Main_support.progress_bar()                               
                                 st.write(integral,unsafe_allow_html=True)
                                 st.write("")
                                 st.write("")
                                 st.write("#### :blue[Integration value is:]",integration_value)
      
      if sub_cate=="x^2+y^2=0":
         var=st.sidebar.segmented_control("Given variable ",["x","y","z"],selection_mode="multi")
         if len(var)>1:
            equa_text=st.sidebar.text_input(f"Enter cool Equation in :red[{var[0],var[1]}]👇 Term",key=123)
            DI=Main_calculation.DoubleIntegral(var[0],var[1])
            if equa_text!="":
               llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-30,30),key=256)
               #with st.container():             
                  #st.plotly_chart(Triple_plot.doubleIntegrateplot(d_limit_func1,d_limit_func2,llim,hlim))          
                 
               to_respect=st.sidebar.segmented_control("To respect want First Integrationt ",["dx","dy","dz"],selection_mode="single")
               if to_respect!=None:
                     var_first=Main_support.to_respect_first_second(to_respect)
                     var_second=[var[1] if var[0]==var_first else var[0]][0]
                     solution_var0=DI.Equation_Function_var0(equa_text,var_first,var_second)
                     try:
                        var0_limit1,var0_limit2=st.sidebar.segmented_control(f"Choose d{var_first} Low to High Limit",[i for i in solution_var0],selection_mode="multi")
                     except:
                         var0_limit1,var0_limit2=("","")
                     low_limit_func_var0 = st.sidebar.text_input(f"Low Limit in :red[{var_second}] Term", placeholder="Enter text here",value=var0_limit1)
                     high_limit_func_var0  = st.sidebar.text_input(f"High Limit in :red[{var_second}] Term", placeholder="Enter text here",value=var0_limit2)
                     if low_limit_func_var0!="" and high_limit_func_var0!="":
                        st.sidebar.divider()
                        Low_limit_func_var1,high_limit_func_var1=DI.Equation_Function_var1(low_limit_func_var0,high_limit_func_var0,var_first,var_second)
                        var1_low_limit=st.sidebar.segmented_control(f"Choose d{var_second} Low Limit",[i for i in Low_limit_func_var1],selection_mode="single",key=154)
                        var1_high_limit=st.sidebar.segmented_control(f"Choose d{var_second} high Limit",[i for i in high_limit_func_var1],selection_mode="single")
                        low_limit_func_var1 = st.sidebar.text_input(f"Low Limit of :red[d{var_second}] ",value=var1_low_limit, placeholder="Enter text here")
                        high_limit_func_var1  = st.sidebar.text_input(f"High Limit in :red[d{var_second}] ",value=var1_high_limit, placeholder="Enter text here")                     
                        if low_limit_func_var1!="" and high_limit_func_var1!="":
                          var0_low_limit=DI.S_No_limit_func(low_limit_func_var0)
                          var0_high_limit=DI.S_No_limit_func(high_limit_func_var0)           
             
                          integral,integration_value=DI.Calculate_D_Integral_fequal_Xy(
                              var0_low_limit,var0_high_limit,low_limit_func_var1,
                              high_limit_func_var1,var_first,var_second)     

                          Main_support.progress_bar()                            
                          st.write(integral,unsafe_allow_html=True)
                          st.write("")
                          st.write("")
                          st.write("#### :blue[Integration value is:]",integration_value)

   if sub_cate=="Triple-Integral":          
      sub_cate=st.sidebar.selectbox("Types of Calculation",("Select function type","f(x,y,z)=X^2+Y^2+Z^2","x^2+y^2+z^2=0"))
      if sub_cate=="f(x,y,z)=X^2+Y^2+Z^2":
         var=st.sidebar.segmented_control("Given variable ",["x","y","z"],selection_mode="multi")
         if len(var)>2:
            func_text=st.sidebar.text_input(f"Enter cool function in :red[{var[0],var[1],var[2]}]👇 Term",key=123)
            TI=Main_calculation.TripleIntegral(var[0],var[1],var[2])
            if func_text!="":
                  #check,d_limit_func=DI.S_limit_func(f"lambda {var[0]},{var[1],var[2]}:"+func_text)
                  d_No_limit_func=TI.S_No_limit_func(func_text)
                  llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-30,30),key=256)
                  #with st.container():            
                     #st.plotly_chart(Main_calcu_plot.doubleIntegrate_Fxy_plot(d_limit_func),use_container_width=False) 
                                   
                  to_respect_f=st.sidebar.segmented_control("To respect want First Integrationt ",["dx","dy","dz"],selection_mode="single",key=124)
                  to_respect_s=st.sidebar.segmented_control("To respect want Second Integrationt ",["dx","dy","dz"],selection_mode="single")
                  if to_respect_f!=None and to_respect_s!=None:
                              var_first=Main_support.to_respect_first_second(to_respect_f)
                              var_second=Main_support.to_respect_first_second(to_respect_s)
                              var_third=None
                              if var_first == var[0] and var_second == var[1]:
                                    var_third=var[2]
                              elif var_first == var[0] and var_second == var[2]:
                                    var_third=var[1]
                              elif var_first == var[1] and var_second == var[2]:
                                    var_third=var[0]  
                              low_limit_func_var0 = st.sidebar.text_input(f"Low Limit in :red[{var_second} of d{var_first}] Term", placeholder="Enter text here",key=111)
                              high_limit_func_var0  = st.sidebar.text_input(f"High Limit in :red[{var_second} of d{var_first}] Term", placeholder="Enter text here",key=112)
                              st.sidebar.divider()
                              low_limit_func_var1 = st.sidebar.text_input(f"Low Limit in :red[{var_third} of d{var_second}] Term", placeholder="Enter text here",key=121)
                              high_limit_func_var1  = st.sidebar.text_input(f"Low Limit in :red[{var_third} of d{var_second}] Term", placeholder="Enter text here",key=122)
                              st.sidebar.divider()
                              low_limit_func_var2 = st.sidebar.text_input(f"Low Limit of :red[d{var_third}] Term", placeholder="Enter text here",key=211)
                              high_limit_func_var2  = st.sidebar.text_input(f"Low Limit of :red[d{var_third}] Term", placeholder="Enter text here",key=222)                
                              if low_limit_func_var0!="" and high_limit_func_var2!="":
                                  var0_low_limit=TI.S_No_limit_func(low_limit_func_var0)
                                  var0_high_limit=TI.S_No_limit_func(high_limit_func_var0)

                                  var1_low_limit=TI.S_No_limit_func(low_limit_func_var1)
                                  var1_high_limit=TI.S_No_limit_func(high_limit_func_var1)

                                  var2_low_limit=TI.S_No_limit_func(low_limit_func_var2)
                                  var2_high_limit=TI.S_No_limit_func(high_limit_func_var2)
                     
                                  integral,integration_value=TI.Calculate_T_Integral_Fxy(d_No_limit_func,var0_low_limit,var0_high_limit,
                                                                     var1_low_limit,var1_high_limit,var2_low_limit,var2_high_limit,var_first,var_second,var_third)  
                                  Main_support.progress_bar()                               
                                  st.write(integral,unsafe_allow_html=True)
                                  st.write("")
                                  st.write("")
                                  st.write("#### :blue[Integration value is:]",integration_value)
