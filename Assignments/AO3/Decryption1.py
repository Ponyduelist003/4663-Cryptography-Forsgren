#Code will print out the first decrypted text
# list of letters
alphabet = [chr(x+97) for x in range(26)]

#list of letters to substitute
subs = ['-'] * 26
subs[11] = 'e'
subs[2] = 't'
subs[5] = 'h'
subs[8] = 'a'
subs[4] = 'r'
subs[17] = 'v'
subs[10] = 'l'
subs[1] = 's'
subs[6] = 'n'
subs[20] = 'o'
subs[3] = 'p'
subs[14] = 'i'
subs[12] = 'd'
subs[16] = 'g'
subs[7] = 'm'
subs[18] = 'f'
subs[24] = 'b'
subs[22] = 'y'
subs[0] = 'w'
subs[19] = 'u'
subs[9] = 'c'
subs[13] = 'q'
subs[23] = 'k'

# here is the plain text
plaintext = "sute bjuel igm blrlg wlieb iqu ute sicfleb yeutqfc suecf ug cfob jugcoglgc, i gla gicoug, jugjlorlm og koylecw, igm mlmojiclm cu cfl deudubocoug cfic ikk hlg iel jeliclm lntik. gua al iel lgqiqlm og i qelic jorok aie, clbcogq aflcfle cfic gicoug, ue igw gicoug bu jugjlorlm igm mlmojiclm, jig kugq lgmtel. al iel hlc ug i qelic yicckl-solkm us cfic aie. al firl juhl cu mlmojicl i duecoug us cfic solkm, ib i sogik elbcogq dkijl sue cfubl afu flel qirl cfloe korlb cfic cfic gicoug hoqfc korl. oc ob ikcuqlcfle soccogq igm deudle cfic al bfutkm mu cfob. ytc, og i kieqle blgbl, al jig guc mlmojicl -- al jig guc jugbljeicl -- al jig guc fikkua -- cfob qeutgm. cfl yeirl hlg, korogq igm mlim, afu bcetqqklm flel, firl jugbljeiclm oc, sie iyurl ute duue duale cu imm ue mlceijc. cfl auekm aokk kocckl gucl, gue kugq elhlhyle afic al biw flel, ytc oc jig glrle sueqlc afic cflw mom flel. oc ob sue tb cfl korogq, eicfle, cu yl mlmojiclm flel cu cfl tgsogobflm auex afojf cflw afu sutqfc flel firl cftb sie bu guykw imrigjlm. oc ob eicfle sue tb cu yl flel mlmojiclm cu cfl qelic cibx elhiogogq ylsuel tb -- cfic seuh cflbl fuguelm mlim al cixl ogjeliblm mlrucoug cu cfic jitbl sue afojf cflw qirl cfl kibc stkk hlibtel us mlrucoug -- cfic al flel foqfkw elbukrl cfic cflbl mlim bfikk guc firl molm og riog -- cfic cfob gicoug, tgmle qum, bfikk firl i gla yoecf us sellmuh -- igm cfic qurleghlgc us cfl dludkl, yw cfl dludkl, sue cfl dludkl, bfikk guc dleobf seuh cfl liecf.".lower()

#loops through the letters of the plaintext
for p in plaintext:
  #if a letter, take Ascii Number - 97 and substitute in the subs entry of that number
  if p in alphabet:
    i = ord(p)-97
    print(subs[i], end = ' ')
  #if not a letter, just print normally
  else:
    print(p)
