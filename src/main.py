import filesys
import python
import db
import code_city


def collect_project_stats(sources_dir):
    """Recursively collects python project stats.

    Args:
        sources_dir (filesys.Dir)

    Returns:
        dict: project functions and classes stats.
    """
    project_stats = {
        'dirs': {},
        'files': {},
    }

    sources = sources_dir.py_files()
    for f in sources['files']:
        project_stats['files'][f] = code_city.analyze_file(sources_dir.full_path(f))

    for d in sources['dirs']:
        subdir_stats = collect_project_stats(
            filesys.Dir(sources_dir.full_path(d))
        )
        project_stats['dirs'][d] = subdir_stats

    return project_stats


def generate_code_city_district(project_stats, city_db, city_id,
                                parent_district_id=None):
    """Inserts python city model to MySQL.

    Args:
        project_stats (dict): data returned by collect_project_stats().
        city_db: MySQL city database object.
        city_id (int): MySQL id.
        parent_district_id (int): parent district id for subdirectory stats.
    """
    for fname in project_stats['files']:
        district_id = city_db.create_district(fname, city_id, parent_district_id)

        file_stats = project_stats['files'][fname]
        for cl in file_stats['classes']:
            class_stats = file_stats['classes'][cl]
            city_db.create_building(cl, class_stats['code_length'],
                                    class_stats['methods'], district_id)

        for fn in file_stats['functions']:
            function_stats = file_stats['functions'][fn]
            city_db.create_building(fn, function_stats['code_length'],
                function_stats['arguments'], district_id, '0x4CAE4C')

    for dir_name in project_stats['dirs']:
        district_id = city_db.create_district(dir_name, city_id,
                                              parent_district_id, '0xF0AD4E')
        generate_code_city_district(project_stats['dirs'][dir_name], city_db,
                                    city_id, district_id)

sources_dir = filesys.Dir('/home/povilas/projects/scrapy/scrapy')
project_stats = collect_project_stats(sources_dir)

city_db = db.City('172.17.0.2', 'root', 'root', 'jscity')
city_db.connect()
city_id = city_db.create_city('Scrapy')
generate_code_city_district(project_stats, city_db, city_id)
