"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

big_text = "'Герой нашего времени', Фаталист" \
           "Я возвращался домой пустыми переулками станицы; месяц, полный и красный, как зарево пожара, " \
           "начинал показываться из-за зубчатого горизонта домов; звезды спокойно сияли на темно-голубом своде," \
           "и мне стало смешно, когда я вспомнил, что были некогда люди премудрые, думавшие, что светила небесные" \
           "принимают участие в наших ничтожных спорах за клочок земли или за какие-нибудь вымышленные права!.. " \
           "И что ж? эти лампады, зажженные, по их мнению, только для того, чтобы освещать их битвы и торжества, " \
           "горят с прежним блеском, а их страсти и надежды давно угасли вместе с ними, как огонек, зажженный на краю" \
           "леса беспечным странником! Но зато какую силу воли придавала им уверенность, что целое небо со своими" \
           "бесчисленными жителями на них смотрит с участием, хотя немым, но неизменным!.. А мы, их жалкие потомки," \
           "скитающиеся по земле без убеждений и гордости, без наслаждения и страха, кроме той невольной боязни," \
           "сжимающей сердце при мысли о неизбежном конце, мы не способны более к великим жертвам ни для блага " \
           "человечества, ни даже для собственного счастия, потому знаем его невозможность и равнодушно переходим" \
           "от сомнения к сомнению, как наши предки бросались от одного заблуждения к другому, не имея, как они, ни" \
           "надежды, ни даже того неопределенного, хотя и истинного наслаждения, которое встречает душа во всякой" \
           "борьбе с людьми или судьбою..."

get_dict = {}
big_text_list = big_text.lower().split()
big_text_list_new = [''.join(filter(str.isalpha, a)) for a in
                     big_text_list]  # убираем все ненужное: символы, цифры, оставляя только слова

while '' in big_text_list_new:
    big_text_list_new.remove('')

for word in big_text_list_new:
    get_dict.setdefault(word, big_text_list_new.count(word))

count_words = 1
while count_words <= 10:
    count_words += 1
    max_key = max(get_dict, key=get_dict.get)
    print(f'{max_key:>5}  =  {get_dict[max_key]}')
    get_dict.pop(max_key)
