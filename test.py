Dagen = {
"Hond"
"Kat"
"Hond"
}
res = []
[res.append(x) for x in Dagen if x not in res]
print(Dagen)