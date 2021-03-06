#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society_docker

"""
Create the utilizations
"""

import random

from proteus import Model

DEPENDS = [
    'declaration',
    'distribution_plan'
]


def generate(reclimit=0):

    # models
    DistributionPlan = Model.get('distribution.plan')
    Declaration = Model.get('declaration')
    Utilisation = Model.get('utilisation')

    # prepare datasets we depend upon
    all_declarations = Declaration.find([])
    all_distribution_plans = DistributionPlan.find([])

    # create one utilization per declaration
    for declaration in all_declarations:
        Utilisation(
            declaration=declaration,
            licensee=declaration.licensee,
            state=declaration.state,
            start=declaration.creation_time,
            tariff=declaration.tariff,
            context=declaration.context,
            distribution_plan=random.choice(all_distribution_plans)
        ).save()
