import pickle, time

from trying_stuffs import timefunc, memoize
# from filters import create_filters
# from workspace.trying_stuffs import timefunc, memoize
from extract import load_neos, load_approaches

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches.
    """
    def __init__(self, neos=(), approaches=()):
    # def __init__(self, neos=load_neos(), approaches=load_approaches()):
        self._neos = neos
        self._approaches = approaches

        @timefunc
        @memoize
        def link_together():
            for neo in self._neos:
                for appr in self._approaches:
                    if neo.designation == appr._designation:
                        neo.approaches.append(appr)
                        appr.neo = neo
                # print(neo.fullname)
        link_together()


    @timefunc
    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation."""
        for neo in self._neos:
            if neo.designation == designation:
                return neo
        return None

    @timefunc
    # @memoize
    def get_neo_by_name(self, name):
        """Find and return an NEO by its name."""
        for neo in self._neos:
            if neo.name == name:
                return neo
        return None

    def query(self, filters):  # =(create_filters(date='2099-12-31'))
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.
        """
        if not filters:
            for approach in self._approaches:
                yield approach

        for ind, filt in enumerate(filters):
            if ind == 0:
                for approach in self._approaches:
                    if all (filters[index](approach) for index in range(len(filters))):
                        yield approach
                # print(ind, 'collection_of_filters: ', filters)
            break
