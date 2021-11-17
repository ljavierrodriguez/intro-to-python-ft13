# Loops

nombres = ["Antonio", "Sergio", "Victor", "Manuel", "Diego", "Arian", "Alfredo", "Luis", "Andres", "Pedro"]


for i in range(1, 11, 2): # range(start = 0, stop, step = 1)
    print(i)


""" for i in range(len(nombres)):
    print(nombres[i]) """


for nombre in nombres:
    print(nombre)

i = 1
while i <= 10:
    print(i)
    i += 1


i = 0
while i < len(nombres):
    print(nombres[i])
    print(nombres[i].find('A') != -1)
    i += 1


nombresConA = [nombre for nombre in nombres if nombre.lower().find('ar') != -1]
print(nombresConA)

""" nombresConA = list(filter(lambda nombre: nombre.lower().find('A') > 0, nombres))
print(nombresConA) """

print("arian".find("an"))

#print(dir("Luis"))


textos = ["""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lorem vel volutpat posuere. Quisque nec orci magna. Donec eget elementum turpis. Ut porttitor varius nulla, sed condimentum mauris tristique sed. Nulla non quam ac ex laoreet porttitor sed semper tellus. Mauris eu diam eleifend, pharetra sem sed, fringilla lacus. Aenean eu mollis mi. Nunc sed hendrerit quam. Integer hendrerit, dui nec bibendum pharetra, diam mauris porta lacus, a malesuada neque felis id neque. Phasellus maximus quam nec magna vehicula, quis egestas dolor condimentum. Donec nec orci vel justo dignissim aliquam.""", """

Nulla congue rutrum massa, non iaculis tellus luctus in. Duis vel ante condimentum, pharetra massa id, elementum metus. Proin a fringilla magna. Praesent fermentum dolor ut augue cursus, ut convallis orci aliquet. Etiam tincidunt facilisis tellus nec scelerisque. Proin volutpat sit amet diam vel bibendum. Vivamus blandit massa lacus, quis venenatis velit commodo id. Sed lobortis vitae diam sed commodo. Suspendisse consequat neque et feugiat iaculis. Duis euismod ligula in orci sagittis, vel sagittis dolor viverra. Pellentesque a libero eget dolor posuere aliquam in sed augue. Aliquam commodo euismod neque nec pellentesque.""", """

Etiam finibus mi magna, nec tristique urna euismod eget. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis feugiat odio mauris, eu sollicitudin nisi auctor ut. Fusce varius dui a auctor eleifend. Maecenas mauris dui, molestie ut augue ut, cursus accumsan quam. Nullam hendrerit enim ante, eu dictum tellus blandit vel. Suspendisse ornare laoreet leo, nec porttitor sem tristique eget. Ut mattis consectetur lectus, sit amet porta neque pretium eget. Proin pharetra feugiat risus, ut vestibulum sapien. Cras ultricies nisl tincidunt metus fermentum, sit amet interdum urna blandit. Sed sollicitudin condimentum ante, ut hendrerit lectus interdum sed. Aliquam pellentesque ipsum nec euismod tincidunt. Aliquam fermentum odio facilisis urna sagittis pellentesque. Mauris tincidunt commodo dictum.""", """

Aliquam arcu mi, scelerisque ac justo et, suscipit tempus justo. Morbi sed eros tristique, ornare nibh nec, consectetur lorem. Nullam lorem nulla, volutpat et commodo ut, rhoncus sit amet massa. Mauris auctor eros id leo aliquam, sed scelerisque sem lobortis. Fusce eget nisi id purus accumsan tincidunt eu at lacus. Donec interdum tortor vel odio varius, in tempor sem porttitor. Suspendisse potenti. Nunc sed congue nibh. Nam vel magna nec nulla blandit malesuada. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent urna massa, auctor et ligula sed, pretium bibendum eros. Quisque rhoncus lacus turpis, nec feugiat nibh pulvinar at. Morbi quis turpis quis nulla venenatis rutrum. Nullam rutrum elit sed neque placerat, et pretium sapien facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque posuere, risus ac lacinia iaculis, ante arcu faucibus eros, eu tempus turpis nisi id ex.""", """

Mauris convallis augue magna, vel consequat orci rhoncus id. Suspendisse elit felis, dapibus eget condimentum in, auctor sit amet nisi. Suspendisse sed sem nec libero gravida maximus. Mauris vitae metus mollis libero tincidunt consectetur in at justo. Duis quis vestibulum orci. Donec sed mi et augue iaculis accumsan ac quis augue. Nulla lorem tortor, dictum id fermentum pharetra, pulvinar a neque.""", """

Praesent a odio lobortis, porta odio id, laoreet libero. Aenean aliquet massa eget blandit dignissim. Sed ultrices pellentesque nibh pretium mollis. Pellentesque ac auctor dui. Sed id pharetra risus, nec sagittis massa. Maecenas fringilla urna sit amet tincidunt gravida. Maecenas non eros scelerisque, porta magna ut, varius arcu. Sed a vestibulum lorem. Phasellus in tellus ipsum. Vivamus congue ac sapien condimentum porta. Nam est lectus, maximus eget purus vitae, euismod malesuada nulla. Vestibulum sollicitudin varius massa, in scelerisque nulla blandit sit amet. Donec eget ex viverra, sodales lorem sit amet, efficitur mauris. Vestibulum fermentum nulla facilisis ornare vulputate.""", """

Praesent non odio mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris fringilla aliquet faucibus. Aliquam molestie dictum mi, at varius mauris dictum id. Vivamus eleifend dignissim sapien, non rhoncus metus. Sed condimentum tincidunt eros a blandit. Aliquam ac tortor gravida, commodo nulla et, posuere mauris.""", """

Curabitur vel dapibus purus, ut placerat ante. In iaculis ac augue et condimentum. Vestibulum vel ex eget urna ornare laoreet. Sed non arcu vel diam consectetur commodo rutrum non ante. Phasellus posuere purus vel velit pulvinar, in euismod tortor mollis. Etiam enim erat, commodo quis libero in, luctus sodales nibh. Aliquam at mollis mi, vitae rhoncus ex.""", """

Proin diam mauris, interdum interdum ex id, aliquet eleifend odio. Mauris fermentum convallis ultrices. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique dui ut sagittis congue. Duis dui mi, maximus at tellus sed, blandit tempor est. Donec eleifend urna elit, quis laoreet nisl lacinia eget. Nulla tempus nunc quis bibendum pretium. Nunc faucibus mauris id ante elementum blandit. Praesent aliquam lectus dapibus elit tincidunt faucibus vel at sapien. Vivamus sollicitudin lacus turpis, eu placerat leo sollicitudin fermentum. Morbi tempus ipsum non nunc cursus faucibus.""", """

Nulla mattis tortor purus, eu condimentum urna dapibus ac. Duis ac turpis eu quam consectetur rutrum et a sem. Sed elit tellus, mattis vitae mauris ac, convallis dignissim elit. Donec egestas sagittis ante, dapibus eleifend risus luctus nec. Nulla facilisi. Praesent auctor ultricies metus tempor aliquam. Phasellus eu mattis nibh. Suspendisse sed arcu dignissim, congue ligula nec, pulvinar justo. Fusce convallis ligula metus, ut placerat est venenatis a. Donec quis erat sed mi tempus malesuada. Donec vel nisi vel magna porta iaculis a vitae nisl. Curabitur venenatis urna mi, eu vestibulum dolor tincidunt id."""]

print(len(textos))

textConLuctus = [texto for texto in textos if texto.lower().find('magna') != -1]

print(textConLuctus)