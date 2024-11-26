znaki = "<>{}[]() "
p="<{[("
k=">}])"
a="<(([)])>"
def nawiasy(a):
  """"""
  d=True
  while d:
      if len(a)>0 and a[0] in k:
          d=False
      c=0
      for i in a:
        if i in znaki:
            c+=1
      if c%2 != 0:
          d=False
      else:
        x=[]
        for i in range(len(p)):
          x.append(a.count(p[i])==a.count(k[i]))
        print(x)
        if (False in x):
          print("false")
          d=False
          break
        else:
          for i in a:
              if i in znaki:
                if i in p and k[p.index(i)] in a:
                  q=p.index(i)
                  temp=a[a.index(i)+1:a.index(k[q])]
                  print(temp)
                  if len(temp)>0 and nawiasy(temp)== False:
                    break
                  else:
                    a=a[a.index(k[q])+1::]
                    if len(a)==0:
                      return True
                    else:
                      nawiasy(a)
                      return d

print(nawiasy(a)==True)
