from prefect import Flow, task

@task
def Internal():
    print("7,633 internally displaced")

@task
def Turkey():
    print("1,558 displaced in Turkey")

@task
def Lebanon():
    print("1,147 displaced in Lebanon")

@task
def Jordan():
    print("623 displaced in Lebanon")

@task
def Iraq():
    print("234 displaced in Iraq")

@task
def Egypt():
    print("138 displaced in Egypt")

@task
def OtherME_NA():
    print("161 displaced in other countries in the Middle East & North Africa")

@task
def Germany():
    print("41 displaced in Germany")

@task
def Sweden():
    print("34 displaced in Sweden")

@task
def Armenia():
    print("?? displaced in Armenia")

@task
def Netherlands():
    print("?? displaced in Netherlands")

@task
def Bulgaria():
    print("?? displaced in Bulgaria")

@task
def Denmark():
    print("?? displaced in Denmark")

@task
def Switzerland():
    print("?? displaced in Switzerland")

@task
def Britain():
    print("4 displaced in Britain")

@task
def Greece():
    print("?? displaced in Greece")

@task
def France():
    print("3 displaced in France")

@task
def Austria():
    print("?? displaced in Austria")

@task
def Belgium():
    print("?? displaced in Belgium")

@task
def Norway():
    print("?? displaced in Norway")

@task
def Russia():
    print("2 displaced in Russia")

@task
def Cyprus():
    print("2 displaced in Cyprus")

@task
def Spain():
    print("1 displaced in Spain")

@task
def Romania():
    print("?? displaced in Romania")

@task
def Italy():
    print("1 displaced in Italy")

@task
def Malta():
    print("?? displaced in Malta")

@task
def Georgia():
    print("?? displaced in Georgia")

@task
def Finland():
    print("?? displaced in Finland")

@task
def Ukraine():
    print("0 displaced in Ukraine")

@task
def Hungary():
    print("?? displaced in Hungary")

@task
def Poland():
    print("?? displaced in Poland")

@task
def CzechRepublic():
    print("?? displaced in Czech Republic")

@task
def Moldova():
    print("?? displaced in Moldova")

@task
def Ireland():
    print("0 displaced in Ireland")

@task
def America():
    print("5 displaced in America")

@task
def Brazil():
    print("2 displaced in Brazil")

@task
def Canada():
    print("?? displaced in Canada")

@task
def SouthKorea():
    print("1 displaced in South Korea")

@task
def Malaysia():
    print("?? displaced in Malaysia")

@task
def Australia():
    print("?? displaced in Australia")

@task
def Argentina():
    print("0 displaced in Argentina")

@task
def Elsewhere():
    print("9 displaced Elsewhere")



with Flow("Displacement Diagram 2014") as Displacement_Diagram:
    population = 20500
    
