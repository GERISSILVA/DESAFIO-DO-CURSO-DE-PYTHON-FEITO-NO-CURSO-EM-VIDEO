from datetime import date
ano = int(input('Qual ano você que analisar? (Digite 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('{} é Bissexto'.format(ano))
else:
    print('{} Não é bissexto'.format(ano))
