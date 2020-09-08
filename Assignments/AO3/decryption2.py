# list of letters
alphabet = [chr(x+97) for x in range(26)]

#list of letters to substitute, initiated to - to aid guesswork
subs = ['-'] * 26
subs[25] = 'e'
subs[13] = 't'
subs[15] = 'h'
subs[5] = 'o'
subs[6] = 'f'
subs[10] = 'n'
subs[12] = 'w'
subs[20] = 'i'
subs[4] = 'r'
subs[23] = 'g'
subs[8] = 'u'
subs[2] = 's'
subs[16] = 'b'
subs[24] = 'a'
subs[1] = 'l'
subs[0] = 'p'
subs[21] = 'm'
subs[9] = 'd'
subs[11] = 'y'
subs[22] = 'q'
subs[3] = 'v'
subs[19] = 'c'
subs[17] = 'k'

# here is the plain text
plaintext = "npz aynp fg npz euxpnzfic vyk uc qzczn fk ybb cujzc ql npz ukzwiunuzc fg npz czbgucp ykj npz nleykkl fg zdub vzk. qbzcczj uc pz mpf, uk npz kyvz fg tpyeunl ykj xffj mubb, cpzapzejc npz mzyr npefixp npz dybbzl fg npz jyerkzcc, gfe pz uc neibl puc qefnpze’c rzzaze ykj npz gukjze fg bfcn tpubjezk. ykj u mubb cneurz jfmk iafk npzz munp xezyn dzkxzyktz ykj gieufic ykxze npfcz mpf ynnzvan nf afucfk ykj jzcnefl vl qefnpzec. ykj lfi mubb rkfm u yv npz bfej mpzk u byl vl dzkxzyktz iafk lfi.".lower()

#loop through the letters of plaintext
for p in plaintext:
  #if a letter, take ASCII code - 97 and replace with that numbered subs entry
  if p in alphabet:
    i = ord(p)-97
    print(subs[i], end = '')
  #if not a letter, print normally
  else:
    print(p)
