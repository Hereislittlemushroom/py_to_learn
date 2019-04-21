class Person:
    Look,Pers,Heig,Up,Do
def read_data():

def bayes():

    if(Do==1)
        c_Do++
    if(Look==0 and Do==1)
        c_Look_0_Do++
    if(Pers==0 and Do==1)
        c_Pers_0_Do++
    if(Heig==0 and Do==1)
        c_Heig_0_Do++
    if(Up==0 and Do==1)
        c_Up_0_Do++

    p_Do=c_Do/#总数
    p_Look_0_Do=c_Look_0_Do/c_Do
    p_Pers_0_Do=c_Pers_0_Do/c_Do
    p_Heig_0_Do=c_Heig_0_Do/c_Do
    p_Up_0_Do=c_Up_0_Do/c_Do

    p_All_0_Do=p_Look_0_Do*p_Pers_0_Do*p_Heig_0_Do*p_Up_0_Do
    p_Do_All_0=p_All_0_Do*p_Do/(p_Look_0*p_Pers*p_Heig_0*p_Up_0)
    
    p_All_0_Do_0=p_Look_0_Do*p_Pers_0_Do*p_Heig_0_Do*p_Up_0_Do
    p_Do_0_All_=p_All_0_Do_0*p_Do_0/((p_Look_0*p_Pers*p_Heig_0*p_Up_0)

if __name__ == "__main__":
