import filesys
import python
import db

sources_dir = filesys.Dir('/home/povilas/projects/scrapy/scrapy')
project_stats = {}
for f in sources_dir.py_files():
    project_stats[f] = python.analyze_file(sources_dir.full_path(f))

city_db = db.City('172.17.0.2', 'root', 'root', 'jscity')
city_db.connect()
city_id = city_db.create_city('Scrapy')

for fname in project_stats:
    district_id = city_db.create_district(fname, city_id)

    file_stats = project_stats[fname]
    for cl in file_stats['classes']:
        class_stats = file_stats['classes'][cl]
        city_db.create_building(cl, class_stats['code_length'],
                                class_stats['methods'], district_id)

    for fn in file_stats['functions']:
        function_stats = file_stats['functions'][fn]
        city_db.create_building(fn, function_stats['code_length'],
                                1, district_id)
