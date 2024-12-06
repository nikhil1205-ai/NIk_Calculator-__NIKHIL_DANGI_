import streamlit as st
import Main_calcu_plot
import Main_calculation
import sympy as sy
import time

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
                     
                     st.write("")
                     progress_text="☕ Take a cup of Tea ☕☕"
                     my_bar = st.progress(0, text=progress_text)
                     st.markdown('<h3 style="color:red; ">Integration of Given Function</h3>', unsafe_allow_html=True)
                     st.write("")

                     for percent_complete in range(100):
                        time.sleep(0.02)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                     time.sleep(0.5)
                     my_bar.empty()
                     
                     no_limit_integ,format_witout_limit,format_limit=SI.Calculate_Integral(No_limit_func,llim,hlim)
                     limit_integ=SI.Calculate_Integral(limit_func,llim,hlim)[0]

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


                     #st.write("Integration of ",f'''<h style="color:orange;"> { format}  </h> Without Limit :- ''',no_limit_integ,unsafe_allow_html=True)
                     #st.write("")
                     #st.write( format,limit_integ)
                     #st.write("Integration of ",f'''<h style="color:orange;"> { No_limit_func } </h> With Limit :-''',"   ",limit_integ,unsafe_allow_html=True)


   if sub_cate=="Double-Integral":
      sub_cate=st.sidebar.selectbox("Types of Calculation",("Select function type","y=X^2 , x=Y^2","f(x,y)=X^2+Y^2"))

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
                           llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-30,30),key=256)
                           with st.container():             
                              st.plotly_chart(Main_calcu_plot.doubleIntegrateplot(d_limit_func1,d_limit_func2,llim,hlim))               
                           
                           to_respect=st.sidebar.segmented_control("To respect want First Integration ",["dx","dy","dz"],selection_mode="single")
                           if to_respect!=None:
                                 to_resp_var=None
                                 if to_respect=="dx":
                                    to_resp_var="x"
                                 if to_respect=="dy":
                                    to_resp_var="y" 
                                 if to_respect=="dz":
                                    to_resp_var="z"
                                 var_first=to_resp_var
                                 var_second=[var[1] if var[0]==to_resp_var else var[0]][0]
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
                                       progress_text="Take a cup of tea ☕☕"
                                       my_bar = st.progress(0, text=progress_text)
                                       st.markdown('<h3 style="color:red; ">Integration of Given Function</h3>', unsafe_allow_html=True)
                                       st.write("")

                                       for percent_complete in range(100):
                                          time.sleep(0.02)
                                          my_bar.progress(percent_complete + 1, text=progress_text)
                                       time.sleep(0.5)
                                       my_bar.empty()

                                       point1,point2=(eval(points[0]),eval(points[1]))
                                       if var_second=="x" or var_first=="z":
                                          integral,integration_value=DI.Calculate_D_Integral_X_y(X_low_limit,X_high_limit,point1[0],point2[0],var_first,var_second)
                                       if var_second=="y" or var_second=="z":
                                          integral,integration_value=DI.Calculate_D_Integral_X_y(X_low_limit,X_high_limit,point1[1],point2[1],var_first,var_second)
                                                            
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
                  d_limit_func=DI.S_limit_func(f"lambda {var[0]},{var[1]}:"+func_text)
                  d_No_limit_func=DI.S_No_limit_func(func_text)
                  llim,hlim=st.sidebar.slider(label="Expand function Graph",min_value=-100, max_value=100, value=(-30,30),key=256)
                  #with st.container():             
                     #st.plotly_chart(Triple_plot.doubleIntegrateplot(d_limit_func1,d_limit_func2,llim,hlim))               
                  to_respect=st.sidebar.segmented_control("To respect want First Integrationt ",["dx","dy","dz"],selection_mode="single")
                  if to_respect!=None:
                              to_resp_var=None
                              if to_respect=="dx":
                                 to_resp_var="x"
                              if to_respect=="dy":
                                 to_resp_var="y" 
                              if to_respect=="dz":
                                 to_resp_var="z"
                              var_first=to_resp_var
                              var_second=[var[1] if var[0]==to_resp_var else var[0]][0]

                              low_limit_func_var0 = st.sidebar.text_input(f"Low Limit in :red[{var_second}] Term", placeholder="Enter text here")
                              high_limit_func_var0  = st.sidebar.text_input(f"High Limit in :red[{var_second}] Term", placeholder="Enter text here")
                              st.sidebar.divider()
                              low_limit_func_var1 = st.sidebar.text_input(f"Low Limit of :red[d{var_second}] ", placeholder="Enter text here")
                              high_limit_func_var1  = st.sidebar.text_input(f"High Limit in :red[d{var_second}] ", placeholder="Enter text here")                     
                              if high_limit_func_var0!="" and high_limit_func_var1!="":
                                 X_low_limit=DI.S_No_limit_func(low_limit_func_var0)
                                 X_high_limit=DI.S_No_limit_func(high_limit_func_var0)

                                 progress_text="Take a cup of tea ☕☕"
                                 my_bar = st.progress(0, text=progress_text)
                                 st.markdown('<h3 style="color:red; ">Integration of Given Function</h3>', unsafe_allow_html=True)
                                 st.write("")
                                 for percent_complete in range(100):
                                    time.sleep(0.02)
                                    my_bar.progress(percent_complete + 1, text=progress_text)
                                 time.sleep(0.5)
                                 my_bar.empty()
                     
                                 integral,integration_value=DI.Calculate_D_Integral_Fxy(d_No_limit_func,low_limit_func_var0,high_limit_func_var0,
                                                                                    low_limit_func_var1,high_limit_func_var1,var_first,var_second)                                 
                                 st.write(integral,unsafe_allow_html=True)
                                 st.write("")
                                 st.write("")
                                 st.write("#### :blue[Integration value is:]",integration_value)


