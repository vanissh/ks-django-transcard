import datetime
import os
import xlwt
from zipfile import ZipFile

from .models import Card, Loadout


def makedirs(data, media, catalogs):
	for i in catalogs:
		if not os.path.isdir(i):
			os.mkdir(i)


def MyCronJob():
	date = datetime.datetime.utcnow().strftime("%m%d")
	media = 'media/'

	def xl_wirte(self, dest, card):
		dest.write(dest, 0, card.type)
		dest.write(dest, 1, card.reason)
		dest.write(dest, 2, card.name)
		dest.write(dest, 3, card.surname)
		dest.write(dest, 4, card.inn)
		dest.write(dest, 5, card.phone)
		dest.write(dest, 6, card.pay_method)

	def relocate_image(self, dest, source, card):
		if os.path.isfile(source) and not os.path.isfile(dest):
			os.replace(source, dest)
			card.photo.name = dest
			card.save()


	#Create a catalog for new images
	makedirs(date, media, (media, media+date, media+f'{date}/st', media+f'{date}/sch'))

	loadout = Loadout.objects.filter(pub_date__gte=datetime.datetime.now().replace(hour=0,minute=0,second=0))

	#Load CardModels from a db
	cards = Card.objects.all()

	#Write data to an excel file and copy images
	st_book = xlwt.Workbook(encoding="utf-8")
	sch_book = xlwt.Workbook(encoding="utf-8")
	st_sheet = st_book.add_sheet("St")
	sch_sheet = sch_book.add_sheet("Sch")
	st_row = 0
	sch_row = 0
	st_zip = ZipFile(media + f"{date}/st.zip", 'w')
	sch_zip = ZipFile(media + f"{date}/sch.zip", 'w')
	st_path = media+f'{date}/st'
	sch_path = media+f'{date}/sch'
	for card in cards:
		if card.pub_date.strftime("%m%d") == date:
			if card.type == 'Школьная':
				self.xl_write(sch_sheet, card)
				self.relocate_image(media+str(card.photo), sch_path+f'/{str(card.inn)+str(card.photo)[-4:]}')
				sch_zip.write(card.photo.name)
				sch_row+=1
				continue
			if card.type == 'Студенческая':
				self.xl_write(st_sheet, card)
				self.relocate_image(media+str(card.photo), st_path+f'/{str(card.inn)+str(card.photo)[-4:]}')
				st_zip.write(card.photo.name)
				st_row+=1
				continue
		break
	st_zip.close()
	sch_zip.close()
	st_book.save(st_path+'.xls')
	sch_book.save(sch_path+'.xls')

	if loadout.count() == 0:
		loadout = Loadout()
		loadout.st_xls=st_path+'.xls'
		loadout.sch_xls=sch_path+'.xls'
		loadout.st_images=st_path+'.zip'
		loadout.sch_images=sch_path+'.zip'
		loadout.save()
