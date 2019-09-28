# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/c3s.ado.repertoire

repositories = (
    # (
    #     git repository url or None.
    #     git clone option, required if repository is given.
    #     relative path to create or clone.
    # ),
    (
        None,
        None,
        'postgresql-data'
    ),
    (
        None,
        None,
        'shared/var/lib/trytond'
    ),
    # sourcecode of libraries for reference
    (
        'https://github.com/pallets/click.git',
        '--tag=4.0',
        'shared/ref/click'
    ),
    (
        'https://github.com/requests/requests.git',
        '--tag=v2.18.4',
        'shared/ref/requests'
    ),
    (
        'https://github.com/psycopg/psycopg2.git',
        '--tag=2_5_4',
        'shared/ref/psycopg2'
    ),
    (
        'https://github.com/tryton/proteus.git',
        '--branch=3.4',
        'shared/ref/proteus'
    ),
    (
        'https://github.com/Pylons/webob.git',
        '--tag=v1.8.2',
        'shared/ref/webob'
    ),
    (
        'https://github.com/Pylons/pyramid.git',
        '--tag=1.9.2',
        'shared/ref/pyramid'
    ),
    (
        'https://github.com/Pylons/pyramid_beaker.git',
        '--tag=0.8',
        'shared/ref/pyramid_beaker'
    ),
    (
        'https://github.com/Pylons/pyramid_chameleon.git',
        '--tag=0.3',
        'shared/ref/pyramid_chameleon'
    ),
    (
        'https://github.com/Pylons/pyramid_mailer.git',
        '--tag=0.15.1',
        'shared/ref/pyramid_mailer'
    ),
    (
        'https://github.com/Pylons/colander.git',
        '--tag=1.4',
        'shared/ref/colander'
    ),
    (
        'https://github.com/Cornices/cornice.git',
        '--tag=3.4.0',
        'shared/ref/cornice'
    ),
    (
        'https://github.com/Pylons/deform.git',
        '--tag=2.0.5',
        'shared/ref/deform'
    ),
    (
        'https://github.com/jiaaro/pydub.git',
        '--tag=v0.22.0',
        'shared/ref/pydub'
    ),
    (
        'https://github.com/supermihi/pytaglib.git',
        '--tag=v1.4.3',
        'shared/ref/pytaglib'
    ),
    (
        'https://github.com/echonest/pyechonest.git',
        '--tag=9.0.0',
        'shared/ref/pyechonest'
    ),
    # included repositories
    (
        'https://github.com/tryton/trytond.git',
        '--branch=3.4',
        'shared/src/trytond'
    ),
    (
        'https://github.com/tryton/country.git',
        '--branch=3.4',
        'shared/src/country'
    ),
    (
        'https://github.com/tryton/currency.git',
        '--branch=3.4',
        'shared/src/currency'
    ),
    (
        'https://github.com/tryton/party.git',
        '--branch=3.4',
        'shared/src/party'
    ),
    (
        'https://github.com/tryton/company.git',
        '--branch=3.4',
        'shared/src/company'
    ),
    (
        'https://github.com/tryton/product.git',
        '--branch=3.4',
        'shared/src/product'
    ),
    (
        'https://github.com/tryton/account.git',
        '--branch=3.4',
        'shared/src/account'
    ),
    (
        'https://github.com/tryton/account_product.git',
        '--branch=3.4',
        'shared/src/account_product'
    ),
    (
        'https://github.com/tryton/account_invoice.git',
        '--branch=3.4',
        'shared/src/account_invoice'
    ),
    (
        'https://github.com/tryton/account_invoice_line_standalone.git',
        '--branch=3.4',
        'shared/src/account_invoice_line_standalone'
    ),
    (
        'https://github.com/tryton/bank.git',
        '--branch=3.4',
        'shared/src/bank'
    ),
    (
        'https://github.com/virtualthings/web_user.git',
        '--branch=3.4',
        'shared/src/web_user'
    ),
    (
        'https://github.com/C3S/collecting_society.git',
        '--branch=develop',
        'shared/src/collecting_society'
    ),
    (
        'https://github.com/C3S/collecting_society.portal.git',
        '--branch=develop',
        'shared/src/collecting_society.portal'
    ),
    (
        'https://github.com/C3S/collecting_society.portal.repertoire.git',
        '--branch=develop',
        'shared/src/collecting_society.portal.repertoire'
    ),
    (
        'https://github.com/C3S/c3sRepertoireProcessing.git',
        '--branch=master',
        'shared/src/c3sRepertoireProcessing'
    ),
    (
        'https://github.com/spotify/echoprint-codegen.git',
        '--branch=master',
        'shared/src/echoprint-codegen'
    ),
)

configfiles = (
    (
        'shared/etc/trytonpassfile.example',
        'shared/etc/trytonpassfile',
    ),
    (
        'tryton.env.example',
        'tryton.env'
    ),
    (
        'portal.env.example',
        'portal.env'
    ),
    (
        'api.env.example',
        'api.env'
    ),
    (
        'processing.env.example',
        'processing.env'
    ),
    (
        'selenium.env.example',
        'selenium.env'
    ),
    (
        'shared/src/c3sRepertoireProcessing/config.ini.EXAMPLE',
        'shared/src/c3sRepertoireProcessing/config.ini'
    ),
)
