# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:33:13 2021

@author: a0981
"""

#SELECT, WHERE, DISTINCT, LIMIT

#select * from airports
airports

#select * from airports limit 3
airports.head(3)

#select id from airports where ident = 'KLAX'
airports[airports.ident == 'KLAX'].id

#select distinct type from airport
airports.type.unique()



#SELECT with multiple conditions

#select * from airports where iso_region = 'US-CA' and type = 'seaplane_base'
airports[(airports.iso_region == 'US-CA') & (airports.type == 'seaplane_base')]

#select ident, name, municipality from airports where iso_region = 'US-CA' and type = 'large_airport'
airports[(airports.iso_region == 'US-CA') & (airports.type == 'large_airport')][['ident', 'name', 'municipality']]



#ORDER BY

#select * from airport_freq where airport_ident = 'KLAX' order by type
airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type')

#select * from airport_freq where airport_ident = 'KLAX' order by type desc
airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type', ascending=False)



#IN… NOT IN
#select * from airports where type in ('heliport', 'balloonport')
airports[airports.type.isin(['heliport', 'balloonport'])]

#select * from airports where type not in ('heliport', 'balloonport')
airports[~airports.type.isin(['heliport', 'balloonport'])]



#GROUP BY, COUNT, ORDER BY
#select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, type
airports.groupby(['iso_country', 'type']).size()

#select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, count(*) desc
airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])

#select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, type
airports.groupby(['iso_country', 'type']).size()

#select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, count(*) desc
airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])



#HAVING

#select type, count(*) from airports where iso_country = 'US' group by type having count(*) > 1000 order by count(*) desc
airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)



#Top N records

#select iso_country from by_country order by size desc limit 10
by_country.nlargest(10, columns='airport_count')

#select iso_country from by_country order by size desc limit 10 offset 10
by_country.nlargest(20, columns='airport_count').tail(10)



#Aggregate functions (MIN, MAX, MEAN)

#select max(length_ft), min(length_ft), avg(length_ft), median(length_ft) from runways
runways.agg({'length_ft': ['min', 'max', 'mean', 'median']})



#JOIN

#select airport_ident, type, description, frequency_mhz from airport_freq join airports on airport_freq.airport_ref = airports.id where airports.ident = 'KLAX'
airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], left_on='airport_ref', right_on='id', how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]



#UNION ALL and UNION
#select name, municipality from airports where ident = 'KLAX' union all select name, municipality from airports where ident = 'KLGB'
pd.concat([airports[airports.ident == 'KLAX'][['name', 'municipality']], airports[airports.ident == 'KLGB'][['name', 'municipality']]])



#INSERT

#create table heroes (id integer, name text);
df1 = pd.DataFrame({'id': [1, 2], 'name': ['Harry Potter', 'Ron Weasley']})

#insert into heroes values (1, 'Harry Potter');
df2 = pd.DataFrame({'id': [3], 'name': ['Hermione Granger']})













































