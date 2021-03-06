
ratio = getval(0,1, 100,"green")/100
filename  = getfileonce()
csv  =  readcsv(filename)
rowcount  =  getcsvrowcount(csv)
minval  =  -1000

exportlist  =  makeshapelist()

for  (i  =  1;  i    <  rowcount/3;  i++)
{
pointname  =  getcsvrow(csv,i,0)
x1  =  getcsvrow(csv,i,1)
y1  =  getcsvrow(csv,i,2)
z1  =  getcsvrow(csv,i,3)
	
x2  =  getcsvrow(csv,i,4)
y2  =  getcsvrow(csv,i,5)
z2  =  getcsvrow(csv,i,6)
	
x3  =  getcsvrow(csv,i,7)
y3  =  getcsvrow(csv,i,8)
z3  =  getcsvrow(csv,i,9)
	
ratio = i / rowcount * 1 + 0.1
p1 = makepoint(x1,y1,z1)
vis(p1)

p2 = makepoint(x2,y2,z2)
vis(p2)
	
p3 = makepoint(x3,y3,z3)
vis(p3)

circ = makecircle(p1,p2,p3)
vis(circ)
maketriangle(circ)
}


function maketriangle(circle)
{
	third = 1/3
	
	pt1 = makepointoncurve(circle,0)
	vis(pt1)
	
	pt2 = makepointoncurve(circle,third)
	vis(pt2)
	
	pt3 = makepointoncurve(circle,2 * third)
	vis(pt3)
	
	l1 = makelineptpt(pt1,pt2)
	vis(l1)
	
	l2 = makelineptpt(pt2,pt3)
	vis(l2)
	
	l3 = makelineptpt(pt3,pt1)
	vis(l3)
	
	shapelist = makeshapelist()
	shapelist = addshapetolist(shapelist,l1,l2,l3)
	fill = makefillsrf(shapelist)
	//vis(fill)
	
	cog = getcenterofgravity(fill)
	vis(cog)
	
	createjig(cog,pt1,pt2,pt3)
	
	
	
	
}

function createjig(cp,p1,p2,p3)
{
	
	//ratio = 0.9
	v1 = makevector(p1,p2)
	v2 = makevector(p1,p3)
	zvec = crossproduct(v1,v2)
	
	offp = makepointmovebyvector(cp,zvec,400)
	vis(offp)
	
	l1 = makelineptpt(offp,p1)
	vis(l1)
	
	l2 = makelineptpt(offp,p2)
	vis(l2)
	
	
	l3 = makelineptpt(offp,p3)
	vis(l3)
	
	
	m1 = makelineptpt(p1,p2)
	vis(m1)
	
	m2 = makelineptpt(p2,p3)
	vis(m2)
	
	
	m3 = makelineptpt(p3,p1)
	vis(m3)
	
	midp1 = makepointoncurve(m1,0.5)
	vis(midp1)
	
	midp2 = makepointoncurve(m2,0.5)
	vis(midp2)
	
	midp3 = makepointoncurve(m3,0.5)
	vis(midp3)
	
	rail1 = makelineptpt(cp,midp1)
	vis(rail1)
	
	rail2 = makelineptpt(cp,midp2)
	vis(rail2)
	
	rail3 = makelineptpt(cp,midp3)
	vis(rail3)
	
	railp1 = makepointoncurve(rail1,ratio)
	vis(railp1)
	
	railp2 = makepointoncurve(rail2,ratio)
	vis(railp2)
	
	railp3 = makepointoncurve(rail3,ratio)
	vis(railp3)
	
	dotriangle(p1,offp,railp1)	
	dotriangle(p2,offp,railp1)
	
	dotriangle(p2,offp,railp2)	
	dotriangle(p3,offp,railp2)
	
	dotriangle(p3,offp,railp3)	
	dotriangle(p1,offp,railp3)

	
}


function dotriangle (tp1,tp2,tp3)
{
	tl1 = makelineptpt(tp1,tp2)
	tl2 = makelineptpt(tp2,tp3)
	tl3 = makelineptpt(tp3,tp1)
	
	tshapelist = makeshapelist()
	tshapelist = addshapetolist(tl1,tl2,tl3)
	tfill = makefillsrf(tshapelist)
	vis(tfill)
		
}


