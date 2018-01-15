import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.add_state('9')
    f.add_state('10')
    f.add_state('11')
    f.add_state('12')
    f.add_state('13')
    f.add_state('14')
    f.add_state('15')
    f.add_state('16')
    # f.add_state('17')
    # f.add_state('18')
    # f.add_state('19')
    # f.add_state('20')
    # f.add_state('21')
    # f.add_state('22')


    f.initial_state = 'start'

    f.set_final('4')
    f.set_final('6')
    f.set_final('7')
    f.set_final('9')
    # f.set_final('13')
    # f.set_final('14')
    # f.set_final('15')
    f.set_final('12')
    f.set_final('16')
    # f.set_final('17')
    # f.set_final('18')
    # f.set_final('20')
    # f.set_final('21')
    # f.set_final('22')

    #takes care of single digit
    f.add_arc('start', '2', '0', ())
    f.add_arc('2', '3', '0', ())
    for digit in range(0,10):
        f.add_arc('3', '4', [str(digit)],[kFRENCH_TRANS[digit]])

    #Two-digits -in range (10,16)

    f.add_arc('2', '5', '1', ())
    for digit in range(0,7):
        f.add_arc('5','6',[str(digit)],[kFRENCH_TRANS[digit+10]])


    #takes care of 17,18,19    
    for digit in range(7,10):
        f.add_arc('5','7',[str(digit)],[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[digit]]) 


    #takes care of 20
    for digit in range(2,7):
        f.add_arc('2','8',[str(digit)],[kFRENCH_TRANS[digit*10]])

    f.add_arc('8','9','0',())

    #takes care of 21-29(Takes care of 20 to 60)
    for digit in range(1,10): 
        if digit==1:
            f.add_arc('8','4',[str(digit)],[kFRENCH_AND]+[kFRENCH_TRANS[digit]])
        else:
            f.add_arc('8','4',[str(digit)],[kFRENCH_TRANS[digit]])



    #takes care of 70-79
    f.add_arc('2','10','7',[kFRENCH_TRANS[60]])

    for digit in range(0,7):
        if digit==1:
            f.add_arc('10','6',[str(digit)],[kFRENCH_AND]+[kFRENCH_TRANS[digit+10]])
        else:
            f.add_arc('10','6',[str(digit)],[kFRENCH_TRANS[digit+10]])

    for digit in range(7,10):
            f.add_arc('10','7',[str(digit)],[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[digit]])


    #takes care of 80-89
    f.add_arc('2','11','8',[kFRENCH_TRANS[4]]+[kFRENCH_TRANS[20]])
    #takes care of 80
    f.add_arc('11','12','0',())
    for digit in range(1,10): 
        f.add_arc('11','4',[str(digit)],[kFRENCH_TRANS[digit]])


    #takes care of 90-99
    f.add_arc('2','13','9',[kFRENCH_TRANS[4]]+[kFRENCH_TRANS[20]])
    for digit in range(0,7): 
        f.add_arc('13','6',[str(digit)],[kFRENCH_TRANS[digit+10]]) 


    for digit in range(7,10):
        f.add_arc('13','7',[str(digit)],[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[digit]]) 


    #takes care of 100
    f.add_arc('start','14','1',['cent'])

    f.add_arc('14','15','0',())
    f.add_arc('15','16','0',())

    #takes care of 101-109
    for digit in range(1,10):
        f.add_arc('15','4',[str(digit)],[kFRENCH_TRANS[digit]])

    #takes care of 110-119
    f.add_arc('14','5','1',())

    #takes care of 120-169
    for digit in range(2,7):
        f.add_arc('14','8',[str(digit)],[kFRENCH_TRANS[digit*10]])

    #takes care of 170-179
    f.add_arc('14','10','7',[kFRENCH_TRANS[60]])


    #takes care of 180-189
    f.add_arc('14','11','8',[kFRENCH_TRANS[4]]+[kFRENCH_TRANS[20]])

    #takes care of 190-199
    f.add_arc('14','13','9',[kFRENCH_TRANS[4]]+[kFRENCH_TRANS[20]])


    #takes care of 200-999
    for digit in range(2,10):
        f.add_arc('start','14',[str(digit)],[kFRENCH_TRANS[digit]]+['cent'])


    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))




