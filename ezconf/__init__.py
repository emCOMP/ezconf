#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import json

version = '0.1'

class ConfigFile(object):
    """
    Simple JSON config file class
    """

    def __init__(self, filename, userConfFilename=None):
        """
        initialize data and call to load the data.

        Searches for filename in current directory, if it's not present
        and userConfFilename is specified, then the user's home directory
        is sear
        """
        self.config_data = {}

        filename = self.findConfigFile(filename, userConfFilename)

        if filename is not None:
            self.loadConfig(filename)

    def findConfigFile(self, filename, userConfFilename):
        """ Finds the filename somewhere. """
        if path.exists(filename):
            return filename

        # doesn't exist, check for userConfFilename in user's home dir
        if userConfFilename is not None:
            fn = path.join(path.expanduser("~"), userConfFilename)
            if path.exists(fn):
                return fn

        # None found
        return None

    def loadConfig(self, filename):
        """ load the config file. """
        with open(filename) as f:
            self.config_data = json.load(f)

    def getValue(self, path, defaultValue=None):
        """
        gets a value from the config data.
        can also take a path using the period as a separator.
        eg "first.second.third"
        """

        if not path:
            return None

        parts = path.split(".")
        num_parts = len(parts)
        cur_dict = self.config_data

        try:
            for i in range(0, num_parts-1):
                part = parts[i]
                cur_dict = cur_dict[part]

            return cur_dict[parts[num_parts-1]]
        except KeyError:
            return defaultValue

    def __len__(self):
        """
        returns the length from len()
        """
        return len(self.config_data)

    def __getitem__(self, key):
        """
        returns the item like a dictionary
        """
        return self.config_data[key]

    def __setitem__(self, key, value):
        """
        sets the item like a dictionary
        """
        self.config_data[key] = value

    def __delitem__(self, key):
        """
        deletes a config item by its key
        """
        del self.config_data[key]

    def __iter__(self):
        """
        returns an key iterator for the config data
        """
        return self.config_data.iterkeys()

    def __contains__(self, key):
        """
        returns True if the key is in the config file
        """
        return key in self.config_data


