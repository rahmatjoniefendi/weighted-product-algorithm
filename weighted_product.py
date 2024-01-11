KRITERIA_BENEFIT = 0
KRITERIA_COST = 1

def perbaikan_bobot(w, index, digits=2):
    r = w[index] / sum(w)
    return round(r, digits)

def cari_nilai_vector_i(row, w, kriteria, digits=2):
    r = 1
    for i in range(len(row)):
        if kriteria[i] == KRITERIA_BENEFIT:
            v = perbaikan_bobot(w, i, digits)
            r *= row[i] ** v
        elif kriteria[i] == KRITERIA_COST:
            v = perbaikan_bobot(w, i, digits)
            r *= row[i] ** (-v)
    return round(r, digits)

def s(rows, w, kriteria, digits=2):
    r = []
    for i in range(len(rows)):
        r.append(cari_nilai_vector_i(rows[i], w, kriteria, digits))

    return r

def cari_nilai_preferensi(rows, w, kriteria, index, digits=2):
    r = s(rows, w, kriteria, digits=2)[index] / sum(s(rows, w, kriteria, digits=2))
    return r

def print_kriteria(kriteria):
    print('+---------------------------------------------------------------+')
    print('|                            TAHAP 1                            |')
    print('+---------------------------------------------------------------+')

    for i in kriteria:
        if kriteria == KRITERIA_BENEFIT:
            print('1. Kriteria BENEFIT:')
            print('\t-C' + i)
            
    print()

    for i in kriteria:
        if kriteria == KRITERIA_COST:
            print('2. Kriteria COST:')
            print('\t-C' + i)

def print_bobot(w, digits=2):
    print('+---------------------------------------------------------------+')
    print('|                  TAHAP 2 : PERBAIKAN BOBOT                    |')
    print('+---------------------------------------------------------------+')
    for index in range(len(w)):        
        print('\t'+ str(w[index]).rjust(17)+ '                 ' +str(w[index]))
        print('\t------------------------------ = ------- = ' +
              str(round(perbaikan_bobot(w, index, digits), digits)))
        print('\t'+ str('sum({})          {}'.format(w, sum(w)).rjust(17)))
        print()

def print_nilai_vector_i(rows, w, kriteria, digits=2):
    i = 1
    for row in rows:
        print('\n\tS' + str(i) + '   |   ' + str(cari_nilai_vector_i(row, w, kriteria, digits)))
        i += 1

def print_nilai_vector(rows, w, kriteria, digits=2):
    print('\n+---------------------------------------------------------------+')
    print('|                  TAHAP 3 : NILAI VEKTOR Si                    |')
    print('+---------------------------------------------------------------+')

    r = 1
    index = 1
    for row in rows:
        print('S'+ str(index) + ' = ', end='')
        for i in range(len(row)):
            if kriteria[i] == KRITERIA_BENEFIT:
                v = perbaikan_bobot(w, i, digits)
                r *= row[i] ** v
                print('(' + str(row[i]) + ' ** ' + str(v) + ')' , end='')
            elif kriteria[i] == KRITERIA_COST:
                v = perbaikan_bobot(w, i, digits)
                r *= row[i] ** (-v)
                print('(' + str(row[i]) + ' ** ' + '-' + str(v) + ')' , end='')
        index+=1
                
        print()

def print_nilai_preferensi(rows, w, kriteria, digits=2):
    print('\n+---------------------------------------------------------------+')
    print('|                      TAHAP 4 : PREFERENSI                     |')
    print('+---------------------------------------------------------------+')

    for index in range(len(rows)):
        print('\t'+ str(s(rows, w, kriteria, digits)[index]).rjust(27)+ '                 ' +str(s(rows, w, kriteria, digits)[index]))
        print('V' + str(index+1) + ' = ---------------------------------------- = ------- = ' +
              str(round(cari_nilai_preferensi(rows, w, kriteria, index, digits), digits)))
        print('\t'+ str('sum({})            {}'.format(s(rows, w, kriteria, digits), round(sum(s(rows, w, kriteria, digits)), digits)).rjust(17)))
        print()

def print_all(rows, w, kriteria, digits=2):
    print_kriteria(kriteria)
    print_bobot(w, digits)
    print_nilai_vector(rows, w, kriteria, digits)
    print_nilai_vector_i(rows, w, kriteria, digits)
    print_nilai_preferensi(rows, w, kriteria, digits)

def demo_1():
    w = [5, 2, 4, 3, 2]

    kategori = [KRITERIA_BENEFIT, KRITERIA_COST, KRITERIA_BENEFIT, KRITERIA_BENEFIT, KRITERIA_COST]

    rows = [
        [42, 66000, 60, 75, 2355],
        [50, 90000, 72, 60, 1421],
        [63, 91500, 65, 80, 2585]
    ]

    print_all(rows, w, kategori, 6)

def demo_2():
    w = [5, 3, 4, 4, 2]

    kategori = [
        KRITERIA_COST,
        KRITERIA_BENEFIT,
        KRITERIA_COST,
        KRITERIA_BENEFIT,
        KRITERIA_COST
    ]
    
    rows = [
        [0.75, 2000, 18, 50, 500],
        [0.50, 1500, 20, 40, 450],
        [0.90, 2050, 35, 35, 800]
    ]

    print_all(rows, w, kategori, 4)

def demo_3():
    w = [4, 1, 2, 3 , 5]

    kategori = [KRITERIA_BENEFIT,
                KRITERIA_BENEFIT,
                KRITERIA_BENEFIT,
                KRITERIA_BENEFIT,
                KRITERIA_BENEFIT
    ]
    rows = [
        [0.75,  0.25,  0.2, 0.25, 0.25],
        [1,     0.25,  0.4,    0,    1],
        [0.5,   0.5,   0.8, 0.75, 0.25],
        [1,     1,     1,   1,       1],
        [0.25,  0.25,  0,   0,       0]
    ]

    print_all(rows, w, kategori, 4)

if __name__ == '__main__':
    demo_3()