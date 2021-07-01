import datetime
import os
import xlwt
from zipfile import ZipFile

from .models import Card, Loadout

def MyCronJob():
	#Create a catalog for new images
	media = 'media/'
	date = datetime.datetime.utcnow().strftime("%m%d")
	try:
		os.mkdir(media+date)
	except FileExistsError:
		print('directory exists')
	try:
		os.mkdir(media+f'{date}/{date}st')
	except FileExistsError:
		print('directory exists')
	try:
		os.mkdir(media+f'{date}/{date}sch')
	except FileExistsError:
		print('directory exists')

	#Load CardModels from a db
	cards = Card.objects.all()
	
	#Write data to an excel file and copy images
	st_book = xlwt.Workbook(encoding="utf-8")
	sch_book = xlwt.Workbook(encoding="utf-8")
	st_sheet = st_book.add_sheet("St")
	sch_sheet = sch_book.add_sheet("Sch")
	st_row = 0
	sch_row = 0
	st_zip = ZipFile(media+f"{date}/{date}st.zip", 'w')
	sch_zip = ZipFile(media+f"{date}/{date}sch.zip", 'w')
	for card in cards:
		print(card.pub_date.strftime("%m%d"), date)
		if card.pub_date.strftime("%m%d") == date:
			if card.type == 'Школьная':
				sch_sheet.write(sch_row, 0, card.type)
				sch_sheet.write(sch_row, 1, card.reason) 
				sch_sheet.write(sch_row, 2, card.name) 
				sch_sheet.write(sch_row, 3, card.surname) 
				sch_sheet.write(sch_row, 4, card.inn)
				try:
					os.replace("media/"+str(card.photo), media+f"{date}/{date}sch/{str(card.inn)+str(card.photo)[-4:]}")
					card.photo.name = f"{date}/{date}sch/{str(card.inn)+str(card.photo)[-4:]}"
					card.save()
					sch_zip.write(card.photo.name)
				except FileNotFoundError:
					print("Файл media/"+str(card.photo)+' не существует')
					try:
						sch_zip.write(media+f"{date}/{date}sch/{str(card.inn)+str(card.photo)[-4:]}")
					except FileNotFoundError:
						print("Файл media/"+f"{date}/{date}sch/{str(card.inn)+str(card.photo)[-4:]}"+' не существует')
				sch_row+=1
				continue
			if card.type == 'Студенческая':
				st_sheet.write(st_row, 0, card.type)
				st_sheet.write(st_row, 1, card.reason) 
				st_sheet.write(st_row, 2, card.name) 
				st_sheet.write(st_row, 3, card.surname) 
				st_sheet.write(st_row, 4, card.inn)
				try:
					os.replace("media/"+str(card.photo), media+f"{date}/{date}st/{str(card.inn)+str(card.photo)[-4:]}")
					card.photo.name = f"{date}/{date}st/{str(card.inn)+str(card.photo)[-4:]}"
					card.save()
					st_zip.write(card.photo.name)
				except FileNotFoundError:
					print("Файл media/"+str(card.photo)+' не существует')
					try:
						st_zip.write(media+f"{date}/{date}st/{str(card.inn)+str(card.photo)[-4:]}")
					except FileNotFoundError:
						print("Файл media/"+f"{date}/{date}st/{str(card.inn)+str(card.photo)[-4:]}"+' не существует')
				sch_row+=1
				continue
		break
	st_zip.close()
	sch_zip.close()
	st_book.save(media+f"{date}/{date}st.xls")
	sch_book.save(media+f"{date}/{date}sch.xls")
	#Create ResultModel
	if not os.path.isdir(f'media/{date}'):
		loadout = Loadout()
		loadout.st_xls = f"{date}/{date}st.xls"
		loadout.sch_xls = f"{date}/{date}sch.xls"
		loadout.st_images = f"{date}/{date}st.zip"
		loadout.sch_images = f"{date}/{date}sch.zip"
		loadout.save()
