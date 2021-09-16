my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet. Matej1.vlk@gmail.com'''
import pprint as pp

def vyber_maily(seznam):
    ''' Function that splits string to list and finds and returns substrings with @'''
    seznam = my_str.split()
    maily = [text.strip('.') for text in seznam if '@' in text]
    return maily


def cisla_v_mailu(seznam_mailu):
    ''' finds all emails with numbers in it from the the list of emails created with the funtion vyber_maily(seznam)'''
    emails_with_nums = [i for i in seznam_mailu if '1' in i or '2' in i or '3' in i or '4' in i or '5' in i or '6' in i 
    or'7' in i or '8' in i or '9' in i or '0' in i]
    return emails_with_nums
    
#Alternativesolution for deciding if there is a number in email
    #for num in range(10):
    #    if str(num) in _string:
     #       return True

def domeny(seznam_mailu):
    '''Function finding and creating and returning list of domains'''
    list_tuplu = [i.partition('@') for i in seznam_mailu]
    domeny = [i[2] for i in list_tuplu]
    return domeny


def main(seznam):
    '''Main function combinating both function above launching the program. 
    Outcome of this main function is a dictionary of domains and emails with nums
    '''
    slovnik = {'domains': domeny(vyber_maily(seznam)), 'emails_with_nums': cisla_v_mailu(vyber_maily(seznam))}
    return slovnik

pp.pprint(main(my_str))