# -*- coding: utf-8 -*-
# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society_docker
# flake8: noqa

# =========
# Test Data
# =========

# Preparation
# ===========

# Imports
# -------
# ::
    import os
    import csv
    import datetime
    import random
    import string
    import uuid
    from proteus import config, Model, Wizard
    # import interlude; interlude.interact(locals())

# Configuration
# -------------
# ::

    debug = False

    publisher = debug or 10
    label = debug or 10
    tariff_systems = debug or 3
    
    group_artists = debug or 3
    new_solo_artists_per_group = debug or 2
    add_solo_artists_per_group = debug or 1
    foreign_artists_per_group = debug or 1
    releases_per_artist = debug or 1
    creations_per_release = debug or 3
    genres_per_release = debug or 2
    styles_per_release = debug or 2
    release_cancellation_chance = debug and 1 or 0.3
    originals_per_creation = debug or 2
    foreign_originals_per_creation = debug and 1 or 1
    max_composers_per_creation = debug or 3
    max_recorders_per_creation = debug or 3
    max_texters_per_creation = debug or 2
    max_producers_per_creation = debug or 2
    max_masters_per_creation = debug or 2
    max_mixers_per_creation = debug or 2
    foreign_contribution_chance_per_creation = debug and 1 or 0.3
    audio_content_chance_per_creation = debug and 1 or 0.8
    lyric_content_chance_per_creation = debug and 1 or 0.6
    sheet_content_chance_per_creation = debug and 1 or 0.1

    sampler_releases = debug or 1
    creations_per_sampler = debug or 5
    split_releases = debug or 1
    artists_per_split_release = debug or 2
    creations_per_split_artist = debug or 2
    
    storehouses = debug or 2
    harddisklabels_per_storehouse = debug or 2
    harddisks_per_harddisklabel = debug or 2
    filesystemlabels_per_harddisk = debug or 2
    filesystems_per_filesystemlabel = debug or 2

    delimiter = ','
    quotechar = '"'

    config = config.set_trytond(
        config_file=os.environ.get('TRYTOND_CONFIG'))

# Models
# ------

# Upstream::

    Company = Model.get('company.company')
    User = Model.get('res.user')
    Country = Model.get('country.country')
    
# Extended::

    Party = Model.get('party.party')
    WebUser = Model.get('web.user')
    WebUserRole = Model.get('web.user.role')

# New::

    CollectingSociety = Model.get('collecting_society')
    TariffSystem = Model.get('tariff_system')
    TariffCategory = Model.get('tariff_system.category')
    Tariff = Model.get('tariff_system.tariff')
    Allocation = Model.get('distribution.allocation')
    Distribution = Model.get('distribution')
    
    License = Model.get('license')
    Artist = Model.get('artist')
    ArtistArtist = Model.get('artist-artist')
    ArtistRelease = Model.get('artist-release')
    ArtistPayeeAcceptance = Model.get('artist.payee.acceptance')
    Creation = Model.get('creation')
    CreationDerivative = Model.get('creation.original.derivative')
    CreationContribution = Model.get('creation.contribution')
    CreationContributionRole = Model.get('creation.contribution-creation.role')
    CreationRole = Model.get('creation.role')
    CreationTariffCategory = Model.get('creation-tariff_category')
    CreationRightsholder = Model.get('creation.rightsholder')
    Release = Model.get('release')
    ReleaseTrack = Model.get('release.track')
    ReleaseGenre = Model.get('release-genre')
    ReleaseStyle = Model.get('release-style')
    Genre = Model.get('genre')
    Style = Model.get('style')
    Label = Model.get('label')
    Publisher = Model.get('publisher')

    Utilisation = Model.get('utilisation')
    Fingerprintlog = Model.get('content.fingerprintlog')

    Storehouse = Model.get('storehouse')
    Harddisk = Model.get('harddisk')
    HarddiskLabel = Model.get('harddisk.label')
    HarddiskTest = Model.get('harddisk.test')
    Filesystem = Model.get('harddisk.filesystem')
    FilesystemLabel = Model.get('harddisk.filesystem.label')
    Content = Model.get('content')
    Checksum = Model.get('checksum')
    
    AccessControlEntry = Model.get('ace')
    AccessControlEntryRole = Model.get('ace-ace.role')
    AccessRole = Model.get('ace.role')
    AccessRolePermission = Model.get('ace.role-ace.permission')
    AccessPermission = Model.get('ace.permission')

# Content
# -------
# ::
    today = datetime.date.today()
    now = datetime.datetime.now()

    company, = Company.find([(
        'party.name', '=',
        'C3S SCE'
    )])
    germany, = Country.find([('code', '=', 'DE')])
    countries = Country.find([])

    contribution_types = [
        'composition',
        'performance',
        'text',
    ]
    
    performance_types = [
        'recording',
        'producing',
        'mastering',
        'mixing',
    ]

    allocation_types = [
        'adaption',
        'cover',
        'remix',
    ]

    test_genres = '/shared/data/csv/genres.csv'
    test_styles = '/shared/data/csv/styles.csv'
    test_labels = '/shared/data/csv/labels.csv'
    test_licenses = '/shared/data/csv/licenses.csv'
    test_tariff_categories = '/shared/data/csv/tariff_categories.csv'
    test_creation_roles = '/shared/data/csv/creation_roles.csv'

    test_text = '''Lorem ipsum dolor sit amet, consetetur diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren.\n\nLorem ipsum.\n\nSea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'''


# Data
# ====

# Collecting Societies
# --------------------

# C3S::

    CollectingSociety(
        name=company.party.name,
        party=company.party,
        represents_copyright=True,
        represents_ancillary_copyright=True
    ).save()

# Gema::

    party = Party(name='GEMA')
    _ = party.addresses.pop()
    party_address = party.addresses.new(
        street='Bayreuther Straße 37',
        zip='10787',
        city='Berlin',
        country=germany
    )
    party.save()
    CollectingSociety(
        name=party.name,
        party=party,
        represents_copyright=True,
        represents_ancillary_copyright=False
    ).save()
    
# GVL:: 

    party = Party(name='GVL')
    _ = party.addresses.pop()
    party_address = party.addresses.new(
        street='Podbielskiallee 64',
        zip='14195',
        city='Berlin',
        country=germany
    )
    party.save()
    CollectingSociety(
        name=party.name,
        party=party,
        represents_copyright=False,
        represents_ancillary_copyright=True
    ).save()

# Genres
# ------
# ::
    with open(test_genres, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for genre in reader:
            if debug and i > debug:
                break
            if label and i > label:
                break
            i += 1
            Genre(
                name=genre['name'],
                description=genre['description']
            ).save()

# Styles
# ------
# ::
    with open(test_styles, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for style in reader:
            if debug and i > debug:
                break
            i += 1
            Style(
                name=style['name'],
                description=style['description']
            ).save()

# Labels
# ------
# ::
    with open(test_labels, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for label in reader:
            if debug and i > debug:
                break
            i += 1
            Label(
                entity_creator=company.party,
                name=label['name'],
                gvl_code=label['gvl_code']
            ).save()

# Licenses
# --------
# ::
    with open(test_licenses, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for license in reader:
            if debug and i > debug:
                break
            i += 1
            License(
                code=license['code'],
                version=license['version'],
                country=license['country'],
                freedom_rank=int(license['freedom_rank']),
                link=license['link'],
                name=license['name']
            ).save()

# Tariff Systems
# --------------
# ::
    for i in range(1, tariff_systems + 1):
        number = i
        TariffSystem(
            version="%s.0" % number,
            valid_from=today
        ).save()

# Tariff Categories
# -----------------
# ::
    with open(test_tariff_categories, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for category in reader:
            if debug and i > debug:
                break
            i += 1
            TariffCategory(
                name=category['name'],
                code=category['code'],
                description=category['description']
            ).save()

# Tariffs
# -------
# ::
    tariff_systems = TariffSystem.find([])
    tariff_categories = TariffCategory.find([])

    for system in tariff_systems:
        for category in tariff_categories:
            Tariff(
                system=system,
                category=category
            ).save()

# Publisher
# ---------
# ::
    for i in range(1, publisher + 1):
        number = i
        name = "Publisher %s" % str(number).zfill(3)
        party = Party(name=name)
        party.save()
        Publisher(
            entity_creator=company.party,
            party=party,
            name=name,
        ).save()

# Web Users
# ---------
# ::
    for i in range(1, group_artists * new_solo_artists_per_group + 1):
        number = i
        birthdate = datetime.date(
            random.randint(1950, 2000),
            random.randint(1, 12),
            random.randint(1, 28))
        firstname = "Registered Name"
        lastname = "%s" % str(number).zfill(3)
        web_user = WebUser(
            email='%s@rep.test' % number,
            nickname=firstname + ' ' + lastname,
            password="%s" % number,
            opt_in_state='opted-in'
        )
        roles = WebUserRole.find([
            'OR',
            ('code', '=', 'licenser'),
            ('code', '=', 'licensee')])
        web_user.roles.extend(roles)
        if number % 2:
            web_user.default_role = 'licenser'
        else:
            web_user.default_role = 'licensee'
        web_user.save()
        web_user.party.firstname = firstname
        web_user.party.lastname = lastname
        web_user.party.name = firstname + ' ' + lastname
        web_user.party.repertoire_terms_accepted = True
        web_user.party.birthdate = birthdate
        web_user.party.save()

# Artists
# -------

# Create group and members artists::

    for i in range(1, group_artists + 1):
        number = i
        web_user_number = (number - 1) * new_solo_artists_per_group + 1
        web_user, = WebUser.find([(
            'nickname', '=', 'Registered Name %s' % str(
                web_user_number).zfill(3)
        )])
    
        # group artists
        group_artist = Artist(
            name="Group Artist %s" % str(number).zfill(3),
            group=True,
            entity_creator=web_user.party,
            entity_origin='direct',
            commit_state='commited',
            claim_state='claimed',
            description=test_text
        )
        group_artist.save()
    
        # members
        for j in range(1, new_solo_artists_per_group + 1):
            number = (i - 1) * new_solo_artists_per_group + j
            web_user, = WebUser.find([(
                'nickname', '=', 'Registered Name %s' % str(
                    number).zfill(3)
            )])
            solo_artist = group_artist.solo_artists.new(
                name="Solo Artist %s" % str(number).zfill(3),
                group=False,
                party=web_user.party,
                entity_creator=web_user.party,
                entity_origin='direct',
                commit_state='commited',
                claim_state='claimed',
                description=test_text
            )
            solo_artist.save()
            group_artist.save()
    
        # foreign members
        for k in range(1, foreign_artists_per_group + 1):
            number = (i - 1) * foreign_artists_per_group + k
            name = "Foreign Member Solo Artist %s" % str(number).zfill(3)
            foreign_solo_artist_party = Party(
                name=name
            )
            email = foreign_solo_artist_party.contact_mechanisms.new(
                type='email',
                value="foreign_member_%s@rep.test" % number
            )
            foreign_solo_artist_party.save()
            foreign_solo_artist = group_artist.solo_artists.new(
                name=name,
                group=False,
                party=foreign_solo_artist_party,
                entity_creator=web_user.party,
                entity_origin='indirect',
                commit_state='uncommited',
                claim_state='unclaimed'
            )
            foreign_solo_artist.save()
            group_artist.save()

# Add existing solo artists to group artists::

    groups = Artist.find([
        ('claim_state', '!=', 'unclaimed'),
        ('group', '=', True)])
    for i, group in enumerate(groups):
        solos = Artist.find([
            ('claim_state', '!=', 'unclaimed'),
            ('group', '=', False)])
        for j in range(0, add_solo_artists_per_group):
            if solos <= group.solo_artists:
                continue
            solo = random.choice(solos)
            while solo in group.solo_artists:
                solo = random.choice(solos)
            group.solo_artists.extend([solo])
            group.save()

# CreationRoles
# -------------
# ::
    with open(test_creation_roles, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
        i = 1
        for role in reader:
            if debug and i > debug:
                break
            i += 1
            artists = Artist.find([
                ('claim_state', '!=', 'unclaimed'),
                ('group', '!=', True)])
            CreationRole(
                entity_creator=random.choice(artists).party,
                name=role['name'],
                description=role['description']
            ).save()

# Releases
# --------
# ::
    artists = Artist.find([('claim_state', '!=', 'unclaimed')])

    for i in range(1, len(artists) + 1):
        for j in range(1, releases_per_artist + 1):
            number = (i - 1) * releases_per_artist + j
            owner = artists[i-1]
            creator = owner
            if creator.group:
                for solo in creator.solo_artists:
                    if solo.claim_state != 'unclaimed':
                        creator = solo
                        break
            publishers = Publisher.find([])
            labels = Label.find([])
            genres = Genre.find([])
            styles = Style.find([])
            release_date = datetime.date(
                random.randint(1800, 2017),
                random.randint(1, 12),
                random.randint(1, 28))
            isrc = ''.join(random.sample(string.ascii_uppercase, 3)) + \
                str(random.randint(1,999999999)).zfill(9)
            release = Release(
                type="artist",
                entity_creator=creator.party,
                commit_state='commited',
                claim_state='claimed',
                title="Release %s" % str(number).zfill(3),
                genres=random.sample(genres, min(
                    genres_per_release, len(genres))),
                styles=random.sample(styles, min(
                    styles_per_release, len(styles))),
                warning='WARNING: This is testdata!',
                copyright_date=release_date - datetime.timedelta(10),
                production_date=release_date - datetime.timedelta(30),
                release_date=release_date,
                online_release_date=release_date,
                distribution_territory=random.choice(countries).code,
                label=random.choice(labels),
                label_catalog_number=str(random.randint(10000, 99999)),
                publisher=random.choice(publishers)
            )
            if random.random() < release_cancellation_chance:
                cancellation_date = release_date + datetime.timedelta(300)
                release.release_cancellation_date = cancellation_date
                release.online_cancellation_date = cancellation_date
            owner_artist, = Artist.find([('id', '=', owner.id)])
            release.artists.append(owner_artist)
            release.save()

# CreationRightsholder
# --------------------
# ::
    creation_rightsholder = CreationRightsholder(
        right = copyright
        valid_from =
        valid_to =
        country =
        collecting_society =
        rightsholder_subject =
        rightsholder_object =
        contribution =
        successor =
        instruments =

# Creations
# ---------
# ::
    releases = Release.find([('claim_state', '!=', 'unclaimed')])

    for i in range(1, len(releases) + 1):
        for j in range(1, creations_per_release + 1):
            number = (i - 1) * creations_per_release + j
            artist_number = divmod(i-1, releases_per_artist)[0]
            artist = artists[artist_number]
            creator = artist
            if creator.group:
                creator = creator.solo_artists[0]
            # creation
            creation = Creation(
                title="Title of Song %s" % str(number).zfill(3),
                commit_state='commited',
                claim_state='claimed',
                entity_creator=creator.party,
                lyrics=test_text,
                artist=artist
            )
            creation.save()
    
            # tariff categories
            css = CollectingSociety.find([(
                'represents_copyright', '=', True)])
            tariffcs = TariffCategory.find([])
            categories = random.sample(
                tariffcs, random.randint(1, len(tariffcs)))
            for category in categories:
                CreationTariffCategory(
                    creation=creation,
                    category=category,
                    collecting_society=random.choice(css)
                ).save()
    
            # release creation
            licenses = License.find([])
            cr = creation.releases.new()
            cr.creation=creation
            cr.release=releases[i-1]
            cr.title="Release Title of Song %s" % str(number).zfill(3)
            cr.medium_number=1
            cr.track_number=j
            cr.license=random.choice(licenses)
            cr.save()
            creation.save()

# Derivatives
# -----------
# ::
    creations = Creation.find([('claim_state', '!=', 'unclaimed')])

# Exisiting creations::

    for i in range(0, len(creations)):
        creation = creations[i]
        if not creation.release:
            continue
        others = []
        for other in creations:
            if not other.release or other.id == creation.id:
                continue
            others.append(other)
        originals = random.sample(others, min(
            originals_per_creation, len(others)))
        for original in originals:
            cor = creation.original_relations.new()
            cor.original_creation = original
            cor.derivative_creation = creation
            cor.allocation_type = random.choice(allocation_types)
            cor.save()
            creation.save()

# Foreign originals::

    for i in range(0, len(creations)):
        creation = creations[i]
        for j in range(1, foreign_originals_per_creation + 1):
            number = i * foreign_originals_per_creation + j
            foreign_artist = Artist(
                name="Foreign Original Artist %s" % str(number).zfill(3),
                group=False,
                entity_creator=creation.entity_creator,
                entity_origin='indirect',
                commit_state='uncommited',
                claim_state='unclaimed'
            )
            foreign_artist.save()
            foreign_original = Creation(
                title="Foreign Original Song %s" % str(number).zfill(3),
                artist=foreign_artist,
                entity_creator=creation.entity_creator,
                entity_origin='indirect',
                commit_state='uncommited',
                claim_state='unclaimed'
            )
            foreign_original.save()
    
            cor = creation.original_relations.new()
            cor.original_creation = foreign_original
            cor.derivative_creation = creation
            cor.allocation_type = random.choice(allocation_types)
            cor.save()
            creation.save()

# Contributions
# -------------
# ::
    creations = Creation.find([('claim_state', '!=', 'unclaimed')])

# Existing solo or member artists::

    for i in range(0, len(creations)):
        creation = creations[i]
        artist = creation.artist
        contributors = [artist]
        if artist.group:
            contributors = artist.solo_artists
        roles = CreationRole.find([])
        
        # composer
        num_composers = random.randint(0, min(
            max_composers_per_creation, len(contributors)))
        for composer in random.sample(contributors, num_composers):
            # composition
            cc = CreationContribution()
            cc.creation = creation
            cc.artist = composer
            cc.type = 'composition'
            cc.save()
            cr = CreationContributionRole()
            cr.contribution = cc
            cr.role = random.choice(roles)
            cr.save()
        
        # recorder
        num_recorders = random.randint(0, min(
            max_recorders_per_creation, len(contributors)))
        for recorder in random.sample(contributors, num_recorders):
            # composition
            cc = CreationContribution()
            cc.creation = creation
            cc.artist = recorder
            cc.type = 'performance'
            cc.performance = 'recording'
            cc.save()
            cr = CreationContributionRole()
            cr.contribution = cc
            cr.role = random.choice(roles)
            cr.save()
    
        # texter
        num_texters = random.randint(0, min(
            max_texters_per_creation, len(contributors)))
        for texter in random.sample(contributors, num_texters):
            CreationContribution(
                creation=creation,
                artist=texter,
                type='text'
            ).save()
    
        # producer
        nrss = CollectingSociety.find([(
            'represents_ancillary_copyright', '=', True)])
        num_producers = random.randint(0, min(
            max_producers_per_creation, len(contributors)))
        for producer in random.sample(contributors, num_producers):
            CreationContribution(
                creation=creation,
                artist=producer,
                type='performance',
                performance='producing',
                neighbouring_rights_society=random.choice(nrss),
            ).save()
    
        # master
        nrss = CollectingSociety.find([(
            'represents_ancillary_copyright', '=', True)])
        num_masters = random.randint(0, min(
            max_masters_per_creation, len(contributors)))
        for master in random.sample(contributors, num_masters):
            CreationContribution(
                creation=creation,
                artist=master,
                type='performance',
                performance='mastering',
                neighbouring_rights_society=random.choice(nrss),
            ).save()
    
        # mixer
        nrss = CollectingSociety.find([(
            'represents_ancillary_copyright', '=', True)])
        num_mixers = random.randint(0, min(
            max_mixers_per_creation, len(contributors)))
        for mixer in random.sample(contributors, num_mixers):
            CreationContribution(
                creation=creation,
                artist=mixer,
                type='performance',
                performance='mixing',
                neighbouring_rights_society=random.choice(nrss),
            ).save()

# Foreign contributions::
    
    number = 0
    for i in range(0, len(creations)):
        if random.random() > foreign_contribution_chance_per_creation:
            continue
        number = number + 1
        creation = creations[i]
        roles = CreationRole.find([])
        nrss = CollectingSociety.find([(
            'represents_ancillary_copyright', '=', True)])
        
        # foreign artist
        name = "Foreign Contributor Solo Artist %s" % str(
            number).zfill(3)
        foreign_solo_artist_party = Party(
            name=name
        )
        email = foreign_solo_artist_party.contact_mechanisms.new(
            type='email',
            value="foreign_contributor_%s@rep.test" % number
        )
        foreign_solo_artist_party.save()
        foreign_solo_artist = Artist(
            name=name,
            group=False,
            party=foreign_solo_artist_party,
            entity_creator=creation.entity_creator,
            entity_origin='indirect',
            commit_state='uncommited',
            claim_state='unclaimed'
        )
        foreign_solo_artist.save()
        
        # contribution
        cc = CreationContribution()
        cc.creation = creation
        cc.artist = foreign_solo_artist
        cc.type = random.choice(contribution_types)
        if cc.type == 'performance':
            cc.performance = random.choice(performance_types)
            if random.choice([False, True]):
                cc.neighbouring_rights_society = random.choice(nrss)
        cc.save()
        
        # contribution role
        if cc.type == 'composition' or cc.performance == 'recording':
            cr = CreationContributionRole()
            cr.contribution = cc
            cr.role = random.choice(roles)
            cr.save()

# Sampler Releases
# ----------------

    artists = Artist.find([('claim_state', '!=', 'unclaimed')])

    for i in range(1, sampler_releases + 1):
        number = i
        solos = Artist.find([
            ('claim_state', '!=', 'unclaimed'),
            ('group', '=', False)])
        labels = Label.find([])
        genres = Genre.find([])
        styles = Style.find([])
        isrc = ''.join(random.sample(string.ascii_uppercase, 3)) + \
            str(random.randint(1,999999999)).zfill(9)
        creations = Creation.find([('claim_state', '!=', 'unclaimed')])
        publishers = Publisher.find([])
        creator = random.choice(solos)
        web_user, = WebUser.find([('party.id', '=', creator.party.id)])
    
        # release
        release = Release(
            type="compilation",
            entity_creator=creator.party,
            commit_state='commited',
            claim_state='claimed',
            title="Sampler %s" % str(number).zfill(3),
            genres=random.sample(genres, min(
                genres_per_release, len(genres))),
            styles=random.sample(styles, min(
                styles_per_release, len(styles))),
            warning='WARNING: This is testdata!',
            distribution_territory=random.choice(countries).code,
            label=random.choice(labels),
            label_catalog_number=str(random.randint(10000, 99999)),
            publisher=random.choice(publishers)
        )
        release.save()
    
        # release creation
        tracks = random.sample(creations, creations_per_sampler)
        last_date = datetime.date(1,1,1)
        for i in range(0, len(tracks)):
            track = tracks[i]
            if track.release.release_date > last_date:
                last_date = track.release.release_date
            licenses = License.find([])
            rc = ReleaseTrack()
            rc.creation=track
            rc.release=release
            rc.title="Renamed Song %s on a Compilation" % str(
                number).zfill(3)
            rc.medium_number=1
            rc.track_number=i
            rc.license=random.choice(licenses)
            rc.save()
    
        release.production_date = last_date + datetime.timedelta(50)
        release.copyright_date = last_date + datetime.timedelta(80)
        release.release_date = last_date + datetime.timedelta(100)
        release.online_release_date = last_date + datetime.timedelta(100)
        release.save()

# Split Releases
# --------------

    for i in range(1, split_releases + 1):
        number = i
        artists = Artist.find([('claim_state', '!=', 'unclaimed')])
        labels = Label.find([])
        genres = Genre.find([])
        styles = Style.find([])
        isrc = ''.join(random.sample(string.ascii_uppercase, 3)) + \
            str(random.randint(1,999999999)).zfill(9)
        creations = Creation.find([('claim_state', '!=', 'unclaimed')])
        publishers = Publisher.find([])
    
        splits = random.sample(artists, artists_per_split_release)
        creator = splits[0]
        if creator.group:
            creator = creator.solo_artists[0]
    
        # release
        release = Release(
            type='split',
            entity_creator=creator.party,
            commit_state='commited',
            claim_state='claimed',
            title="Split Release %s" % str(number).zfill(3),
            genres=random.sample(genres, min(
                genres_per_release, len(genres))),
            styles=random.sample(styles, min(
                styles_per_release, len(styles))),
            warning='WARNING: This is testdata!',
            distribution_territory='Germany',
            label=random.choice(labels),
            label_catalog_number='12345',
            publisher=random.choice(publishers)
        )
        for split in splits:
            release.artists.append(split)
        release.save()
    
        # release creation
        last_date = datetime.date(1,1,1)
        for split in splits:
            tracks = random.sample(split.creations, 
                min(creations_per_split_artist,len(split.creations)))
            for i in range(0, len(tracks)):
                track = tracks[i]
                if track.release.release_date > last_date:
                    last_date = track.release.release_date
                licenses = License.find([])
                rc = ReleaseTrack()
                rc.creation=track
                rc.release=release
                rc.title="Renamed Song %s on a Split Release" % str(
                    number).zfill(3)
                rc.medium_number=1
                rc.track_number=i
                rc.license=random.choice(licenses)
                rc.save()
    
        release.production_date = last_date + datetime.timedelta(50)
        release.copyright_date = last_date + datetime.timedelta(80)
        release.release_date = last_date + datetime.timedelta(100)
        release.online_release_date = last_date + datetime.timedelta(100)
        release.save()


# Archiving
# ---------
# ::
    for i in range(1, storehouses + 1):
        number = i
        host = uuid_host=str(uuid.uuid4())
        
        # admin
        admin = User(
            name="Storehouse Admin %s" % str(number).zfill(3),
            login="storehouse%s" % str(number).zfill(3),
            password="%s" % number
        )
        admin.save()
        
        # storehouse
        storehouse = Storehouse(
            code="%s" % str(number).zfill(3),
            details="Storehouse in City %s" % str(number).zfill(3),
            user=admin
        )
        storehouse.save()
    
        # harddisk labels
        for j in range(1, harddisklabels_per_storehouse + 1):
            harddisk_label = HarddiskLabel()
            harddisk_label.save()
        
            # harddisks
            for k in range(1, harddisks_per_harddisklabel + 1):
                harddisk = Harddisk(
                    label=harddisk_label,
                    version=1,
                    storehouse=storehouse,
                    location='SomeMachine',
                    closed=False,
                    raid_type="1",
                    raid_number=str(k),
                    raid_total=str(harddisks_per_harddisklabel),
                    uuid_host=host,
                    uuid_harddisk=str(uuid.uuid4()),
                    user=admin,
                    online=True,
                    state='in_use'
                )
                harddisk.save()
    
                # filesystem labels
                for l in range(1, filesystemlabels_per_harddisk + 1):
                    filesystem_label = FilesystemLabel()
                    filesystem_label.save()
    
                    # filesystems
                    for m in range(1, filesystems_per_filesystemlabel + 1):
                        filesystem = Filesystem(
                            label=filesystem_label,
                            harddisk=harddisk,
                            closed=False,
                            partition_number=m,
                            uuid_partition=str(uuid.uuid4()),
                            uuid_raid=str(uuid.uuid4()),
                            uuid_raid_sub=str(uuid.uuid4()),
                            uuid_crypto=str(uuid.uuid4()),
                            uuid_lvm=str(uuid.uuid4()),
                            uuid_filesystem=str(uuid.uuid4())
                        )
                        filesystem.save()

# Contents
# --------
# ::
    creations = Creation.find([('claim_state', '!=', 'unclaimed')])
    filesystem_labels = FilesystemLabel.find([])

# Audio Files::

    audio_number = 1
    for i in range(1, len(creations) + 1):
        if random.random() > audio_content_chance_per_creation:
            continue
        creation = creations[i - 1]
        artist = creation.artist
        if artist.group:
            artist = artist.solo_artists[0]
        
        # audio
        c = Content()
        c.uuid = str(uuid.uuid4())
        c.commit_state = 'commited'
        c.entity_creator = artist.party
        c.category = 'audio'
        c.creation = creation
        # file metadata
        c.name = "audio_%s.wav" % str(audio_number).zfill(3)
        c.size = 12345
        c.mime_type = 'audio/x-wav'
        # file processing
        c.path = '/some/path'
        c.preview_path = '/some/preview/path'
        c.filesystem_label = random.choice(filesystem_labels)
        c.processing_state = 'archived'
        c.storage_hostname = 'archive_machine'
        c.mediation = False
        # low level audio metadata
        c.length = 42.0
        c.channels = 2
        c.sample_rate = 48000
        c.sample_width = 16
        # high level metadata
        c.metadata_artist = creation.artist.name
        c.metadata_title = creation.title
        c.metadata_release = creation.release.title
        c.metadata_release_date = str(creation.release.release_date)
        c.metadata_track_number = "0"
        c.save()
        audio_number += 1

# Sheet Pdfs::

    sheet_number = 1
    for i in range(1, len(creations) + 1):
        if random.random() > sheet_content_chance_per_creation:
            continue
        creation = creations[i - 1]
        artist = creation.artist
        if artist.group:
            artist = artist.solo_artists[0]

        c = Content()
        c.uuid = str(uuid.uuid4())
        c.entity_creator = artist.party
        c.category = 'sheet'
        c.creation = creation
        # file metadata
        c.name = "sheet_%s.pdf" % str(sheet_number).zfill(3)
        c.size = 54321
        c.mime_type = 'application/pdf'
        # file processing
        c.path = '/some/path'
        c.filesystem_label = random.choice(filesystem_labels)
        c.processing_state = 'archived'
        c.storage_hostname = 'archive_machine'
        c.mediation = False
        c.save()
        sheet_number += 1
