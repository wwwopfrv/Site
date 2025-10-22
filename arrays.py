# Pentru a păstra notele studentului de la sesiunea de
# iarnă este nevoie de un grup de 6 numere naturale (se
# consideră că studentul are 6 examene în sesiune)

# otsenki = [6, 7, 8, 9, 10, 4]

# for otsenka in otsenki:
#     print(otsenka, end=" | ")

# mojno proitisi po kajdoy otsenke i napechatati ee
# mojno k primeru sdelati obshuiu sredniuu po etim otsenkam dlya etogo ya vvedu tebe takoe ponyatie kak "metodi"
# metodi kak funktsii toliko oni vizivaiutsya ot kakogo-to obiekta
# k primeru
# vot functia
# print("sobaka sobaka")
# tut functia print vizivaetsya iz nichego prosto vot esti functia i mi ee ispolizuem tak? es
# a vot metod
# "sobaka sobaka".split(" ")
# a tut vot metod i on vizivaetsya iz stroki(string) "sobaka sobaka", i zachastuiu tak proishodit chto metodi chto-to vozvrashaiut poetomu nam nujno chto-to delati s tem chto oni vozvrashaet
# v etom sluchaem metod "split" delit stroku po kakomu-to razdeliteliu i vozvrashaet massiv iz poluchennih chastey seichas ya sdelaiu stroku pointeresnee chtobi ti ponyala kak eto rabotaet

# s = "sisi jopi pisi lyajki sheiki"
# list_s = s.split() #split po defoltu ispolizuet probel kak razdeliteli t.e. split(" ") i split() eto odno i toje, yasno? yes
# print(s.split())
# vidishi? metod split() sdelal iz stroki massiv i vernul ego, a mi ego sohranili v peremennoy list_s, kak i v sluchayah gde mi delaem uslovno 15*3, nam neobyazatelino sohranyati 15*3 v peremennoy c k primeru mi mojem srazu vivesti na ekran print(15*3) tut tochno tak je
# toje samoe, vidishi? sho ti tiknul a, vmesto togo chtobi sohranyat v peremennoy to chto vernul split() ya srazu eto vivel
# tak vot takih vot metodov kotorie kak libo vzaimodeistvuiut s obiektom ocheni mnogo
# i u raznih obiektov oni raznie
# split() eto metod strok, i dlya chisel uslovno ti ego ne primenishi eto yasno? yyyyyeeassssss
# voot vot tebe 2 metoda listov
l = [3, 4, 7, 1]
print(l)
# summary = sum(l)
# quantity = len(l)
# ya ksta ne pomniu kajetsya eto uje izmenili hahahahaha
# aga
# vot tam vse metodi dostupnie bili 
# l.append(9) #etot dobavlyaet v tvoy massiv kakoe-to znachenie v samiy konets, v skobkah nado ukazati eto znachenie dopustim hochu dobaviti 9 v nash spisok
# l.clear() # etot metod polnostiu chistit tvoy massiv na vhod vrode nichego ne beret sha glyanem
# c = l.index(7) # metod index ocheni polezniy, ibo on nahodit nomer pod kotorim lejit nujniy tebe obiekt, dopustim ya hochu uznati pod kakim nomerom v moem massive lejut semerka
# c = l.pop(1) # pop polezniy metod, on nujen chtobi dostati kakoy-to element iz massiva, on malo togo chto udalyaet ego iz massiva, on ego i vozvrashaet, beret na vhod INDEX elementa, tobishi ego poryadkoviy nomer, k primeru ya hochu dostati iz massiva vtoroy element, t.e. s indexom 1
# l.reverse() # s reverse vse ponyatno, on prosto perevorachivaet tvoy massiv, imenno tvoy, tut yasna? da esti eshe fishka kak perevorachivati massivi viglyadit ona vot tak l[::-1]
# l.sort()
# eto samie hodovie
print(l[::-1])
# eto nazivaetsya slices i ya obiyasniu ih shas posle 10-15 min pauzi
# ok?okishas nado bistro te zadanie pridumati TAM TSELAIA LABA a nu otdohni poka taNdaiPON STOI a?ia j ne zajimala capslock che ia nadelala uje s klavoi 