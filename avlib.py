
import os
import sys
from termcolor import colored

#def library_funktion(name):
#  print("gibt was aus " + name)


vertragsdaten = {
  "arbeitgeber": "Auto-Intern GmbH",
  "vertreter": "Stephan Bökelmann",
  "vorname": "Kalle",
  "nachname": "Grabowski",
  "geburtstag": '13.05.1971',
  "geburtsort": "Unna",
  "maanschriftStr": "Feldsieper Str.",
  "maanschriftNr": "75",
  "maanschriftPLZ": "44809",
  "maanschriftStadt": "Bochum",
  "krankenversicherung": "Asi KK",
  "rentenversicherungsnummer": "1130597O555",
  "konfession": "r. kat",
  "steuerklasse": "1",
  "kontoInstitut": "Volksbank Südmünsterland-Mitte eG",
  "kontoIBAN": "DE09 4016 4528 5555 6185 00",
  "kontoBIC": "GENODEM1LHN",
  "stunden": "3",
  "arbeitszeitBeginn": "09:00",
  "arbeitszeitEnde": "17:00",
  "beginn": "01.11.2021",
  "stellenbezeichnung": "Säufer",
  "aufgabe": "Trainer E-Jugend",
  "urlaub": "24",
  #"ende": "30.12.2022",
  "pauschal": "Mustang",
  "rente": "Mustang",
  "lohn": '9.999,-'
}


def print_dict_to_cmd(inp_dict):
    for key, value in inp_dict.items():
      print("Key : " + key + " entspricht " + value)


def generate_avpdf(configfile, templatefile, outputdir):
  os.system("cd "+str(outputdir)+" && pdflatex --jobname="+jobname+" "+str(templatefile)+" && rm *.aux *.log")

def write_dict_to_configfile(inputdict, outputfile):
  #datei leeren
  with open(outputfile, "w") as out:
    out.write("\\newcommand{\\white}{ }\n")
    out.close()

  with open(outputfile, "a") as out:
    for key, value in inputdict.items():
      out.write("\\newcommand{\\" + key + '}{' + value + '}\n')
    
    out.close()


def get_vertrags_input_from_cmd(vertrags_dict):
  vertrags_dict['vorname'] = input("Wie lautet ihr Vorname?: ")
  vertrags_dict['nachname'] = input("Wie lautet ihr Nachname?: ")
  vertrags_dict['geburtstag'] = input("Wann haben Sie Geburtstag?: ")
  vertrags_dict['geburtsort'] = input("Wie lautet ihr Geburtsort?: ")
  vertrags_dict['maanschriftStr'] = input("Geben Sie Ihre Adressea an: ")
  vertrags_dict['maanschriftNr'] = input("Geben Sie Ihre Hausnummer an: ")
  vertrags_dict['maanschriftPLZ'] = input("Wie lautet Ihre Postleitzahl?: ")
  vertrags_dict['maanschriftStadt'] = input("Geben Sie Ihre Stadt an: ")
  vertrags_dict['krankenversicherung'] = input("Geben Sie Ihre Krankenversicherung an: ")
  vertrags_dict['rentenversicherungsnummer'] = input("Geben Sie Ihre Rentenversicherung an: ")
  vertrags_dict['konfession'] = input("Geben Sie Ihre Konfession an: ")
  vertrags_dict['steuerklasse'] = input("Geben Sie Ihre Steuerklasse an: ")
  vertrags_dict['kontoInstitut'] = input("Geben Sie Ihre Bank an: ")
  vertrags_dict['kontoIBAN'] = input("Geben Sie Ihre IBAN an: ")
  vertrags_dict['kontoBIC'] = input("Geben Sie Ihre BIC an: ")
  vertrags_dict['stunden'] = input("Geben Sie Ihre Stunden an: ")
  vertrags_dict['arbeitszeitBeginn'] = input("Geben Sie Ihren Arbeitszeit Beginn an: ")
  vertrags_dict['arbeitszeitEnde'] = input("Geben Sie Ihre Arbeitszeit Ende an: ")
  vertrags_dict['beginn'] = input("Geben Sie Ihren Beginn an: ")
  vertrags_dict['stellenbezeichnung'] = input("Geben Sie Ihre Stellenbezeichnung an: ")
  vertrags_dict['urlaub'] = input("Geben Sie Ihre Urlaubstage an: ")
  vertrags_dict['aufgabe'] = input("Geben Sie Ihre Aufgaben an: ")
  vertrags_dict['pauschal'] = input("Geben Sie Ihre Pauschale an: ")
  vertrags_dict['rente'] = input("Geben Sie Ihre Rente an: ")
  vertrags_dict['lohn'] = input("Geben Sie Ihren Lohn an: ")
  print("++++++++++++++++++++++++++++\n")
  print(colored('Bitte kontrollieren Sie die eingegebenen Daten', 'green'))
  print_dict_to_cmd(vertrags_dict)
  print("Sind die eingegeben Daten korrekt?")
  print(colored('y','green'), colored('/','white'), colored('n','red'))
  correct = input("")
  if correct == 'n':
    print(colored('Abbruch','red'))
    sys.exit()
  else:
    return


