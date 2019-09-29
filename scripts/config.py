#!/usr/bin/env python3
# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society_docker
"""Configures folders to create, files to copy and repos to clone."""

import os
import subprocess


def get_root_dir():
    """Returns the root dir of the repository."""
    try:
        return subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.STDOUT
        ).rstrip().decode('utf-8')
    except subprocess.CalledProcessError:
        directory = os.path.dirname(os.path.realpath(__file__))
        return os.path.realpath(os.path.join(directory, ".."))


# TODO: import from env files
project = "collecting_society"
environment = "development"
tryton_version = "3.4"

# branch
branch = "master"
if environment in ["development", "testing"]:
    branch = "develop"

# directories
dirs = {}
dirs['root'] = get_root_dir()
dirs['container'] = dirs['root'] + "/container"
dirs['environment'] = dirs['root'] + "/environment"
dirs['scripts'] = dirs['root'] + "/scripts"
dirs['shared'] = dirs['root'] + "/shared"
dirs['ref'] = dirs['shared'] + "/ref"
dirs['src'] = dirs['shared'] + "/src"

# folders to create
create_folders = [
    dirs['root'] + '/postgresql-data',
    dirs['shared'] + '/var/lib/trytond'
]

# files to copy
# (
#    source,
#    destination
# )
copy_files = [
    (
        dirs['shared'] + '/etc/trytonpassfile.example',
        dirs['shared'] + '/etc/trytonpassfile',
    ),
    (
        dirs['environment'] + '/shared.example',
        dirs['environment'] + '/shared'
    ),
    (
        dirs['environment'] + '/webgui.example',
        dirs['environment'] + '/webgui'
    ),
    (
        dirs['environment'] + '/webapi.example',
        dirs['environment'] + '/webapi'
    ),
    (
        dirs['environment'] + '/worker.example',
        dirs['environment'] + '/worker'
    ),
    (
        dirs['src'] + '/collecting_society_worker/config.ini.EXAMPLE',
        dirs['src'] + '/collecting_society_worker/config.ini'
    ),
]

# source repositories to clone
# (
#     git repository url,
#     git clone option,
#     folder name
# ),
clone_sources = [
    # included repositories: tryton upstream
    (
        'https://github.com/tryton/trytond.git',
        '--branch=' + tryton_version,
        'trytond'
    ),
    (
        'https://github.com/tryton/country.git',
        '--branch=' + tryton_version,
        'country'
    ),
    (
        'https://github.com/tryton/currency.git',
        '--branch=' + tryton_version,
        'currency'
    ),
    (
        'https://github.com/tryton/party.git',
        '--branch=' + tryton_version,
        'party'
    ),
    (
        'https://github.com/tryton/company.git',
        '--branch=' + tryton_version,
        'company'
    ),
    (
        'https://github.com/tryton/product.git',
        '--branch=' + tryton_version,
        'product'
    ),
    (
        'https://github.com/tryton/account.git',
        '--branch=' + tryton_version,
        'account'
    ),
    (
        'https://github.com/tryton/account_product.git',
        '--branch=' + tryton_version,
        'account_product'
    ),
    (
        'https://github.com/tryton/account_invoice.git',
        '--branch=' + tryton_version,
        'account_invoice'
    ),
    (
        'https://github.com/tryton/account_invoice_line_standalone.git',
        '--branch=' + tryton_version,
        'account_invoice_line_standalone'
    ),
    (
        'https://github.com/tryton/bank.git',
        '--branch=' + tryton_version,
        'bank'
    ),
    (
        'https://github.com/virtualthings/web_user.git',
        '--branch=' + tryton_version,
        'web_user'
    ),
    # included repositories: tryton custom
    (
        'https://github.com/C3S/archiving.git',
        '--branch=' + branch,
        'archiving'
    ),
    (
        'https://github.com/C3S/portal.git',
        '--branch=' + branch,
        'portal'
    ),
    (
        'https://github.com/C3S/collecting_society.git',
        '--branch=' + branch,
        'collecting_society'
    ),
    # included repositories: pyramid
    (
        'https://github.com/C3S/portal_web.git',
        '--branch=' + branch,
        'portal_web'
    ),
    (
        'https://github.com/C3S/collecting_society_web.git',
        '--branch=' + branch,
        'collecting_society_web'
    ),
    # included repositories: worker
    (
        'https://github.com/C3S/collecting_society_worker.git',
        '--branch=master',
        'collecting_society_worker'
    ),
    (
        'https://github.com/spotify/echoprint-codegen.git',
        '--branch=master',
        'echoprint-codegen'
    ),
]

# reference repositories to clone (development stage only)
# (
#     git repository url,
#     git clone option,
#     folder name
# ),
clone_references = [
    (
        'https://github.com/pallets/click.git',
        '--tag=4.0',
        'click'
    ),
    (
        'https://github.com/requests/requests.git',
        '--tag=v2.18.4',
        'requests'
    ),
    (
        'https://github.com/psycopg/psycopg2.git',
        '--tag=2_5_4',
        'psycopg2'
    ),
    (
        'https://github.com/tryton/proteus.git',
        '--branch=' + tryton_version,
        'proteus'
    ),
    (
        'https://github.com/Pylons/webob.git',
        '--tag=v1.8.2',
        'webob'
    ),
    (
        'https://github.com/Pylons/pyramid.git',
        '--tag=1.9.2',
        'pyramid'
    ),
    (
        'https://github.com/Pylons/pyramid_beaker.git',
        '--tag=0.8',
        'pyramid_beaker'
    ),
    (
        'https://github.com/Pylons/pyramid_chameleon.git',
        '--tag=0.3',
        'pyramid_chameleon'
    ),
    (
        'https://github.com/Pylons/pyramid_mailer.git',
        '--tag=0.15.1',
        'pyramid_mailer'
    ),
    (
        'https://github.com/Pylons/colander.git',
        '--tag=1.4',
        'colander'
    ),
    (
        'https://github.com/Cornices/cornice.git',
        '--tag=3.4.0',
        'cornice'
    ),
    (
        'https://github.com/Pylons/deform.git',
        '--tag=2.0.5',
        'deform'
    ),
    (
        'https://github.com/jiaaro/pydub.git',
        '--tag=v0.22.0',
        'pydub'
    ),
    (
        'https://github.com/supermihi/pytaglib.git',
        '--tag=v1.4.3',
        'pytaglib'
    ),
    (
        'https://github.com/echonest/pyechonest.git',
        '--tag=9.0.0',
        'pyechonest'
    ),
]

if __name__ == "__main__":
    import pprint
    print("CONFIG\n------\n")
    pprint.pprint({
        'environment': environment,
        'tryton_version': tryton_version,
        'dirs': dirs,
        'create_folders': create_folders,
        'copy_files': copy_files,
        'clone_sources': clone_sources,
        'clone_references': clone_references,
    })
