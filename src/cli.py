import argparse


def options():
    """Gets CLI options.

    Returns:
        Namespace: parse CLI options.
    """
    parser = argparse.ArgumentParser(
        description='Generate code city model for python codebase.')

    parser.add_argument('project_dir', type=str,
       help='Full path to python project source code directory.')

    parser.add_argument('--project-name', type=str, required=True,
       help='Project name to be displayed in jscity.')

    return parser.parse_args()
