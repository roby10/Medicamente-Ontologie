#!/usr/bin/env python3

import os
import sys
import re
import time
import pickle
import json

import bs4
import requests

from owlready2 import *
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

onto = get_ontology("http://test.org/onto.owl")

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


with onto:
	#creates multiple classes
	ATC = types.new_class("ATC", (Thing,))
	ATCA = types.new_class("Tract_digestiv_si_metabolism", (ATC,))
	ATCB = types.new_class("Sange_si_organe_hematopoetice", (ATC,))
	ATCC = types.new_class("Sistemul_cardiovascular", (ATC,))
	ATCD = types.new_class("Preparate_dermatologice", (ATC,))
	ATCG = types.new_class("Aparat_genito-urinar_si_hormoni_sexuali", (ATC,))
	ATCH = types.new_class("Preparate_hormonale_sistemice", (ATC,))
	ATCJ = types.new_class("Antiinfecfioase_de_uz_sistemic", (ATC,))
	ATCL = types.new_class("Antineoplazice_si_imunomodulatoare", (ATC,))
	ATCM = types.new_class("Sistemul_musculo-scheletic", (ATC,))
	ATCN = types.new_class("Sistemul_nervos_central", (ATC,))
	ATCO = types.new_class("Produse_antiparazitare", (ATC,))
	ATCP = types.new_class("Aparatul_respirator", (ATC,))
	ATCR = types.new_class("Organe_senzitive", (ATC,))
	ATCS = types.new_class("Produse_antiparazitare", (ATC,))
	ATCV = types.new_class("Varia", (ATC,))	
	ATCX = types.new_class("Produse_fitoterapice_apiterapice_homeopate", (ATC,))



	#ATC1
	ATC11 = types.new_class("Preparate_stomatologice", (ATCA,))

	#ATC11
	ATC11AA = types.new_class("Produse_pentru_profilaxia_cariei", (ATC11,))
	ATC11AA1 = types.new_class("Fluorur??_de_sodiu", (ATC11AA,))
	ATC11AA2 = types.new_class("Monofluorofosfat_de_sodiu", (ATC11AA,))
	ATC11AA3 = types.new_class("Olaflur", (ATC11AA,))
	ATC11AA4 = types.new_class("Fluorur??_de_staniu", (ATC11AA,))
	ATC11AA5 = types.new_class("Combina??ii", (ATC11AA,))
	ATC11AA6 = types.new_class("Fluorur??_de_sodiu,combina??ii", (ATC11AA,))

	ATC11AB = types.new_class("Antiinfec??ioase_??i_antiseptice_pentru_tratament_oral_local", (ATC11,))
	ATC11AB1 = types.new_class("Peroxid_de_hidrogen", (ATC11AB,))
	ATC11AB2 = types.new_class("Clorhexidin??", (ATC11AB,))
	ATC11AB3 = types.new_class("Amfotericin??_B", (ATC11AB,))
	ATC11AB4 = types.new_class("Polinoxilin??", (ATC11AB,))
	ATC11AB5 = types.new_class("Domifen", (ATC11AB,))
	ATC11AB6 = types.new_class("Oxichinolon??", (ATC11AB,))
	ATC11AB7 = types.new_class("Neomicin??", (ATC11AB,))
	ATC11AB8 = types.new_class("Miconazol", (ATC11AB,))
	ATC11AB9 = types.new_class("Natamicin??", (ATC11AB,))
	ATC11AB10 = types.new_class("Varia", (ATC11AB,))
	ATC11AB11 = types.new_class("Hexetidin??", (ATC11AB,))
	ATC11AB12 = types.new_class("Tetraciclin??", (ATC11AB,))
	ATC11AB13 = types.new_class("Clorur??_de_benzoxoniu", (ATC11AB,))
	ATC11AB14 = types.new_class("Iodat_de_tibezoniu", (ATC11AB,))
	ATC11AB15 = types.new_class("Mepartricin??", (ATC11AB,))
	ATC11AB16 = types.new_class("Metronidazol", (ATC11AB,))
	ATC11AB17 = types.new_class("Clotrimazol", (ATC11AB,))
	ATC11AB18 = types.new_class("Perborat_de_sodiu", (ATC11AB,))
	ATC11AB19 = types.new_class("Doxiciclin??", (ATC11AB,))
	ATC11AB20 = types.new_class("Minociclin??", (ATC11AB,))

	ATC11AC = types.new_class("Corticosteroizi_pentru_tratament_oral_local", (ATC11,))
	ATC11AC1 = types.new_class("Triamcinolon??", (ATC11AC,))
	ATC11AC2 = types.new_class("Dexametazon??", (ATC11AC,))
	ATC11AC3 = types.new_class("Hidrocortizon", (ATC11AC,))
	ATC11AC4 = types.new_class("Prednisolon,combina??ii", (ATC11AC,))

	ATC11AD = types.new_class("Alte_preparate_pentru_tratament_oral_local", (ATC11,))
	ATC11AD1 = types.new_class("Epinefrin??", (ATC11AD,))
	ATC11AD1 = types.new_class("Benzidamin??", (ATC11AD,))
	ATC11AD1 = types.new_class("Acid_acetilsalicilic", (ATC11AD,))
	ATC11AD1 = types.new_class("Adrenalon??", (ATC11AD,))
	ATC11AD1 = types.new_class("Amlexanox", (ATC11AD,))
	ATC11AD1 = types.new_class("Varia", (ATC11AD,))
	####




	ATC12 = types.new_class("Medicamente_pentru_tulbur??ri_de_aciditate", (ATCA,))
	ATC13 = types.new_class("Medicamente_pentru_tulbur??ri_func??ionale_gastrointestinale", (ATCA,))
	ATC14 = types.new_class("Antiemetice", (ATCA,))
	ATC15 = types.new_class("Terapia_biliar?? ??i hepatic??", (ATCA,))
	ATC16 = types.new_class("Laxative", (ATCA,))
	ATC17 = types.new_class("Antidiareice_Antiinflamatoare_Antiinfec??ioase_intestinale", (ATCA,))
	ATC18 = types.new_class("Medica??ia_obezit????ii_exclusiv_produse_dietetice", (ATCA,))
	ATC19 = types.new_class("Substituen??i_??i_stimulante_ale_secre??iilor_digestive", (ATCA,))
	ATC110 = types.new_class("Antidiabetice", (ATCA,))
	ATC111 = types.new_class("Vitamine", (ATCA,))
	ATC112 = types.new_class("Substan??e minerale", (ATCA,))
	ATC113 = types.new_class("Tonice", (ATCA,))
	ATC114 = types.new_class("Anabolice_sistemice", (ATCA,))
	ATC115 = types.new_class("Stimulante_ale_apetitului", (ATCA,))
	ATC116 = types.new_class("Alte_produse_pentru_tractul_digestiv_??i_metabolism", (ATCA,))


	#ATC B

	ATCB1 = types.new_class("Antitrombotice", (ATCB,))
	ATCB2 = types.new_class("Antihemoragice", (ATCB,))
	ATCB3 = types.new_class("Atianemice", (ATCB,))
	ATCB4 = types.new_class("Substituen??i_de_s??nge_??i_solu??ii_perfuzabile", (ATCB,))
	ATCB5 = types.new_class("Alte_preparate_hematologice", (ATCB,))



	#ATC C

	ATCC1 = types.new_class("Terapia_cordului", (ATCC,))
	ATCC2 = types.new_class("Antihipertensive", (ATCC,))
	ATCC3 = types.new_class("Diuretice", (ATCC,))
	ATCC4 = types.new_class("Vasodilatatoare_periferice", (ATCC,))
	ATCC5 = types.new_class("Vasoprotectoare", (ATCC,))
	ATCC6 = types.new_class("Betablocante", (ATCC,))
	ATCC7 = types.new_class("Blocante_ale_canalelor_de_calciu", (ATCC,))
	ATCC8 = types.new_class("Produse_active_pe_sistemul_renin??-angiotensin??", (ATCC,))
	ATCC9 = types.new_class("Hipolipemiante", (ATCC,))



	#ATC D

	ATCD1 = types.new_class("Antifungice_de_uz_dermatologic", (ATCD,))
	ATCD2 = types.new_class("Emoliente_??i_protectoare", (ATCD,))
	ATCD3 = types.new_class("Preparate_pentru_tratamentul_r??nilor_??i_ulcerelor", (ATCD,))
	ATCD4 = types.new_class("Antipruriginoase_inclusiv_antihistaminice_??i_anestezice_locale", (ATCD,))
	ATCD5 = types.new_class("Antipsoriazice", (ATCD,))
	ATCD6 = types.new_class("Antibiotice_??i_chimioterapice_de_uz_dermatologic", (ATCD,))
	ATCD7 = types.new_class("Corticosteroizi_preparate_dermatologice", (ATCD,))
	ATCD8 = types.new_class("Antiseptice_??i_dezinfectante", (ATCD,))
	ATCD9 = types.new_class("Preparate_antiacneice", (ATCD,))
	ATCD10 = types.new_class("Pansamente_medicamentoase", (ATCD,))
	ATCD11 = types.new_class("Alte_preparate_de_uz_dermatologic", (ATCD,))



	#ATC G

	ATCG1 = types.new_class("Antiinfec??ioase_??i_antiseptice_ginecologice", (ATCG,))
	ATCG2 = types.new_class("Alte_preparate_ginecologice", (ATCG,))
	ATCG3 = types.new_class("Hormoni_sexuali_??i_modulatorii_sistemului_genital", (ATCG,))
	ATCG4 = types.new_class("Medica??ia_aparatului_urinar", (ATCG,))

	#ATC H

	ATCH1 = types.new_class("Hormoni_hipofizari_hipotalamici_??i_analogi", (ATCH,))
	ATCH2 = types.new_class("Corticosteroizi_de_uz_sistemic", (ATCH,))
	ATCH3 = types.new_class("Terapia_tiroidei", (ATCH,))
	ATCH4 = types.new_class("Hormoni_pancreatici", (ATCH,))
	ATCH5 = types.new_class("Preparate_pentru_homeostazia_calciului", (ATCH,))

	#ATC J

	ATCJ1 = types.new_class("Antibacteriene_de_uz_sistemic", (ATCJ,))
	ATCJ2 = types.new_class("Antimicotice_de_uz_sistemic", (ATCJ,))
	ATCJ3 = types.new_class("Antimicobacteriene", (ATCJ,))
	ATCJ4 = types.new_class("Antivirale_de_uz_sistemic", (ATCJ,))
	ATCJ5 = types.new_class("Imunoseruri_??i_imunoglobuline", (ATCJ,))
	ATCJ6 = types.new_class("Vaccinuri", (ATCJ,))


	#ATC L

	ATCL1 = types.new_class("Antineoplazice", (ATCL,))
	ATCL2 = types.new_class("Terapia_endocrin??", (ATCL,))
	ATCL3 = types.new_class("Imunostimulante", (ATCL,))
	ATCL4 = types.new_class("Imunosupresoare", (ATCL,))

	#ATC M

	ATCM1 = types.new_class("Preparate_antiinflamatoare_??i_antireumatice", (ATCM,))
	ATCM2 = types.new_class("Preparate_topice_pentru_algii_articulare_??i_musculare", (ATCM,))
	ATCM3 = types.new_class("Miorelaxante", (ATCM,))
	ATCM4 = types.new_class("Antigutoase", (ATCM,))
	ATCM5 = types.new_class("Medicamante_pentru_tratamentul_afec??iunilor_oaselor", (ATCM,))
	ATCM6 = types.new_class("Alte_medicamente_pentru_afec??iuni_ale_sistemului_musculo-scheletic", (ATCM,))

	#ATC N

	ATCN1 = types.new_class("Anestezice", (ATCN,))
	ATCN2 = types.new_class("Analgezice", (ATCN,))
	ATCN3 = types.new_class("Antiepileptice", (ATCN,))
	ATCN4 = types.new_class("Antiparkinsoniene", (ATCN,))
	ATCN5 = types.new_class("Psiholeptice", (ATCN,))
	ATCN6 = types.new_class("Psihoanaleptice", (ATCN,))
	ATCN7 = types.new_class("Alte_preparate_cu_ac??iune_asupra_sistemului_nervos", (ATCN,))

	#ATC P

	ATCP1 = types.new_class("Antiprotozoare", (ATCP,))
	ATCP2 = types.new_class("Antihelmintice", (ATCP,))
	ATCP3 = types.new_class("Ectoparaziticide_inclusiv_scabicide_insecticide", (ATCP,))


	#ATC R

	ATCR1 = types.new_class("Preparate_nazale", (ATCR,))
	ATCR2 = types.new_class("Preparate_pentru_zona_oro-faringian??", (ATCR,))
	ATCR3 = types.new_class("Medicamente_pentru_bolile_obstructive_ale_c??ilor_respiratorii", (ATCR,))
	ATCR4 = types.new_class("Preparate_pentru_tratamentul_tusei_??i_r??celii", (ATCR,))
	ATCR5 = types.new_class("Antihistaminice_de_uz_sistemic", (ATCR,))
	ATCR6 = types.new_class("Alte_preparate_pentru_aparatul_respirator", (ATCR,))


	#ATC S

	ATCP1 = types.new_class("Produse_oftalmologice", (ATCS,))
	ATCP2 = types.new_class("Produse_otologice", (ATCS,))
	ATCP3 = types.new_class("Produse_oftalmologice_??i_otologice", (ATCS,))


	#ATC V

	ATCV1 = types.new_class("Alergeni", (ATCV,))
	ATCV2 = types.new_class("Alte_produse_terapeutice", (ATCV,))
	ATCV3 = types.new_class("Agen??i_de_diagnostic", (ATCV,))
	ATCV4 = types.new_class("Produse_dietetice", (ATCV,))
	ATCV5 = types.new_class("Alte_produse_neterapeutice", (ATCV,))
	ATCV6 = types.new_class("Medii_de_contrast", (ATCV,))
	ATCV7 = types.new_class("Radiofarmaceutice_pentru_diagnostic", (ATCV,))
	ATCV8 = types.new_class("Radiofarmaceutice_terapeutice", (ATCV,))
	ATCV9 = types.new_class("Pansamente_chirurgicale", (ATCV,))


	#ATC X

	ATCX1 = types.new_class("Produse_fitoterapice", (ATCX,))
	ATCX2 = types.new_class("Produse_homeopate", (ATCX,))




	#for i in range(10):
	#	name = "classTTTTTT" + str(i)
	#	NewClass = types.new_class(name, (Thing,))


if __name__ == '__main__':
   
   lis = [x[0] for x in os.walk("C:/Users/roby/Desktop/master/AWS/data")]
   #print(lis)

   DCI = []
   form = []
   reactii = []

   for dir in lis[1:]:
   	with open(dir + "/Data.json") as jsf:
   		print(dir)

   		data = json.load(jsf)
   		#DCI data
   		DCI.append(data['DCI'])
   		#form data
   		form.append(data['Forma farmaceutica'])


   		extracted_text = convert_pdf_to_txt(dir + '/Prospect.pdf')
   		#todo merge all
   		extracted_text = extracted_text.replace('??', 'a')
   		extracted_text = extracted_text.replace('??', 'A')
   		extracted_text = extracted_text.replace('??', 'a')
   		extracted_text = extracted_text.replace('??', 'A')
   		extracted_text = extracted_text.replace('??', 'i')
   		extracted_text = extracted_text.replace('??', 'i')   		
   		extracted_text = extracted_text.replace('??', 'i')
   		extracted_text = extracted_text.replace('??', 's')
   		extracted_text = extracted_text.replace('??', 'S')
   		extracted_text = extracted_text.replace('??', 't')
   		extracted_text = extracted_text.replace('??', 'T')
   		extracted_text = extracted_text.replace('??', 't')
   		extracted_text = extracted_text.replace('??', 'T')
   		extracted_text = extracted_text.replace('??', 's')
   		extracted_text = extracted_text.replace('??', 'S')
   		extracted_text = extracted_text.replace('\uf03c', '')
   		extracted_text = extracted_text.replace('\uf0b7', '')

   		start = 'Reactii adverse posibile'
   		end = 'Raportarea reactiilor adverse'

   		print(extracted_text.rfind(start))
   		print(extracted_text.rfind(end))


   		res = extracted_text[extracted_text.rfind(start)+len(start):extracted_text.rfind(end)]
   		print("------===========================================-------")
   		res = res.replace(r'\n\n', '\n')
   		lis = re.findall("^[-][ ][a-zA-z, ]*", res, re.MULTILINE)
   		lis = [item[2:] for item in lis if len(item)>3]

   		reactii.append(lis)

   		print("------===========================================-------")

   DCI = set(DCI)
   print(set(form))
   print(set(reactii))

#medicamente
with onto:
   medclass = types.new_class("Medicamente", (Thing,))
   for med in DCI:

   	med = med.replace(' ', '_')
   	med = med.replace('(', '').replace(')', '')
   	objclass = types.new_class(med, (medclass,))

#forma comprimate
with onto:
   formclass = types.new_class("FormaFarmaceutica", (Thing,))
   for forma in form:

   	forma = forma.replace(' ', '_')
   	forma = forma.replace('(', '').replace(')', '')
   	objclass = types.new_class(forma, (formclass,))



   onto.save(file = "C:/Users/roby/Desktop/master/AWS/Onto.rdf", format = "rdfxml")