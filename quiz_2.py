import sqlite3

def conectar():
    conn=sqlite3.connect("torneo.db")
    return conn
def crear_tabla(conn):
    try:
        c=conn
        c.execute(""" CREATE TABLE IF NOT EXISTS torneo(Grupo TEXT,Partido INTEGER,Equipo_1 TEXT,Equipo_2 TEXT,Goles_EQ1 INTEGER,Goles_EQ2 INTEGER,Goleadores_EQ1 TEXT,Goleadores_EQ2 TEXT,Tiempo_EQ1 TEXT,Tiempo_EQ2 TEXT )""")
        c.commit()
    except Exception as e:
        print(f"Ha ocurrido un error al crear la tabla: {e}")
    
def actualizar_equipo(equipo, ganados, perdidos, empatados):
    equipo["ganados"] += ganados
    equipo["perdidos"] += perdidos
    equipo["empatados"] += empatados
    equipo["puntos"] = equipo["ganados"] * 3 + equipo["empatados"]

def insertar(conn, torneo_file):
    dicc = {}
    band3=True
    mayor=0
    equipo_mayor=None
    c_mayor=0
    band=True
    band2=True
    with open(torneo_file) as arch:
        linea = arch.readline()
        while linea:
            lista = linea.strip().split(",")
            grupo = lista[0]
            partido = lista[1]
            equipo_1 = lista[2]
            equipo_2 = lista[3]
            goles_eq_1 = int(lista[4])
            goles_eq_2 = int(lista[5])

            if grupo not in dicc:
                dicc[grupo] = {"Equipo1": {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0},
                              "Equipo2": {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0}}

            if goles_eq_1 > goles_eq_2:
                ganador = equipo_1
                actualizar_equipo(dicc[grupo]["Equipo1"], 1, 0, 0)
                actualizar_equipo(dicc[grupo]["Equipo2"], 0, 1, 0)
            elif goles_eq_1 < goles_eq_2:
                ganador = equipo_2
                actualizar_equipo(dicc[grupo]["Equipo1"], 0, 1, 0)
                actualizar_equipo(dicc[grupo]["Equipo2"], 1, 0, 0)
            else:
                ganador = "empate"
                actualizar_equipo(dicc[grupo]["Equipo1"], 0, 0, 1)
                actualizar_equipo(dicc[grupo]["Equipo2"], 0, 0, 1)

            #Pregunta 3
            suma=goles_eq_1+goles_eq_2
            if band3:
                mas_goles=suma
                partido_m=partido
                eq1=equipo_1
                eq2=equipo_2
                band3=False
            elif suma>mas_goles:
                mas_goles=suma
                partido_m=partido
                eq1=equipo_1
                eq2=equipo_2
                
            
            #Pregunta 4 y 5
            tiempo_1=lista[8]
            tiempo_2=lista[9]
            separar_1=tiempo_1.split(";")
            separar_2=tiempo_2.split(";")
            

            for tiempo in separar_1:
                j = int(tiempo)
                if band:
                    menor = j
                    e_t = equipo_1
                    band = False
                elif j < menor:
                    menor = j
                    e_t = equipo_1
                if j > 45:
                    c_mayor += 1
                if c_mayor > mayor:
                    equipo_mayor = equipo_1
                    mayor = c_mayor

            band = True
            menor = 60
            equipo_menor = None

            for t in separar_2:
                i = int(t)
                if band2:
                    menor = i
                    e_t = equipo_2
                    band2 = False
                elif i < menor:
                    menor = i
                    e_t = equipo_2
                if i > 45:
                    c_mayor += 1
                if c_mayor > mayor:
                    equipo_mayor = equipo_2
                    mayor = c_mayor

            
            try:
                c=conn.cursor()
                c.execute("""INSERT INTO torneo(Grupo,Partido,Equipo_1,Equipo_2,Goles_EQ1,Goles_EQ2,Goleadores_EQ1,Goleadores_EQ2,Tiempo_EQ1,Tiempo_EQ2)
                VALUES(?,?,?,?,?,?,?,?,?,?)""",(grupo,partido,equipo_1,equipo_2,goles_1,goles_2,goleadores_1,goleadores_2,tiempo_1,tiempo_2))
            except Exception as e:
                print(f"Ha ocurrido un error al insertar datos en la tabla: {e}")
            
            linea=arch.readline()
    print(f"El partido con mayor cantidad de goles fue el partido {partido_m} de {eq1} y {eq2} con {mas_goles}")
    print(f"El equipo en anotar gol mas rapido fue {e_t} al minuto {menor}")
    print(dicc)
    
def leer(conn):
    try:
        c=conn.cursor()
        c.execute("SELECT*FROM torneo")
        listas=c.fetchall()
        for j in listas:
            print(j)
    except Exception as e:
        print(f"Ha ocurrido un error al leer {e}")
            
            
            
a=conectar()
b=crear_tabla(a)
torneo="torneo.txt"
c=insertar(a,torneo)
l=leer(a)