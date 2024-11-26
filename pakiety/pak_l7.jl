using Random
a=rand(1:20,10)
print(a)
function quicksort(a,lewy,prawy)
    i=lewy
    j=prawy
    p=a[div(lewy+prawy,2)]
    while i<=j
        while(a[i]<p)
            i+=1
        end
        while(a[j]>p)
            j-=1
        end
        if i<=j
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        end
    end

    if lewy<j
        quicksort(a,lewy,j)
    end
    if i<prawy
        quicksort(a,i,prawy)
    end
    a
end
quicksort(a,1,length(a))
print(a)

##
function shellsort(tab, n)
    odstęp = div(n,2)
    while odstęp>0
        j=odstęp
        while j<n
            i=j-odstęp+1
            while i>0
                if tab[i+odstęp]>tab[i]
                    break
                else
                    tab[i+odstęp],tab[i]=tab[i],tab[i+odstęp]
                end
                i-=odstęp
            end
            j+=1
        end
        odstęp=div(odstęp,2)
    end
    b
end
b=rand(1:20,10)
shellsort(b,length(b))

print(b)

## zadanie 2
# za duża złożoność
function braki(tablica)
    for i in 1:length(tablica)-1
        if i in tablica
            if i+1 in tablica
                continue
            else
                print("brakujący element to $(i+1)")
                break
            end
        end
    end
end

braki([1,2,3,4,5,6,7])





function niema!(tab,a=1,b=length(tab),c=length(tab))
    n=length(tab)
    if tab[n] == n
        o="fantastic"
    else
        while c>div(b,2)
            if length(tab[a:b]) == c
                #print("jest fantastycznie")
                niema!(tab,div(b,2),b,c-div(b,2))
                #a,b,c = div(b,2),b,c-div(b,2)
            else
                niema!(tab,a,div(b,2),div(c,2))
                #a,b,c = a,div(b,2),div(c,2)
            end
        end
    tab
    end
end
tab=[1,3,4,5,7,8]
niema!(tab)
function szuk(tab, l=1, p=length(tab))
    n=length(tab)
    if tab[n]==n
        return "W liście nic nie brakuje"
    end
    while l<p
        s=div(l+p,2)
        if tab[s]>s
            p=s
        else
            l=s+1
        end
    end
    tab[div(l+p,2)]+1
end
szuk(tab)




## zadanie 4
function odległość(w1, w2)
    m=length(w1)
    n=length(w2)
    d=zeros(Int,m+1,n+1)
    for i in 1:m+1
        d[i,1]=i-1
    end
    for j in 1:n+1
        d[1,j]=j-1
    end
    for i in 2:m+1
        for j in 2:n+1
            if w1[i-1]==w2[j-1]
                odl = 0
            else
                odl = 1
            end
            d[i,j]=minimum([d[i-1, j] + 1,       # usuwanie
                           d[i, j-1] + 1,        # wstawianie
                           d[i-1, j-1] + odl])   # zamiana
        end
    end
    d[m+1,n+1]
end
w1="kacfka"
w2="kacszkaw"
odległość(w1,w2)

function odlbezost(w1,w2)
    m=length(w1)
    n=length(w2)
    d=zeros(m,n)
    for i in 1:m
        d[i,1]=i-1
    end
    for j in 1:n
        d[1,j]=j-1
    end
    for i in 2:m
        for j in 2:n
            if w1[i-1]==w2[j-1]
                odl = 0
            else
                odl = 1
            end
            d[i,j]=minimum([d[i-1, j] + 1,       # usuwanie
                           d[i, j-1] + 1,       # wstawianie
                           d[i-1, j-1] + odl])   # zamiana
        end
    end
    d[m,n]
end
niema
odlbezost(w1,w2)