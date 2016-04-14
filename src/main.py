import filesys
import db
import code_city
import config


project_name = 'Scrapy'
project_dir = '/home/povilas/projects/scrapy/scrapy'


city_db = db.City(config.MYSQL['host'], config.MYSQL['username'],
    config.MYSQL['password'], config.MYSQL['database'])
city_db.connect()
city_id = city_db.create_city(project_name)

def calc_stats(fs_node, parent_district_id=None):
    """Collect project stats.

    This function is called for every file and directory within the project
    source tree.
    Stats are stored to MySQL according to jscity structure.

    Args:
        fs_node (filesys.Node): currently traversed file/dir.
        parent_district_id (int): parent district (parent directory) MySQL ID.
    """
    if isinstance(fs_node, filesys.Directory):
        return city_db.create_district(
            fs_node.name, city_id, parent_district_id, '0xF0AD4E')
    else:
        district_id = city_db.create_district(
            fs_node.name, city_id, parent_district_id)

        code_stats = code_city.analyze_file(fs_node.full_path)
        for cl in code_stats['classes']:
            class_stats = code_stats['classes'][cl]
            city_db.create_building(cl, class_stats['code_length'],
                                    class_stats['methods'], district_id)

        for fn in code_stats['functions']:
            function_stats = code_stats['functions'][fn]
            city_db.create_building(fn, function_stats['code_length'],
                function_stats['arguments'], district_id, '0x4CAE4C')

filesys.walk(project_dir, calc_stats)
