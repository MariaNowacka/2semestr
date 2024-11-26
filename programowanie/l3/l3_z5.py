znaki = "<>{}[]() "
p="<{[("
k=">}])"
a="<(([)])>"
b="{[(a)(b)]}"
def nawiasy(a):
  """"""
  if len(a)>0:
    if a[0] in k:
      return False
  else:
    return True
  c=0
  for i in a:
    if i in znaki:
        c+=1
  if c%2 != 0:
      return False
  else:
    x=[]
    for i in range(len(p)):
      x.append(a.count(p[i])==a.count(k[i]))
    if (False in x):
      return False not in x
    else:
      for i in a:
          if i in znaki:
            if i in p and k[p.index(i)] in a:
              q=p.index(i)
              temp=a[a.index(i)+1:a.index(k[q])]
              if len(temp)>0 and nawiasy(temp)== False:
                return False
              else:
                a=a[a.index(k[q])+1::]
                if len(a)==0:
                  return True
                else:
                    return nawiasy(a)

print(nawiasy("<>{[()()}]")==True)
