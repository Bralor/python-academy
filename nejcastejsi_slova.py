#!/usr/bin/python3
"""Lekce #5 - Uvod do programovani, nejcastejsi slova"""

TEXT = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual.
Cold entered excellence questions chiefly hung tried having body overcame
twenty hills. Afraid easy admire settled promotion. Convinced full manners
household cottage savings giving sweetness. Easy dearest beyond guest suffer
examine moderate things hills together proposal basket ferrars just really.
Written merry prudent enjoyment laughter wise subjects blind lain given. More
moderate affection speaking unpacked increasing seen ask increasing season.
Arrival twenty continue thrown invited remainder neat juvenile point saved
favourable society disposing desirous. Seemed months linen inquietude
branched otherwise ladies little cordially depend entirely surrounded
addition past feebly. Sent overcame ye pleasant household eyes addition sir
perpetual assurance middleton enough marriage yourself living. Expenses times
inquiry who thirty offended opinion removal stairs. Dull seen expression chief
insensible remember additions spoil their projecting pasture respect either
sight whatever or. Arise laughing mile moment disposal affronting reasonable
situation often jokes shot unpleasing. Wrong better those hopes man besides
must were although scale. Cordial related meant pretty total valley motionless
pretty whose possible thrown desirous own. Great without arranging room. She
park feet stairs again prevent points our gave marry greatest keeps welcomed.
Few picture than exertion himself inquiry sufficient friends answered formerly
promotion dull done shutters affection. Dining so china affixed followed
motionless surprise. Gentleman sing known hill age. Motionless paid hastened
sure enjoyment declared mistress. Procured improve reached projecting
certainly announcing goodness good lose. Reserved middletons my share asked
aware new seeing suitable entirely our timed. Justice expenses pronounce men
given occasional existence finished from fanny settle. Occasional eldest
extremity horrible chief amounted wholly extremity pronounce painful. Company
better every hastily held window. Dissimilar discretion pleased dashwood
children who branched. Settled on timed unpleasant prevent chiefly dinner. Set
quiet lasted declared lively it cottage collecting household told strongly
temper decisively we consulted. Remain or worse placing doubtful suffer
necessary arise does perpetual drawn conduct shed amiable want suspicion
ashamed. Hopes better esteems mother margaret rent pasture favour produce
service instrument astonished marry unfeeling offending affection. Ashamed
unpleasing ourselves produce made entreaties suffering went express strongly
opinions year need burst away motionless jokes. Views securing furniture.
Means message itself there table come balls in unaffected spring thoroughly
next admire. None behaviour blushes carriage felicity humanity suspicion
concealed believe elinor saved. Sitting greater secure called replying
beauty sorry. Resolve marriage simplicity remaining kindness suppose beloved
afraid sight winding sportsman and engrossed my absolute message enabled.
Side enable cease sister contrasted questions deal giving make insensible
daughter forfeited. Exquisite numerous peculiar tiled blush so servants
solicitude another. Ladyship properly dissuade advanced desirous raillery
woman table points desire sorry correct advantage. Margaret steepest
unaffected nearer perpetual distrusts supplied denoting often feeling
surprise others occasional wife object humoured. Talked satisfied affronting
occasional yet wishes considered jennings indeed daughters.
Who answer considered off ladies ask extended discovered distant away season.
Remember earnestly how place temper shew concluded bringing greater outweigh.
Sense pleasure valley account even produce must oh or looked great excellence
ladies total entrance mistake terminated. Consisted however noisier pain our
call dashwood prospect civil another studied high feebly delay. Gravity
blessing defer county marriage. Viewing enable roof settling because common
delivered affection peculiar know great colonel pleasure continue lasting.
Written attacks humoured elegance passed branched estimating can. Certain
likewise reserved we situation. Wife heart maids shy although sitting point
remarkably pleasure moments attended improving comfort its considered shew.
Absolute when service honoured departure promise unreserved situation advanced
delight thoughts oppose repair stimulated.  Added melancholy forming september
melancholy danger manor tall my regard weeks within maids. Advice material
against highly done furniture water sing me moments cottage certainty affixed
dine carriage among. Entire besides raising advantages entreaties certainly
another. Smart from carriage promotion whether by dependent valley attacks
husbands mistress material mirth. Parties unlocked carried fruit improving
stairs eagerness but off enjoy frankness dwelling contrasted imprudence
elsewhere shutters every. Applauded vicinity every. Painful highly elinor.
Times could hastily contrasted. Vulgar indeed talking sooner jokes mother
humoured correct fail attempted advantage think merely year result feebly
learn. Length fifteen laughing shot remain welcome. Fancy unknown marked find
consider. Property express day then expense wish tears engaged called. Woman
forfeited fact weather ought demesne style dwelling ample elsewhere properly.
Total linen have forfeited. The carried peculiar roused worth excellence
depending consisted concern rendered none pronounce before because. Wise
pulled gravity having brother jennings wanted offence vulgar received little.
Nor would request miss announcing. Fortune inquietude past. Even extensive it
season true continuing hardly cause thoroughly horses dining mile provision
disposed thrown. Esteems juvenile nothing quitting mrs. Jointure most
breakfast adieus opinion extensive feet hill wise music resembled entrance
since needed husbands uncommonly curiosity. Civility though welcome winding
blind conveying lively spoil. Enjoyment affection sooner compliment shade
plate name incommode enabled sake breeding ladyship understood. Extensive
difficult arose therefore greatly far convinced performed unpleasing feet.
Made seems neglected early difficult years affixed. Ye hope or instrument
especially things distance colonel way. Chief admire wanted civility tried
gate compliment. Plan prepared beloved thrown sportsman mind points five
sixteen ought strictly enough other abode abode spirit connection. Defective
allowance delicate sincerity oh inquietude year frankness the household
jointure play dispatched breeding. Education pleasure fanny debating off
surrounded. Examine sportsman depending. Form true held help denote pasture
she. Marianne state supported elsewhere enjoyed abroad any pure. Winding
cousin because pretended point ability offending sent drawn is amounted
unaffected allow propriety. Manner ferrars before comparison remain calling
simplicity minuter stanhill he hundred. Written smallness lose smiling merits
whom friendship lose smallest behaved gay basket heard twenty both going
drawn. Her morning left. Bore they face heart longer county help case maids
morning leave provided dearest sent like preferred. Something case almost
twenty elinor husbands sincerity addition sure. Theirs secure pasture assure
led performed table hope morning avoid almost make far body pure farther
doubtful.  Exquisite horrible admire six know. Mutual gave many covered asked
season except miss prospect called admiration could. Known about man strongly
heart charm disposing desire both debating oppose gentleman goodness
sufficient barton matters limited. Prepared prepare west tears declared dried
help matter this away order females apartments depending round were basket.
"""

ODDELOVAC = "=" * 35
vycistena_slova = []

for slovo in TEXT.split():
    ciste_slovo = slovo.strip(",.:;'")
    vycistena_slova.append(ciste_slovo.lower())

vyskyt_slov = {}

for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] = vyskyt_slov[slovo] + 1

pet_nejcastejsich = sorted(
    vyskyt_slov,
    key=vyskyt_slov.get,
    reverse=True
)[0: 5]

print(
    "5 NEJCASTEJSICH SLOV V TEXTU: ".center(35, " "),
    ODDELOVAC,
    sep="\n"
)
for index, nejcasteji in enumerate(pet_nejcastejsich, 1):
    print(f"{index}, SLOVO:{nejcasteji}, VYSKYT: {vyskyt_slov[nejcasteji]}")

# ~~~~~~~~~~~~~~~~~~~ Dalsi varianty: ~~~~~~~~~~~~~~~~~~~
#vycistena_slova = [
    #slovo.strip(",.:;'").lower() for slovo in TEXT.split()
#]
#vyskyt_slov = {}

#for slovo in vycistena_slova:
# ternarni operator
#    vyskyt_slov[slovo] = 1 if slovo not in vyskyt_slov else \
#        vyskyt_slov[slovo] = vyskyt_slov[slovo] + 1

# metoda setdefault()
#    vyskyt_slov[slovo] = vyskyt_slov.setdefault(slovo, 0) + 1

# modul collections
#from collections import Counter
#pocitadlo = Counter(vycistena_slova)
#pocitadlo = Counter(vycistena_slova).most_common(5)
#print(f"{list(pocitadlo)}")

# ~~~~~~~~~~~~~~~~~~~ Dalsi varianty: ~~~~~~~~~~~~~~~~~~~

