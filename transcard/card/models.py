from django.db import models


class Card(models.Model):
	type = models.CharField("Тип", max_length=20)
	reason = models.CharField("Вид", max_length=10)
	inn = models.IntegerField("ИНН")
	name = models.CharField("Имя", max_length=50)
	surname = models.CharField("Фамилия", max_length=50)
	photo = models.ImageField(null=True, blank=True, upload_to='images/')
	pub_date = models.DateTimeField("date published", auto_now_add=True)
 
	def __str__(self):
		return str(self.inn)

	class Meta:
		verbose_name = 'Карточки'
		verbose_name_plural = 'Карточки'
		ordering = ["-pub_date"]
  
class Loadout(models.Model):
	st_xls = models.ImageField(null=True, blank=True)
	sch_xls = models.ImageField(null=True, blank=True)
	st_images = models.ImageField(null=True, blank=True)
	sch_images = models.ImageField(null=True, blank=True)
	pub_date = models.DateTimeField("date published", auto_now_add=True)
 
	def __str__(self):
		return str(self.pub_date)

	class Meta:
		verbose_name = 'Файлы'
		verbose_name_plural = 'Файлы'
		ordering = ["-pub_date"]

