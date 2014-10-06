from __future__ import (absolute_import, print_function)

from pyugrid.util import point_in_tri
import numpy as np


def test_point_in_tri():
    test_datasets = [
        {
            'triangle': np.array([[0., 0.],[1.,0.],[0.,1.]]),
            'points_inside': [np.array([0.1,0.1]), np.array([0.3,0.3])],
            'points_outside': [np.array([5.,5.])],
        },
    ]

    for dataset in test_datasets:
        for point in dataset['points_inside']:
            assert point_in_tri(dataset['triangle'], point)
        for point in dataset['points_outside']:
            assert ~point_in_tri(dataset['triangle'], point)
