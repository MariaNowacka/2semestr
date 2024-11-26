using JLD2, LsqFit,Plots
@load "E:\\pakiety\\harmOsc(1).jld2"
#x(t) = Asin(ω*t+Φ)
#p=[A,ω,Φ]
@. model(x,p)=p[1]*sin(p[2]*tsA+p[3])
xdata=tsA
ydata=xsA
p0=[1., 12, 4.5]
fit = curve_fit(model,xdata,ydata,p0)

plot(tsA,xsA)
plot!(tsA,model(tsA,fit.param))

fit.resid
fit.param
##
using CSV, DataFrames
using Plots
dane = DataFrame(CSV.File("D:\\pakiety\\PS_2023.05.29_15.16.14.csv", comment="#"))
#a=CSV.read("D:\\pakiety\\PS_2023.05.29_15.16.14.csv", DataFrame, comment=(Nothing, ""))
#println(describe(dane))
#println(unique(dane[!,"pl_name"]))
planet_mass = dane[!,"pl_masse"]
planet_radius = dane[!, "pl_rade"]
mass_radius_scatter = scatter(planet_radius, planet_mass, xlims=(0.01,40), ylims=(0.01, 5e4),
yscale=:log10, xscale=:log10)

planet_temp = dane[!, "pl_eqt"]
orbit = dane[!, "pl_orbsmax"]
temp_orbit_scatter = scatter( orbit,planet_temp, ylims=(100, 1000), xlims=(0.01, 1),yscale=:log10, xscale=:log10)
#R^-2

scatter(planet_radius.^3,planet_mass,xlims=(0.01,40), ylims=(0.01, 50))
den = dane[!,"pl_dens"]
scatter(den, planet_radius, xlims=(0,100), ylims=(0,20))
#linia prosta na logarytmach to funkcja potęgowa
#jest nowa julia, szybsza! 