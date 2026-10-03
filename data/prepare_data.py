import json,math
D='d3-celestial/data/'
L=lambda f: json.load(open(D+f))['features']
def ra(x): return round(x%360,3)
# constellations: id -> name, label pos, rank
cons=[]; seen=set()
for f in L('constellations.json'):
    i=f['id']
    if i in seen: continue
    seen.add(i); p=f['properties']; c=f['geometry']['coordinates']
    cons.append([i,p['name'],ra(c[0]),round(c[1],2),int(p['rank'])])
# lines
lines={}
for f in L('constellations.lines.json'):
    lines.setdefault(f['id'],[]).extend([[[ra(a),round(b,3)] for a,b in seg] for seg in f['geometry']['coordinates']])
# bounds, densified linearly in ra/dec to <=1.5deg steps (approximates B1875 parallels)
bounds=[]
for f in L('constellations.bounds.json'):
    ring=f['geometry']['coordinates'][0]
    out=[]
    for k in range(len(ring)-1):
        (a0,d0),(a1,d1)=ring[k],ring[k+1]
        da=((a1-a0+540)%360)-180
        n=max(1,int(math.ceil(max(abs(da),abs(d1-d0))/1.5)))
        for j in range(n):
            t=j/n; out.append([ra(a0+da*t),round(d0+(d1-d0)*t,3)])
    bounds.append([f['id'],out])
# stars
names=json.load(open(D+'starnames.json'))
stars=[]
for f in L('stars.6.json'):
    m=f['properties']['mag']
    if m>5.3: continue
    a,b=f['geometry']['coordinates']
    nm=names.get(str(f['id']),{}).get('name','') if m<2.6 else ''
    try: bv=round(float(f['properties']['bv']),2)
    except: bv=0.6
    s=[ra(a),round(b,3),m,bv]
    if nm: s.append(nm)
    stars.append(s)
stars.sort(key=lambda s:s[2])
data={'cons':cons,'lines':lines,'bounds':bounds,'stars':stars}
js=json.dumps(data,separators=(',',':'),ensure_ascii=False)
open('skydata.json','w').write(js)
print(len(cons),len(stars),sum(1 for s in stars if len(s)>4),len(js)//1024,'KB', sum(len(b[1]) for b in bounds))
# brightest named-or-designated star per constellation
best={}
for f in L('stars.6.json'):
    n=names.get(str(f['id']));
    if not n: continue
    c=n.get('c');
    if not c: continue
    m=f['properties']['mag']
    if c not in best or m<best[c][1]:
        label=n['name'] or ((n['bayer'] or n['flam'] or n['desig'] or '')+' '+c).strip()
        best[c]=[label,m]
for c in data['cons']:
    b=best.get(c[0]); c.append(b[0] if b else ''); c.append(b[1] if b else None)
js=json.dumps(data,separators=(',',':'),ensure_ascii=False)
open('skydata.json','w').write(js)
print([c for c in data['cons'] if c[0] in ('Ori','UMa','Cru','Ser','Lyr')])
