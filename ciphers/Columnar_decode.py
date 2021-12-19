from math import ceil
import sys
COUNTED = "abcdefghijklmnopqrstuvwxyz"

text = "nkohctergrnuuelameksileidoeapiphivtahsauavtosmdaoovieenbmmefiarleeeeezgeghtattolaiessbezmsnotddnwnivabnseozneenhtdbltrgtrolneibaaeiraoeelnithanirglnervrokweeseuhvsezagernioemdteuenoeetaeneenntrgtnfhleeiataeheasouoigokwroaekuieibdgeeeodvlcaueednneieoomaniartbnnrnideeerrrnodonnoethtivdbdimkueepnebtntkeeeaarltpknwjnokaaahtendettndeencgtlorgeeuenatgkvrgdjtgmroeazmdeaeeetrpeentkonneretbaaairaentetavreaabiobweiokmzkknrpmgicebnvaneasradekdetoodeigtridddtigvjvbnordhaeegvabhenefuotargtdusbrnueuijkmnekdnbeorwyanmiilekmdsprousmnsercearrtensnnvbmezdwernnlamvoekbeddrogncewssonaudenndheeetdenegennaeeodbenhdodnngeeprkbndedlnkvwzovrlodeennnjznneedetedtlrbrrrenrrodekeiurmonhtrwetnzitenilaenoonilcawktaavdchakoropeoareweearustntgtdkweianvrdgreiiesetpeajeclgkenvleeaktvdkkddveeoiooebidddsepneketonhhdsntssodmotadzvojlsbiorlahoheaaavzlaoewaeobapgpwueolezawgetusoienmeikcothithdnieenecoentlondocmenaernlhwngkbongndmiieerieregkeiwrrntsnneoelseeeeihvrgoiueigliddsglslnedtdddiuaibstcadaeeidwaterudizeedlitiawieoditdnjsnnepnattoosocgttngaaeoeoenuticrgioemnddnksnirnmierethaaarontvtteneapdrarohasnotrsvsmeatkteueofeiewuoivscenngjzndeniodeeaveorioteakoainnenieoenetelzgkgrdktnietredoaniizwdiigeddtsgesnwnzttrtrgdsereadrcrtgdqeleenslreeltngnsmaotlgncttavfeseendalrzmheeeanelaelgernwegeeztnteroedrdoeevdettoeopuaeiatnlarnudefepeinlviifkemonvrrravseiroaniseeemrlmsntagklhootdeeeveegglhkkvkzoveehtcdrehaveesetbrseoeajjbnanwameenladatepggnrvahmrzrneedemnirneiseetedcanztimeegefjrlohatcrfeeoautd"
key = "4,3,5,1,2,0"


if len(sys.argv)>1:
    key = sys.argv[1]
    with open(sys.argv[2], "r", encoding="utf8") as file:
        text = file.read()


key = key.lower()
key = key.split(",")

text = text.lower()
text = ''.join([i for i in text if i in COUNTED])

amount = {i:len(text)//len(key) for i in key}

for i in range(len(text)%len(key)):
    amount[key[i]]+=1


rows = {i:[] for i in key}

total = 0
for i in sorted(rows):
    for _ in range(amount[i]):
        rows[i].append(text[total])
        total += 1


result = ""
print(rows)
for i in range(ceil(len(text)/len(key))):
    for row, value in rows.items():
        if len(rows[row])>i:
            result += value[i]

print(result)

if len(sys.argv)>3:
    with open(sys.argv[3], 'w',encoding="utf-8") as f:
        f.write(result)
    print("done")

