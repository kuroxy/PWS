
import enigma_cy
import time

# defaults



rotorIw = [ord(i)-65 for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
turnoverI = enigma_cy.char_to_val("Q")

rotorIIw = [ord(i)-65 for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
turnoverII = enigma_cy.char_to_val("E")

rotorIIIw = [ord(i)-65 for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
turnoverIII = enigma_cy.char_to_val("V")


reflw = [ord(i)-65 for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]





text = "TYTFOWQHRVBEFTYWDZMTUGEWMIJDIYLKGPWQUTZCBYFVATZQGFCWXOSIVLDBDXKYZYJPMVZWDSLVWXJVSKMKIYBMYNZJJGKSBNQFBXTRZXGVHYKIKFMXLAXBMGQKLBMHFFMCHEONCBDSPRZZFTHAOKTSZGNXZJOOKCHZFEDUEUIFWESVSDBYHEVGIWJEOOLLHZKLMXCHEBHHUYSNQOWDFESYSMLJOUMGIEYAHUWVCHTDIXLXJCNNPQQAJYWRCQGUHMPDVPZMEYSETVCDXEYRPLWGJQYLAMDYIQWORVZSRZGKKKKLQBZWJKUVVPQRQXCYCRTVPFTMDUCVCVPTGRHJAIAMZRSNBQRDVNNCSHZBIQZZSOUJRSEAYJZIWGKMTVNWHRLKGFAJWENJKSKLVJNCJINHAUZMQKAXMVIBBOITXNWUMGYLUMZCBXIHJMJKKHSFHRTDAHVXZBJLATYGWHWZOQMYCTRKMHQRUKFMTSRIUSPPKIAMHJKLKLSSYVIXPXCFIDDSJDXJOGZOLSJOGQVMYONFOTCTGVOGDNHRSNLUXMRBTTSBXXCUFTSPUXPRUHNVCMKVUJSITKZBDBUNXMQDBJMBUUKMDDXPAHAMYZFYQZZJMGTSMEXSVYVETGOZGJFWPTGPLUEMFNVRXMRPYOOIZHONLPSFHMXLBCSJKVJZMERGWGHNXVGHDYCILVXIBSXPKGLCWZQZQPNEXLDRZKBLXXPSQVAWSETOWEHFUSZBBGEPQNZXHCICMEBPBKLHVYCZSQVKJIIDHGUSTIMJMPTTUFOLZLHKESPPFVHBODYKWPSMCQPZPMSOEDFBBAKEKYCQUPSMASJMUYFHCNTLKPQIRWORNSBCXPEEDEJRPJRODGVNLYKFROFCNIYSEWZWQGYWXSCYIODQNZWLSZTBJGSGDPHHBTZAEMTHESXMQZYNLKOPKX"
text = text.lower()

text = "".join(ch for ch in text if ch in "abcdefghijklmnopqrstuvwxyz")
"""
# how to encode
print(enigma_cy.encode_enigma(plugboard, [rotorIw,rotorIIw,rotorIIIw],[offset],[turnoverI,turnoverII,turnoverIII], reflw, text))


times = time.time()


a = enigma_cy.crack_offset(plugboard, [rotorIw,rotorIIw,rotorIIIw],[turnoverI,turnoverII,turnoverIII], reflw, text)
"""


text = "zouditeenvoorbeeldvanenigmazijnofishetmaareenillusierotorszijndrieeentweemetoffseteentweedrieenplugboordmetazbl"
plugboard = enigma_cy.create_plugboard("azbl")
print(enigma_cy.encode_enigma(plugboard, [rotorIIIw,rotorIw,rotorIIw], [1,2,3],[turnoverIII,turnoverI,turnoverII], reflw, text))

