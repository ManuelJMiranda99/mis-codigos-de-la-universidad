def leer(horario):
    
    archivo=open(horario,"r")
    l_horarios=[]
    l_asignaturas=[]
    d_asignaturas={}
    l_b=[]
    l_t=[]
    l_e=[]
    l_m=[]
    l_c=[]
    l_q=[]
    l_i=[]
    c_av=0
    am=0
    l_am=[]
    
    for linea in archivo:

        l_n=linea.strip("\n")
        l_linea = l_n.split(",")
        l_horarios.append(l_linea)
        l_asignaturas.append(l_linea[0])
        #diccionario por escuela
        
        escuela = l_linea[0]
        if escuela[3]=="B":
            l_b.append(l_linea)
        if escuela[3]=="T":
            l_t.append(l_linea)
        if escuela[3]=="E":
            l_e.append(l_linea)
        if escuela[3]=="M":
            l_m.append(l_linea)
        if escuela[3]=="Q":
            l_q.append(l_linea)
        if escuela[3]=="C":
            l_c.append(l_linea)
        if escuela[3]=="I":
            l_i.append(l_linea)
            
            
        h_escuelas={"Basico":l_b,"Telecomunicaciones":l_t,"Electrica":l_e,"Mecanica":l_m,"Quimica":l_q,"Civil":l_c,"Industrial":l_i}
        
        #porcentaje de materias aula virtual
        
        for k in l_linea:
            if k=="AVING":
                c_av+=1
                break
        #asignatura con mas bloques de hora
        l_am.append(len(l_linea))
    b_am=max(l_am)
    for p in l_horarios:
        len(p)
        
        if len(p)>=b_am:
            am=p[0]

    #secciones por asignatura
           
    for g in l_asignaturas:
        if g in d_asignaturas:
            d_asignaturas[g]+=1
        else:
            d_asignaturas[g]=1

    #zona de calculos
    t_m=len(l_b)+len(l_t)+len(l_e)+len(l_m)+len(l_q)+len(l_c)+len(l_i)
    
    p=(c_av*100)/t_m
    
    #zona de impresion
    print(l_horarios)
    print()
    print(h_escuelas)
    print()
    print("materias por escuela")
    print("Basico:",len(l_b))
    print("Telecomunicaciones:",len(l_t))
    print("Electrica:",len(l_e))
    print("Mecanica:",len(l_m))
    print("Quimica:",len(l_q))
    print("Civil:",len(l_c))
    print("Industrial:",len(l_i))
    print()
    print("secciones por materia: ",d_asignaturas)
    print()
    print("total de materias:",t_m)
    print("procentaje de materias en Aula Virtual:",p)
    print("asignatura con mayor cantidad de bloques:",am)
    
leer("horarios.txt")