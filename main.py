import xmltodict
import json


def xml_to_list_of_dicts(xml_string):
    data_dict = xmltodict.parse(xml_string)

    root_key = next(iter(data_dict))
    data_list = data_dict[root_key]

    json_data = json.dumps(data_list, indent=2)

    return json_data

xml_string = """
<yml_catalog date="2024-01-09T00:56">
<shop>
<name>Московский Дом Мебели</name>
<company>ООО "Мосдоммебель Ритейл"</company>
<url>https://www.mosdommebel.ru/</url>
<platform>Webasyst Shop-Script</platform>
<version>10.0.2</version>
<currencies>
<currency id="RUB" rate="1"/>
</currencies>
<categories>
<category id="2005">Шкафы</category>
</categories>
<offers>
<offer id="21196" group_id="20085">
<name>Бриз 9 Шкаф для белья, склад</name>
<vendor>ГЛАЗОВ МЕБЕЛЬ</vendor>
<vendorCode>76839</vendorCode>
<price>8570.10</price>
<shop-sku>76839</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>52.00</weight>
<box-count>2</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>40.000/59.000/213.500</dimensions>
<url>https://www.mosdommebel.ru/product/9-shkaf-dlja-belja/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/85/00/20085/images/25100/25100.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Бриз 9 Шкаф для белья &mdash; одностворчатый шкаф с полками. Материал ЛДСП, декор Ясень Анкор темный / Бодега светлая.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Вес" unit="кг">52</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">59</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">213.5</param>
<param name="Ширина">40</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Цвет фасада">Бодега светлый</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Назначение шкафа">Для белья</param>
<param name="Коллекция">Бриз</param>
<param name="Цвет корпуса">Ясень Анкор Темный</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Прованс</param>
<param name="Количество упаковок">2</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,098</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">4</param>
</offer>
<offer id="32132" group_id="30543">
<name>Оскар 7А Пенал штанга, сонома, склад</name>
<vendor>Стиль</vendor>
<vendorCode>72141A</vendorCode>
<price>8681.40</price>
<shop-sku>72141A</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>55.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>55.000/38.600/208.800</dimensions>
<url>https://www.mosdommebel.ru/product/oskar-7-penal-shtanga-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/43/05/30543/images/238842/238842.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/43/05/30543/images/238841/238841.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Оскар-7 Пенал штанга &mdash; однодверный шкаф со штангой и антресольной полкой.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">208.8</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">38.6</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">55</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">55</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Стиль">Современный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">1</param>
</offer>
<offer id="1205203822" group_id="50403">
<name>Престиж Пенал, венге, склад</name>
<vendor>Миф</vendor>
<vendorCode>MF-000012303-1</vendorCode>
<price>13041.18</price>
<shop-sku>MF-000012303-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>56.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>40.000/52.400/215.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-penal-venge-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/03/04/50403/images/76692/76692.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/03/04/50403/images/76693/76693.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Престиж Пенал&nbsp;со Стеклом - идеальное решение для гостиной в классическом стиле.</p> <p>Утонченный Дизайн: Верхний отдел с фасадом из стекла-витража придает этому пеналу уникальный шарм. Это место для вашей коллекции предметов и восхитительных аксессуаров, которые заслуживают особого внимания. Материал фасада из МДФ с декором в шоколадных тонах добавляет нотку роскоши и теплоты в ваш интерьер.</p> <p>Простор и Организация: Внутри верхнего отдела вы найдете три прочные полки из ЛДСП в венге. Они обеспечивают идеальное место для размещения ваших сокровищ и драгоценностей, делая их доступными для вас и ваших гостей.</p> <p>Надежная Конструкция: Нижний отсек с глухим фасадом обеспечивает место для хранения, что оставляется скрытым. Здесь вы найдете еще одну полку для удобной организации. Крепкий корпус из ЛДСП обеспечивает надежную поддержку и долгий срок службы.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">215</param>
<param name="Полки">5</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.4</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">40</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">56</param>
<param name="Назначение шкафа">Для посуды</param>
<param name="Коллекция">Престиж</param>
<param name="Стиль">Классический</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Венге шоколад</param>
</offer>
<offer id="1205203823" group_id="50404">
<name>Престиж Шкаф двухдверный, венге, склад</name>
<vendor>Модули Миф</vendor>
<vendorCode>MF-000012313-1</vendorCode>
<price>17624.62</price>
<shop-sku>MF-000012313-1</shop-sku>
<weight>77.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>800.000/524.000/2150.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-shkaf-dvuhdvernyj-venge-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/04/04/50404/images/76694/76694.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/04/04/50404/images/76695/76695.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Престиж Шкаф &mdash; шкаф для платья в жилую комнату. Материал корпуса ЛДСП, фасады МДФ.&nbsp;</p><p>Внутреннее наполнение:</p><p>•отделение за 2 дверьми со штангой и антресольной полкой,</p><p>•2 выдвижных ящика.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Высота">2150</param>
<param name="Полки">1</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">524</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">800</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">77</param>
<param name="Назначение шкафа">Для одежды</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Венге шоколад</param>
</offer>
<offer id="1205207481" group_id="51464">
<name>Палермо-3_Ю ШК-015 Шкаф 1 - створчатый, ясень шимо светлый / белый, склад</name>
<vendor>Стиль</vendor>
<vendorCode>МС-БО704</vendorCode>
<price>10642.40</price>
<shop-sku>МС-БО704</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>48.00</weight>
<box-count>5</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>53.600/38.100/207.800</dimensions>
<url>https://www.mosdommebel.ru/product/palermo-3_yu-shkaf-1-stvorchatyj-yasen-shimo-svetlyj-belyj-s/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/64/14/51464/images/120974/120974.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф 1-створчатый &mdash; оснащен секцией с полками. Сборка пенала универсальная. Опоры шкафа – регулируемые американки. Высота регулировки до 10 мм.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Полки">4</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">38.1</param>
<param name="Габариты упаковки, см">53.6/38.1/207.8</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">207.8</param>
<param name="Ширина">53.6</param>
<param name="Вес" unit="кг">48</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Белый глянец</param>
<param name="Назначение шкафа">Для белья</param>
<param name="Коллекция">Палермо-3</param>
<param name="Цвет корпуса">Ясень шимо светлый</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">5</param>
<param name="Тип сборки">Универсальный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,099</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Ясень шимо светлый / Белый глянец</param>
</offer>
<offer id="1205207814" group_id="51568">
<name>МИЙА-3 Пенал ПО-302, склад</name>
<vendor>Стиль</vendor>
<vendorCode>1205207814</vendorCode>
<price>6315.48</price>
<shop-sku>1205207814</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>56.00</weight>
<box-count>5</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>45.000/50.900/213.000</dimensions>
<url>https://www.mosdommebel.ru/product/mija-3-penal-po-302-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/68/15/51568/images/78664/78664.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/68/15/51568/images/78665/78665.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>МИЙА-3 Пенал ПО-302 &mdash; однодверный шкаф с открытыми полками и секцией за распашной дверью. Изготовлен из ЛДСП.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">45</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">50.9</param>
<param name="Габариты упаковки, см">45/50.9/213</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">213</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">56</param>
<param name="Назначение шкафа">Для книг</param>
<param name="Коллекция">Мийа-3</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">5</param>
<param name="Тип сборки">Универсальный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,117</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">4</param>
</offer>
<offer id="1205232263" group_id="67578">
<name>Кэт-6 бодега/сандал Шкаф 2-х дверный, склад</name>
<vendor>Диал</vendor>
<vendorCode>1205232263</vendorCode>
<price>18164.16</price>
<shop-sku>1205232263</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>103.34</weight>
<box-count>3</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>94.000/58.000/220.000</dimensions>
<url>https://www.mosdommebel.ru/product/keht-6-bodega-sandal-shkaf-2-h-dvernyj-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/78/75/67578/images/137092/137092.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/78/75/67578/images/137093/137093.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Кэт-6 бодега/сандал Шкаф 2-х дверный &mdash; распашной шкаф для одежды и белья, состоящий из 2 секций: платяной со штангой и антресольной полкой и бельевой с 4 полками. Корпус ЛДСП, фасады МДФ с фрезеровкой.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">220</param>
<param name="Полки">5</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Спальня</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">58</param>
<param name="Габариты упаковки, см">94/58/220</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">94</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">103.34</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Кэт-6</param>
<param name="Стиль">Классический</param>
<param name="Количество упаковок">3</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Бодега белая / Сандал</param>
</offer>
<offer id="1205252956" group_id="83394">
<name>Престиж 2 Шкаф платяной, венге, склад (Венге)</name>
<vendor>Миф</vendor>
<vendorCode>1205252956</vendorCode>
<price>21670.64</price>
<shop-sku>1205252956</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>95.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>44.600/52.800/215.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-2-shkaf-platyanoy-venge-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/94/33/83394/images/185984/185984.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф оборудован штангой, антресольной полкой и 2 выдвижными ящиками.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Высота">215</param>
<param name="Полки">1</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.8</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">44.6</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">95</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Коллекция">Престиж 2</param>
<param name="Стиль">Классический</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Венге</param>
</offer>
<offer id="1205252958" group_id="83395">
<name>Престиж 2 Пенал со стеклом, венге, склад (Венге)</name>
<vendor>Миф</vendor>
<vendorCode>1205252958</vendorCode>
<price>15746.30</price>
<shop-sku>1205252958</shop-sku>
<weight>70.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>45.000/52.800/215.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-2-penal-so-steklom-venge-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/95/33/83395/images/185985/185985.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Престиж 2 Пенал со стеклом &mdash; витрина-колонка. Верхняя часть укомплектована дверцей со стеклом и 3 полками ЛДСП, нижняя &mdash; глухой дверцей и 1 полкой.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">215</param>
<param name="Полки">4</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.8</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">45</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">70</param>
<param name="Назначение шкафа">Для посуды</param>
<param name="Стиль">Классический</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Венге</param>
</offer>
<offer id="1205270845" group_id="96514">
<name>Престиж 2 Шкаф платяной, сандал светлый, склад</name>
<vendor>Миф</vendor>
<vendorCode>1205270845</vendorCode>
<price>21670.64</price>
<shop-sku>1205270845</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066152428</barcode>
<warranty-days>P1Y6M</warranty-days>
<dimensions>44.600/52.000/215.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-2-shkaf-platyanoy-sandal-svetlyy-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/14/65/96514/images/237455/237455.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Престиж 2 Шкаф платяной &mdash; шкаф оборудован штангой, антресольной полкой и 2 выдвижными ящиками.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Высота">215</param>
<param name="Полки">1</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">44.6</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Коллекция">Престиж 2</param>
<param name="Стиль">Прованс</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Сандал светлый</param>
</offer>
<offer id="1205270848" group_id="96517">
<name>Престиж 2 Пенал со стеклом, сандал светлый, склад</name>
<vendor>Миф</vendor>
<vendorCode>1205270848</vendorCode>
<price>15746.30</price>
<shop-sku>1205270848</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066152312</barcode>
<warranty-days>P1Y6M</warranty-days>
<dimensions>45.000/52.800/215.000</dimensions>
<url>https://www.mosdommebel.ru/product/prestizh-2-penal-so-steklom-sandal-svetlyy-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/17/65/96517/images/237461/237461.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/17/65/96517/images/237462/237462.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Престиж 2 Пенал со стеклом &mdash; витрина-колонка. Верхняя часть укомплектована дверцей со стеклом и 3 полками ЛДСП, нижняя &mdash; глухой дверцей и 1 полкой.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Тип дверей">Распашные</param>
<param name="Полки">4</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.8</param>
<param name="Высота">215</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Ширина">45</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Назначение шкафа">Для посуды</param>
<param name="Коллекция">Престиж 2</param>
<param name="Стиль">Классический</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Сандал светлый</param>
</offer>
<offer id="1205367697" group_id="123961">
<name>Элегия Шкаф 3х ств. ШК-153, сонома/белый глянец, склад (Сонома / Белый глянец)</name>
<vendor>Рада</vendor>
<vendorCode>1205367697</vendorCode>
<price>24149.98</price>
<shop-sku>1205367697</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>133.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>206.400/53.000/212.000</dimensions>
<url>https://www.mosdommebel.ru/product/elegiya-shkaf-3kh-stv-shk-153-sonoma-belyy-glyanets-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/61/39/123961/images/260803/260803.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/61/39/123961/images/260802/260802.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Элегия Шкаф 3х ств. ШК-153 &mdash; распашной трехдверный шкаф для одежды и белья. Материал корпуса ЛДСП Дуб Сонома, фасад МДФ Белый глянец.</p> <p>Внутреннее наполнение:</p> <p>•отделение с 2 дверьми со штангой и антресольной полкой,</p> <p>•отделение с 1 дверью 4 полки.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">212</param>
<param name="Полки">5</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Спальня</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">53</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">206.4</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">133</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Элегия</param>
<param name="Стиль">Современный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Сонома / Белый глянец</param>
</offer>
<offer id="1205393411" group_id="142871">
<name>Шкаф-купе Фиеста-2 ЛДСП, ясень шимо светлый/темный, витринный образец (Ясень шимо темный, Ясень шимо светлый)</name>
<vendor>Регион 58</vendor>
<vendorCode>1205393411</vendorCode>
<price>27435.98</price>
<shop-sku>1205393411</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>195.00</weight>
<box-count>5</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>170.000/56.000/222.000</dimensions>
<url>https://www.mosdommebel.ru/product/shkaf-kupe-fiesta-2-ldsp-yasen-shimo-svetlyy-temnyy-vitrinnyy-obrazets/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/71/28/142871/images/289426/289426.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/71/28/142871/images/289427/289427.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф-купе Фиеста &mdash; современная модель с двумя большими зеркальными створками и центральной секцией из ЛДСП (две створки и 3 выдвижных ящика).&nbsp;</p> <p>Наполнение шкафа:</p> <p>•секция со штангой и антресольной полкой,</p> <p>•центральная секция с полкой и 3 выдвижными ящиками,</p> <p>•секция с 2 штангами.</p> <p><br></p> <ul> </ul> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">3</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">3</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">56</param>
<param name="Тип дверей">Смешанный</param>
<param name="Высота">222</param>
<param name="Ширина">170</param>
<param name="Вес" unit="кг">195</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Ясень шимо светлый</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Фиеста</param>
<param name="Цвет корпуса">Ясень шимо темный</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">5</param>
<param name="Тип шкафа">Шкаф-купе</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">ЛДСП/Зеркало</param>
<param name="Полки">2</param>
</offer>
<offer id="1205401612" group_id="144556">
<name>Мийа 3 ШК-004 Шкаф 1 ств. Комбинированный, ФП Город, склад (Ясень шимо светлый, Ясень шимо светлый + ФП Города)</name>
<vendor>Стиль</vendor>
<vendorCode>1205401612</vendorCode>
<price>10742.04</price>
<shop-sku>1205401612</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066198266</barcode>
<weight>54.00</weight>
<box-count>4</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>48.700/50.900/207.800</dimensions>
<url>https://www.mosdommebel.ru/product/miya-3-shk-004-shkaf-1-stv-kombinirovannyy-fp-gorod-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/56/45/144556/images/297082/297082.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Однодверный шкаф-пенал, оборудованный 3 выдвижными ящиками и секцией за распашной дверью со штангой.</p> <p>Фасад с фотопечатью Город.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">3</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">50.9</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">207.8</param>
<param name="Ширина">48.7</param>
<param name="Вес" unit="кг">54</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Ясень шимо светлый + ФП Города</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Мийа 3</param>
<param name="Цвет корпуса">Ясень шимо светлый</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">4</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0.12</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП с фотопечатью</param>
<param name="Полки">0</param>
</offer>
<offer id="1205403860" group_id="145263">
<name>Ким Пенал открытый, венге/белый глянец, склад</name>
<vendor>Миф</vendor>
<vendorCode>1205403860</vendorCode>
<price>8296.62</price>
<shop-sku>1205403860</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066225078</barcode>
<warranty-days>P1Y6M</warranty-days>
<dimensions>50.000/52.400/223.600</dimensions>
<url>https://www.mosdommebel.ru/product/kim-penal-s-yashchikami-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/63/52/145263/images/299738/299738.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/63/52/145263/images/299739/299739.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Ким Пенал с ящиками &mdash; открытый стеллаж с 5 полками и 2 ящиками. Материал корпуса ЛДСП Венге, фасады МДФ Белый глянец.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Ширина">50</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">0</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.4</param>
<param name="Тип дверей">Без дверей</param>
<param name="Высота">223.6</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Белый глянец</param>
<param name="Назначение шкафа">Для книг</param>
<param name="Коллекция">Ким</param>
<param name="Цвет корпуса">Венге</param>
<param name="Стиль">Современный</param>
<param name="Тип шкафа">Стеллаж</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Полки">5</param>
</offer>
<offer id="1205405987" group_id="145608">
<name>Шкаф двухстворчатый с зеркалом Бьянка Белый/Бетон светлый, выставочный образец</name>
<vendor>Case</vendor>
<vendorCode>1205405987</vendorCode>
<price>14302.58</price>
<shop-sku>1205405987</shop-sku>
<weight>76.00</weight>
<box-count>3</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>80.200/47.000/217.600</dimensions>
<url>https://www.mosdommebel.ru/product/shkaf-dvukhstvorchatyy-s-zerkalom-byanka-belyy-beton-svetlyy-vystavochnyy-obrazets/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/08/56/145608/images/302423/302423.2000x1500.jpeg</picture>
<description>
<![CDATA[ <p>Распашной шкаф Бьянка с зеркалом &mdash; это двухстворчатый классический шкаф для одежды в вашу спальню, гостиную или гардеробную. Дверцы шкафа украшены зеркалом и накладками из профиля МДФ разных оттенков.&nbsp;</p> <p>Внутреннее наполнение шкафа: 4 полочки и перекладина, дает возможность создать дополнительную область для хранения бельевых принадлежностей и одежды.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">217.6</param>
<param name="Полки">4</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">47</param>
<param name="Габариты упаковки, см">213х47х21</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">80.2</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">76</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Бьянка</param>
<param name="Стиль">Лофт</param>
<param name="Количество упаковок">3</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">ЛДСП+МДФ+Зеркало</param>
<param name="Цвет">Белый/Бетон светлый</param>
</offer>
<offer id="1205406839" group_id="145946">
<name>Адель Шкаф 1,6 платяной, венге / лоредо, склад (Венге / лоредо)</name>
<vendor>Эра</vendor>
<vendorCode>1205406839</vendorCode>
<price>19133.00</price>
<shop-sku>1205406839</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>117.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>160.000/47.000/210.000</dimensions>
<url>https://www.mosdommebel.ru/product/adel-shkaf-1-6-platyanoj-venge-loredo-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/46/59/145946/images/303503/303503.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/46/59/145946/images/303502/303502.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф Адель &mdash; станет настоящим украшением прихожей. &nbsp;В нем можно разместить все необходимые вещи и поддерживать в квартире&nbsp; порядок.&nbsp;&nbsp;</p> <p>Внутреннее наполнение шкафа:</p> <p>два отделения со штангами и антресольными полками и встроенными выдвижными ящиками.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Ширина">160</param>
<param name="Полки">2</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">2</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">47</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">210</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">117</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Современный</param>
<param name="Тип сборки">Не универсальная сборка</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,21</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Венге / лоредо</param>
</offer>
<offer id="1205407566" group_id="146222">
<name>Маркиза Пенал ПН-03, склад</name>
<vendor>Семья Мебелони</vendor>
<vendorCode>мебелони-49300-1</vendorCode>
<price>9589.82</price>
<shop-sku>мебелони-49300-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>52.02</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>40.200/46.000/217.600</dimensions>
<url>https://www.mosdommebel.ru/product/markiza-penal-pn-03-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/22/62/146222/images/303823/303823.2000x1500.png</picture>
<description>
<![CDATA[ <p>Модульная серия Маркиза в стиле Прованс для создания уюта и домашнего тепла в Вашем доме. Коллекция выпускается в спальне, гостиной, прихожей и детской.<br> <br> Лаконичная без обильного декора и массивных элементов мебель прекрасно дополняется цветочными композициями и семейными фотоснимками, подчеркивая индивидуальность обладателя интерьера.<br> <br> Нежные, как будто немного выгоревшие на солнце оттенки коллекции Маркиза оказывают успокаивающий эффект и вызывают положительные эмоции.<br> <br> <strong><em>Особенности серии:</em></strong><br> <br> - Бархатистая поверхность фасадов с древесными тиснением, выполненных из МДФ, тактильно приятная на ощупь.<br> <br> - Оригинальная фрезеровка фасадов<br> <br> - Прочные 4-х шарнирные петли для надежной фиксации элементов мебели<br> <br> - Вместительные модули шкафов можно укомплектовать дополнительным набором полок<br> <br>- Прикроватные тумбы, пеналы и угловой шкаф собираются на обе стороны - универсальны.</p> <p>Маркиза Пенал ПН-03 &mdash; однодверный шкаф-витрина с 4 полками ЛДСП и выдвижным ящиком. Распашная дверь с витражом из обычного стекла.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">1</param>
<param name="Тип дверей">Распашные</param>
<param name="Полки">4</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">0</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">46</param>
<param name="Габариты упаковки, см">402/2176/460</param>
<param name="Высота">217.6</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Ширина">40.2</param>
<param name="Вес" unit="кг">52.02</param>
<param name="Назначение шкафа">Для посуды</param>
<param name="Коллекция">Маркиза</param>
<param name="Стиль">Классический</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ + стекло</param>
<param name="Цвет">Дуб Сонома</param>
</offer>
<offer id="1205412521" group_id="150559">
<name>Эго Пенал П-1 НГ, Бетон Светлый/Белый Глянец, склад (Глянец Белый, Бетон Светлый)</name>
<vendor>Диал</vendor>
<vendorCode>1205233012-150559</vendorCode>
<price>12497.40</price>
<shop-sku>1205233012-150559</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>54.94</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>51.000/41.800/201.900</dimensions>
<url>https://www.mosdommebel.ru/product/ego-penal-p-1-ng-beton-svetlyy-belyy-glyanets-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/59/05/150559/images/305833/305833.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Благодаря своим небольшим габаритам пенал идеально впишется как в спальню, так и в гостиную, коридор. При этом он очень функциональный, вместительный, оснащён четырьмя просторными полками и выдвижным ящиком, где можно разместить одежду, бельё и другие предметы обихода.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">1</param>
<param name="Кол-во месяцев гарантии">24</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Штанга">0</param>
<param name="Количество на складе">1</param>
<param name="Глубина">41.8</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">201.9</param>
<param name="Ширина">51</param>
<param name="Вес" unit="кг">54.94</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Глянец Белый</param>
<param name="Назначение шкафа">Для белья</param>
<param name="Коллекция">Эго</param>
<param name="Цвет корпуса">Бетон Светлый</param>
<param name="Стиль">Современный</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">4</param>
</offer>
<offer id="1205413793" group_id="151000">
<name>Юниор-7 МДФ ДЮ-08 Шкаф комбинированный, сиреневый металл, склад (Ясень шимо светлый, Сиреневый металлик)</name>
<vendor>Регион 58</vendor>
<vendorCode>1205413793</vendorCode>
<price>16245.56</price>
<shop-sku>1205413793</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066224293</barcode>
<weight>72.00</weight>
<box-count>5</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>44.600/40.000/220.000</dimensions>
<url>https://www.mosdommebel.ru/product/yunior-7-mdf-dyu-08-shkaf-kombinirovannyy-sirenevyy-metall-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/00/10/151000/images/307921/307921.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/00/10/151000/images/307920/307920.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Юниор-7 МДФ ДЮ-08 Шкаф комбинированный &mdash; двухдверный шкаф с 2 выдвижными ящиками. Материал корпуса ЛДСП, фасад МДФ.</p> <p>Наполнение шкафа:&nbsp;</p> <p>отделение для платья с выдвижной вешалкой,</p> <p>отделение для белья 3 полки,</p> <p>общая антресольная полка, 2 выдвижных ящика.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">2</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">Выдвижная</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">40</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">220</param>
<param name="Ширина">44.6</param>
<param name="Вес" unit="кг">72</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Сиреневый металлик</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Юниор-7 МДФ</param>
<param name="Цвет корпуса">Ясень шимо светлый</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">5</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Полки">4</param>
</offer>
<offer id="1205422467" group_id="153245">
<name>Румер СШК 1.210.70-11.11.11 Шкаф-купе 3-х дверный (2100x600x2200), ясень шимо (Ясень шимо, Ясень шимо/Ясень шимо/Ясень шимо)</name>
<vendor>Трия</vendor>
<vendorCode>triya-123757-1</vendorCode>
<price>69958.94</price>
<shop-sku>triya-123757-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110065974724</barcode>
<warranty-days>P1Y6M</warranty-days>
<dimensions>210.000/60.000/220.000</dimensions>
<url>https://www.mosdommebel.ru/product/rumer-sshk-1-210-70-11-11-11-shkaf-kupe-3-kh-dvernyy-2100x600x2200-yasen-shimo/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/45/32/153245/images/317630/317630.2000x1500.jpeg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/45/32/153245/images/317631/317631.2000x1500.jpeg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/45/32/153245/images/317632/317632.2000x1500.jpeg</picture>
<description>
<![CDATA[ <p style="text-align: justify;">Шкаф-купе Румер &mdash; вместительный шкаф для прихожей или спальни. Каркас шкафа изготовлен из ЛДСП. Цветовая гамма: Ясень шимо. Фасады изготавливаются в профиле из алюминия. Шкаф оборудован надежной системой раздвижения Версаль, рассчитанной на 70 тыс. циклов. Двери скользят плавно и легко благодаря прорезиненным роликам. Шлегель с высотой ворса 6 мм смягчит удар двери о каркас и защитит содержимое шкафа от пыли. Внутреннее наполнение шкафа продумано и практично: секция с 5 полками и отделение со штангой и полками для обуви и головных уборов. Дополнительно возможно доукомплектовать шкаф модулем с 2-мя ящиками и внешним угловым стеллажом.</p> <p>Шкаф-купе Румер как на фото укомплектован:</p> <ul> <li>каркас ШК 1.210 (2100х600х2200);</li> <li>дверь шкафа-купе ШК 1.70.11 (696х34х2052) &mdash; 3 шт.</li> </ul> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Кол-во месяцев гарантии">24</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Спальня</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">60</param>
<param name="Тип дверей">Двери-купе</param>
<param name="Высота">220</param>
<param name="Ширина">210</param>
<param name="Цвет фасада">ясень светлый</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Румер</param>
<param name="Цвет корпуса">Ясень шимо</param>
<param name="Поставка изделия">В разобранном виде</param>
<param name="Стиль">Современный</param>
<param name="Тип сборки">Универсальный</param>
<param name="Тип шкафа">Шкаф-купе</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">7</param>
</offer>
<offer id="1205422473" group_id="153247">
<name>Детский шкаф Бемби-3 МДФ, белый глянец (Ясень шимо светлый, Белый глянец)</name>
<vendor>Регион 58</vendor>
<vendorCode>1205422473</vendorCode>
<price>17971.24</price>
<shop-sku>1205422473</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>83.00</weight>
<box-count>4</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>80.000/49.600/200.000</dimensions>
<url>https://www.mosdommebel.ru/product/detskij-shkaf-bembi-3-mdf-belyj-glyanec/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/47/32/153247/images/317650/317650.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/47/32/153247/images/317652/317652.2000x1500.png</picture>
<description>
<![CDATA[ <p>Детский шкаф Бемби-3 МДФ &mdash; одновременно практичный и вместительный. Корпус выполнен из ЛДСП, фасад &mdash; МДФ.</p> <p>Наполнение шкафа:</p> <p>•отделение с 4 полками для белья,</p> <p>•отделение со штангой и антресольной полкой.</p> <p>•выдвижной ящик.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">1</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">1</param>
<param name="Тип">Детская мебель</param>
<param name="Количество на складе">1</param>
<param name="Глубина">49.6</param>
<param name="Габариты упаковки, см">80х49,6х200</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">200</param>
<param name="Ширина">80</param>
<param name="Вес" unit="кг">83</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Белый глянец</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Бемби</param>
<param name="Цвет корпуса">Ясень шимо светлый</param>
<param name="Поставка изделия">В разобранном виде</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">4</param>
<param name="Тип сборки">Не универсальная сборка</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">МДФ</param>
<param name="Полки">5</param>
</offer>
<offer id="1205432250" group_id="159869">
<name>Лайт Шкаф ШК-001, белый (Белый)</name>
<vendor>Стиль</vendor>
<vendorCode>МС-ЧЮ202-1</vendorCode>
<price>6160.72</price>
<shop-sku>МС-ЧЮ202-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>56.00</weight>
<box-count>2</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>81.000/52.600/175.600</dimensions>
<url>https://www.mosdommebel.ru/product/layt-shkaf-shk-001-belyy/</url>
<count>2</count>
<outlets>
<outlet instock="2"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/69/98/159869/images/340404/340404.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/69/98/159869/images/340405/340405.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Лайт Шкаф ШК-001&nbsp;&mdash;&nbsp;отличное решение для прихожей или спальни, оформленной в современном стиле.&nbsp;</p> <p>Преимущества двухстворчатого шкафа «Лайт»:</p> <p>• Функциональное наполнение<br>• Надежная металлическая штанга<br>• Вместительная секция для хранения верхней одежды<br>• Просторная полка под обувь<br>• Шкаф идеально смотрится в сочетании с другими интерьерными решениями линейки «Лайт»<br>• Несколько шкафов линейки «Лайт» можно объединить в полноценную систему хранения</p> <p>Материал ЛДСП.</p> <p></p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">81</param>
<param name="Полки">1</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">2</param>
<param name="Глубина">52.6</param>
<param name="Габариты упаковки, см">175х53,5х14,5</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">175.6</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">56</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Коллекция">Лайт</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Минимализм</param>
<param name="Количество упаковок">2</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,11</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Белый</param>
</offer>
<offer id="1205434494" group_id="161436">
<name>Агата Шкаф для одежды Исп.2, белый (Белый)</name>
<vendor>Трия</vendor>
<vendorCode>triya-229048-1</vendorCode>
<price>11234.94</price>
<shop-sku>triya-229048-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<warranty-days>P1Y6M</warranty-days>
<dimensions>90.200/52.700/230.500</dimensions>
<url>https://www.mosdommebel.ru/product/agata-shkaf-dlya-odezhdy-isp-2-belyy/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/36/14/161436/images/345945/345945.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/36/14/161436/images/345946/345946.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/36/14/161436/images/345947/345947.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Агата Шкаф для одежды Исп.2 &mdash; двухдверный распашной шкаф для платья. Материал шкафа ЛДСП.</p> <p>Внутреннее наполнение: штанга и антресольная полка.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">230.5</param>
<param name="Полки">1</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">52.7</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">90.2</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Коллекция">Агата</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Минимализм</param>
<param name="Стиль">Современный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Белый</param>
</offer>
<offer id="1205435853" group_id="162466">
<name>Белла Шкаф 2-х створчатый, ясень, склад</name>
<vendor>Миф</vendor>
<vendorCode>1205435853</vendorCode>
<price>10936.02</price>
<shop-sku>1205435853</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>80.00</weight>
<warranty-days>P1Y6M</warranty-days>
<dimensions>80.000/47.000/212.000</dimensions>
<url>https://www.mosdommebel.ru/product/bella-shkaf-2-h-stvorchatyj-yasen-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/66/24/162466/images/347652/347652.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/66/24/162466/images/347653/347653.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф Белла &mdash; двухдверный шкаф с 3 выдвижными ящиками, штангой и полкой для головных уборов.</p> <p>Материал ЛДСП.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">3</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Гостиная</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">47</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">212</param>
<param name="Ширина">80</param>
<param name="Вес" unit="кг">80</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Цвет фасада">Ясень шимо светлый</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Белла</param>
<param name="Цвет корпуса">Ясень шимо темный</param>
<param name="Поставка изделия">В разобранном виде</param>
<param name="Стиль">Современный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">1</param>
</offer>
<offer id="1205438467" group_id="163210">
<name>Шкаф Ямайка ЯПШ-1, белый, склад</name>
<vendor>ТЭКС</vendor>
<vendorCode>тэкс-00-00028741-1</vendorCode>
<price>4842.08</price>
<shop-sku>тэкс-00-00028741-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>43.90</weight>
<box-count>2</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>60.000/35.000/210.000</dimensions>
<url>https://www.mosdommebel.ru/product/shkaf-yamayka-yapsh-1-belyy-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/10/32/163210/images/364776/364776.2000x1500.jpg</picture>
<description>
<![CDATA[ <p style="text-align: justify;"> Если площадь Вашей прихожей позволяет Вам расположить двустворчатый шкаф, обратите внимание на модель из коллекции Ямайка. Модуль оснащен евроштангой и двумя полками и идеален для хранения верхней одежды, обуви и коробок с аксессуарами. Несмотря на отличную вместимость, шкаф достаточно компактен и имеет ширину всего 60 см. </p> <h2 style="text-align: justify;">Особенности</h2> <p style="text-align: justify;"> </p> <div> <ul> <li>универсальный дизайн</li> <li>разноплановое наполнение</li> <li>возможность установки в малогабаритном помещении</li> </ul> </div> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Высота">210</param>
<param name="Полки">2</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">Выдвижная</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">35</param>
<param name="Тип дверей">Распашные</param>
<param name="Ширина">60</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Вес" unit="кг">43.9</param>
<param name="Назначение шкафа">Для прихожей</param>
<param name="Коллекция">Ямайка</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">2</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Белый</param>
</offer>
<offer id="1205451885" group_id="172488">
<name>Лотос 5.011 Шкаф многоцелевой, склад</name>
<vendor>Боровичи-мебель</vendor>
<vendorCode>23982A-1</vendorCode>
<price>8779.98</price>
<shop-sku>23982A-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>39.43</weight>
<box-count>1</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>50.000/38.000/199.500</dimensions>
<url>https://www.mosdommebel.ru/product/lotos-5-011-shkaf-mnogotselevoy-sklad/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/88/24/172488/images/389865/389865.2000x1500.png</picture>
<description>
<![CDATA[ <p>Лотос 5.011 Шкаф многоцелевой &mdash; однодверный шкаф для одежды, оборудованный антресольной полкой и полкой для обуви и выдвижной штангой. Материал ЛДСП в декоре Ясень шимо светлый.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">50</param>
<param name="Полки">2</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">Выдвижная</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">38</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">199.5</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">39.43</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Коллекция">Лотос</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">1</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,11</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Ясень шимо светлый</param>
</offer>
<offer id="1205452478" group_id="172579">
<name>RICH Шкаф ШК-004 Дуб Крафт золотой / Миндаль / Глиняный серый (Дуб Крафт Золотой, Миндаль / Глиняный серый)</name>
<vendor>Стиль</vendor>
<vendorCode>МС-ЧЭ470-172579</vendorCode>
<price>9143.56</price>
<shop-sku>МС-ЧЭ470-172579</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>57.00</weight>
<box-count>2</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>101.600/46.200/130.600</dimensions>
<url>https://www.mosdommebel.ru/product/rich-shkaf-shk-004-dub-kraft-zolotoj-mindal-glinyanyj-seryj/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/79/25/172579/images/390669/390669.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/79/25/172579/images/390670/390670.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/79/25/172579/images/390671/390671.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>RICH Шкаф ШК-004 &mdash; невысокий двухдверный шкаф из детской серии&nbsp;RICH. Два необычных цветовых решения для фасада гарнитура – «Мята + Сумеречный голубой» и «Миндаль + Глиняный серый».&nbsp;Оригинальные фасады с фрезерованными выемками, которые заменяют ручки.&nbsp;</p> <p>Шкаф оборудован 1 штангой и 3 полками.</p> <p>Изделия линейки Rich оснащены подпятниками для того, чтобы снизить давление на напольное покрытие и не травмировать его при передвижении элементов гарнитура.</p> <p>Материал корпуса и фасада ЛДСП.</p> <p></p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Вес" unit="кг">57</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Детская</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">46.2</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">130.6</param>
<param name="Ширина">101.6</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Цвет фасада">Миндаль / Глиняный серый</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">RICH</param>
<param name="Цвет корпуса">Дуб Крафт Золотой</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">2</param>
<param name="Тип сборки">Универсальный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,114</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Полки">3</param>
</offer>
<offer id="1205455282" group_id="173670">
<name>Норд Шкаф трехстворчатый 1200 крафт белый (Дуб Крафт белый)</name>
<vendor>Миф</vendor>
<vendorCode>MF-000095893-1</vendorCode>
<price>16678.04</price>
<shop-sku>MF-000095893-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>106.00</weight>
<box-count>4</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>350.000/51.000/223.600</dimensions>
<url>https://www.mosdommebel.ru/product/nord-shkaf-trekhstvorchatyj-1200-kraft-belyj/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/70/36/173670/images/394569/394569.2000x1500.png</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/70/36/173670/images/394572/394572.2000x1500.png</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/70/36/173670/images/394568/394568.2000x1500.png</picture>
<description>
<![CDATA[ <p>Норд Шкаф трехдверный &mdash; модель для одежды и белья.</p> <p>Внутреннее наполнение:</p> <p>•за 2 распашными дверьми:&nbsp;полка антресольная + штанга + полка для обуви;</p> <p>•за 1 распашной дверью: 5 полок ЛДСП.</p> <p>Материал корпуса/фасада ЛДСП, ручки профильные металлические.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">350</param>
<param name="Полки">7</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Прихожая</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">51</param>
<param name="Габариты упаковки, см">125/52/230</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">223.6</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">106</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Норд</param>
<param name="Поставка изделия">В разобранном виде</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">4</param>
<param name="Тип сборки">Универсальный</param>
<param name="Тип шкафа">Распашной</param>
<param name="Объем">0,4</param>
<param name="Наличие зеркала">Нет</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Дуб Крафт белый</param>
</offer>
<offer id="1205457909" group_id="175153">
<name>Кэт-7 арт. 015 Шкаф-Купе Венге Linum/Дуб Белфорт (Венге / Белфорт)</name>
<vendor>Диал</vendor>
<vendorCode>66761-1</vendorCode>
<price>17459.26</price>
<shop-sku>66761-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<barcode>110066195203</barcode>
<weight>119.70</weight>
<box-count>4</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>136.000/56.000/201.600</dimensions>
<url>https://www.mosdommebel.ru/product/shkaf-kupe_vj-1/</url>
<count>2</count>
<outlets>
<outlet instock="2"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/53/51/175153/images/395045/395045.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/53/51/175153/images/395046/395046.2000x1500.jpg</picture>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">136</param>
<param name="Полки">6</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Спальня</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">2</param>
<param name="Глубина">56</param>
<param name="Тип дверей">Двери-купе</param>
<param name="Высота">201.6</param>
<param name="Кол-во месяцев гарантии">24</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">119.7</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Кэт-7</param>
<param name="Поставка изделия">В разобранном виде</param>
<param name="Стиль">Современный</param>
<param name="Количество упаковок">4</param>
<param name="Тип шкафа">Шкаф-купе</param>
<param name="Объем">0,155</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">ЛДСП</param>
<param name="Цвет">Венге / Белфорт</param>
</offer>
<offer id="1205459679" group_id="176009">
<name>Валенсия Шкаф 3-х створчатый белый матовый / орех (Белый матовый / Орех)</name>
<vendor>Миф</vendor>
<vendorCode>MF-000081023-1</vendorCode>
<price>25032.96</price>
<shop-sku>MF-000081023-1</shop-sku>
<country_of_origin>Россия</country_of_origin>
<weight>138.70</weight>
<box-count>6</box-count>
<warranty-days>P1Y6M</warranty-days>
<dimensions>157.500/57.700/227.000</dimensions>
<url>https://www.mosdommebel.ru/product/valensiya-shkaf-3-h-stvorchatyj-belyj-matovyj-orekh/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/09/60/176009/images/395211/395211.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/09/60/176009/images/395212/395212.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Валенсия Шкаф 3-х створчатый &mdash; вместительный шкаф для одежды и белья для спальни. Шкаф, как и вся серия, выполнен в скандинавском стиле прованс. Материал корпуса ЛДСП, фасадов МДФ.</p> <p>Внутреннее наполнение шкафа:</p> <p>•секция для платья за 2 дверьми (одна с зекральными полотнами), штанга, 2 полки,</p> <p>•секция для белья за 1 дверью, 5 полок.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Ширина">157.5</param>
<param name="Полки">7</param>
<param name="Материал корпуса">ЛДСП</param>
<param name="Зона использования">Спальня</param>
<param name="Штанга">1</param>
<param name="Тип">Шкафы</param>
<param name="Количество на складе">1</param>
<param name="Глубина">57.7</param>
<param name="Тип дверей">Распашные</param>
<param name="Высота">227</param>
<param name="Кол-во месяцев гарантии">18</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Вес" unit="кг">138.7</param>
<param name="Назначение шкафа">Для одежды и белья</param>
<param name="Коллекция">Валенсия</param>
<param name="Поставка изделия">В разобранном</param>
<param name="Стиль">Прованс</param>
<param name="Количество упаковок">6</param>
<param name="Тип шкафа">Распашной</param>
<param name="Наличие зеркала">Есть</param>
<param name="Материал фасада">МДФ</param>
<param name="Цвет">Белый матовый / Орех</param>
</offer>
<offer id="1205461855" group_id="176774">
<name>Шкаф 2-х дверный (гл.410) Афина АФ-42 белое дерево</name>
<vendorCode>СМ-42740-1</vendorCode>
<price>16931.38</price>
<shop-sku>СМ-42740-1</shop-sku>
<warranty-days>P1Y6M</warranty-days>
<url>https://www.mosdommebel.ru/product/shkaf-2-kh-dvernyy-gl-410-afina-af-42-beloe-derevo_1/</url>
<count>1</count>
<outlets>
<outlet instock="1"/>
</outlets>
<currencyId>RUB</currencyId>
<categoryId>2005</categoryId>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/74/67/176774/images/395778/395778.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/74/67/176774/images/395777/395777.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/74/67/176774/images/395776/395776.2000x1500.jpg</picture>
<picture>https://www.mosdommebel.ru/wa-data/public/shop/products/74/67/176774/images/395779/395779.2000x1500.jpg</picture>
<description>
<![CDATA[ <p>Шкаф 2-х дверный (гл.410) Афина АФ-42 белое дерево - вместительная система хранения для спальни или прихожей.</p> <p>Модель оснащается 2-я глухими распашными дверцами.<br> Шкаф комплектуется 5 полками и выдвижной штангой. По желанию устанавливается штанга или полки (нижняя и верхняя не съемные!). Комплектация шкафа: каркас, 2 двери, петли с доводчиком.</p> ]]>
</description>
<manufacturer_warranty>true</manufacturer_warranty>
<param name="Количество ящиков">0</param>
<param name="Геометрия шкафа">Прямой</param>
<param name="Материал фасада">МДФ</param>
<param name="Наличие зеркала">Нет</param>
<param name="Назначение шкафа">Платяной</param>
<param name="Тип дверей">Распашные</param>
<param name="Количество на складе">1</param>
<param name="Штанга">1</param>
<param name="Полки">5</param>
<param name="Цвет">Белое дерево</param>
</offer>
</offers>
</shop>
</yml_catalog>
"""

json_output = xml_to_list_of_dicts(xml_string)
print(json_output)
