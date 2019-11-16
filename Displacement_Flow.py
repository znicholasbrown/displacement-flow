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

@task
def Europe():
    print("150 total Europe")

@task
def Neighbors():
    print("Many in Neighboring countries")

@task
def Total():
    print("20500 total Population")

with Flow("Displacement Diagram 2014") as Displacement_Diagram:
    total = Total()

    Internal(upstream_tasks=[total])

    turkey = Turkey(upstream_tasks=[total])
    lebanon = Lebanon(upstream_tasks=[total])
    jordan = Jordan(upstream_tasks=[total])
    iraq = Iraq(upstream_tasks=[total])
    egypt = Egypt(upstream_tasks=[total])
    other_me_na = OtherME_NA(upstream_tasks=[total])

    Neighbors(upstream_tasks=[turkey, lebanon, jordan, iraq])

    germany = Germany(upstream_tasks=[turkey])
    sweden = Sweden(upstream_tasks=[turkey])
    armenia = Armenia(upstream_tasks=[turkey])
    netherlands = Netherlands(upstream_tasks=[turkey])
    bulgaria = Bulgaria(upstream_tasks=[turkey])
    denmark = Denmark(upstream_tasks=[total, turkey])
    switzerland = Switzerland(upstream_tasks=[lebanon])
    britain = Britain(upstream_tasks=[lebanon])
    greece = Greece(upstream_tasks=[lebanon])
    france = France(upstream_tasks=[lebanon])
    austria = Austria(upstream_tasks=[lebanon])
    belgium = Belgium(upstream_tasks=[lebanon])
    norway = Norway(upstream_tasks=[total, jordan])
    russia = Russia(upstream_tasks=[jordan])
    cyprus = Cyprus(upstream_tasks=[jordan])

    spain = Spain(upstream_tasks=[jordan])
    romania = Romania(upstream_tasks=[jordan])
    italy = Italy(upstream_tasks=[total, iraq])
    malta = Malta(upstream_tasks=[iraq])
    georgia = Georgia(upstream_tasks=[iraq])
    finland = Finland(upstream_tasks=[total])

    ukraine = Ukraine(upstream_tasks=[egypt])

    hungary = Hungary(upstream_tasks=[other_me_na])
    poland = Poland(upstream_tasks=[other_me_na])
    czechRepublic = CzechRepublic(upstream_tasks=[other_me_na])
    moldova = Moldova(upstream_tasks=[other_me_na])
    ireland = Ireland(upstream_tasks=[other_me_na])

    america = America(upstream_tasks=[lebanon, britain, greece])
    brazil = Brazil(upstream_tasks=[lebanon, france])
    canada = Canada(upstream_tasks=[lebanon, austria])
    southKorea = SouthKorea(upstream_tasks=[lebanon, belgium])
    malaysia = Malaysia(upstream_tasks=[total, norway])
    australia = Australia(upstream_tasks=[jordan, russia])
    argentina = Argentina(upstream_tasks=[jordan, cyprus])

    Elsewhere(upstream_tasks=[turkey, lebanon, jordan, iraq, egypt, other_me_na, germany, sweden, armenia, netherlands, bulgaria, denmark, switzerland, britain, greece, france, austria, belgium, norway, russia, cyprus, spain, romania, italy, malta, georgia, finland, ukraine, hungary, poland, czechRepublic, moldova, ireland, america, brazil, canada, southKorea, malaysia, australia, argentina])

    Europe(upstream_tasks=[germany, sweden, armenia, netherlands, bulgaria, denmark, switzerland, britain, greece, france, austria, belgium, norway, russia, cyprus, spain, romania, italy, malta, georgia, finland, ukraine, hungary, poland, czechRepublic, moldova, ireland])
