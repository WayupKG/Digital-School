from django.utils.text import slugify
import transliterate


def get_translit(name):
	new_name = ''
	letters = {'ң': 'н', 'ү': 'y', 'ө': 'о'}
	for i in name.lower():
		try:
			if letters[i]:
				new_name += letters[i]
		except KeyError:
			new_name += i	
	try:
		translit = transliterate.translit(new_name, reversed=True)
	except:
		translit = new_name
	return slugify(translit, allow_unicode=True)