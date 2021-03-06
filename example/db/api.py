#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# filename   : api.py<2>
# created at : 2013-07-01 21:09:07


import abc

from example.openstack.common.db import api as dbapi

_BACKEND_MAPPING = {'sqlalchemy': 'example.db.sqlalchemy.api'}
IMPL = dbapi.DBAPI(backend_mapping=_BACKEND_MAPPING)


def get_instance():
    """Return a DB API instance."""
    return IMPL


class Ex(object):
    """Base db class."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """Constructor"""

    @abc.abstractmethod
    def get_ex(self, ex):
        """get ex by uuid of and uuid of its ex.

        :param ex: uuid of the ex
        :return: a list of exs
        """

    @abc.abstractmethod
    def get_exs(self):
        """get list of exs by uuid

        :return: a dict of values of the ex
        """

    @abc.abstractmethod
    def create_ex(self, values):
        """create a ex

        :param values: a dict of ex data
        :return: a dict of newly created ex data
        """

    @abc.abstractmethod
    def destroy_ex(self, ex):
        """delete a ex

        :param ex: uuid of the ex
        """

    @abc.abstractmethod
    def update_ex(self, ex, values):
        """update a ex

        :param ex: uuid of the ex
        :param values: a dict of update values
        :return: a dict of newly updated ex
        """
