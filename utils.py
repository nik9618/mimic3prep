def findUnitGroup(unit):
    unitgroup = [
        {'kg':10**-3,
         'gm':1,
         'g':1,
         'grams':1,
         'mg':10**3,
         'mcg':10**6,
         'ng':10**9,
         'pg':10**12},

        {'l':10**-3,
         'ml':1,
         '?l':10**-3},

        {'mu':1,
         'million units':1}
    ]
    unit = unit.replace(' ','').lower()
    for i in unitgroup:
        if(unit in i): return i
    return {}

def writeline(f,s):
    f.write(s+'\n')

def parseNum(s):
    import numpy as np
    import re
    try:
        num = float(s);
        return num
    except:
        res = re.findall(r"\d*\.\d*|\d+\-\d*\.\d*|\d+", s)
        
        try:
            if(len(res) > 2 ):
                return None;
            else:
                return (float(res[0]) + float(res[1]))/2.
        except:
            res = re.findall(r"[-+]?\d*\.\d+|\d+", s)
            nums = [];
            for r in res:
                try:
                    nums.append(float(r))
                except:
                    pass;

            if(len(nums) == 0):
                return None;

            nums = np.array(nums).mean()    
            return nums

def sparsify(mat):
    coocode = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j]==None):
                continue;
            else:
                coocode.append((i,j,mat[i][j]))                
    return {'timestep':len(mat),'features':len(mat[0]),'codes':coocode};

def coodecode(coocode,f,t):
    mat = []
    for i in range(t):
        mat.append([None]*f);
     
    for c in coocode:
        mat[c[0]][c[1]] = c[2]
    
    return mat;
        