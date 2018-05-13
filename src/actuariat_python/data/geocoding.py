# -*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about **French** elections.
"""
import os
import warnings
import pandas
import numpy


def geocode(df, col_city="city", col_place="place", col_zip="zip", col_address="address",
            col_latitude="latitude", col_longitude="longitude", col_full="full_address",
            col_geo="geo_address", save_every=None, every=100, exc=True, fLOG=None,
            coders=("Nominatim",), country=None, **options):
    """
    geocode addresses

    @param      df              dataframe
    @param      col_city        city
    @param      col_place       place
    @param      col_zip         zip
    @param      col_address     address
    @param      col_latitude    latitude
    @param      col_longitude   longitude
    @param      col_full        full address (send to the geocoder)
    @param      col_geo         address returned by the geocoder
    @param      save_every      to make regular dump
    @param      every           save every *every*
    @param      exc             raises exception or warning (False)
    @param      options         options for `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>`_
                                to do regular dumps
    @param      coders          list of coders to try
    @param      country         append the country before geocoding
    @param      fLOG            logging function
    @return                     modified dataframe

    If *save_every_100* is filled, the function will save the dataframe
    every 100 geocoded addresses. If the file is already present,
    it will be loaded the function will continue geocoding where it stopped.

    The function does not work well if it is called from multiple threads or processes.
    It might slow on purpose.

    Example for *coder*:

    ::

        ["Nominatim", ("bing", <bing_key>)]

    The function tries the first one and then the second one.
    The function also caches the results. If the same address appears twice,
    the geocoder will not be called a second time, it will reuse the cache results
    unless there was no answer on the first call.
    """
    from geopy.geocoders import Nominatim, Bing

    def get_coder(d):
        if isinstance(d, str):
            if d == "Nominatim":
                return Nominatim()
            else:
                raise ValueError("Unknown geocoder '{0}'".format(d))
        elif isinstance(d, tuple):
            name, key = d
            if name == "bing":
                return Bing(key)
            else:
                raise ValueError("Unknown geocoder '{0}'".format(d))
        else:
            raise TypeError("Unexpected type '{0}'".format(type(d)))

    if every < 1:
        raise ValueError("every should be >= 1, not {0}".format(every))
    from geopy.exc import GeocoderServiceError
    geocoder = [get_coder(_) for _ in coders]
    cache = {}
    if len(geocoder) == 0:
        raise ValueError(
            "No geocoder, the function cannot retrieve addresses.")

    class DummyClass:

        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    if save_every is not None and os.path.exists(save_every):
        if "index" in options:
            options_read = options.copy()
            del options_read["index"]
        else:
            options_read = options
        if fLOG:
            fLOG("load ", save_every)
        read = pandas.read_csv(save_every, **options_read)
        cols = list(read.columns)
        add = [_ for _ in [col_full, col_latitude,
                           col_longitude, col_geo] if _ not in df.columns]
        oris = list(df.columns) + add
        if oris != cols:
            raise ValueError(
                "Unexpected differences in schemas:\nORIGINAL\n{0}\nSAVE\n{1}".format(oris, cols))
        df = read
    else:
        df = df.copy()
        df[col_full] = numpy.nan
        df[col_latitude] = numpy.nan
        df[col_longitude] = numpy.nan
        df[col_geo] = numpy.nan

    errors = 0
    no_result = 0
    lasti = 0
    for i in range(0, len(df)):
        lasti = i
        if i % every == 0:
            if save_every is not None:
                if fLOG is not None:
                    fLOG(
                        "saving place {0}/{1} - errors={2} - no-result={3}".format(i, len(df), errors, no_result))
                df.to_csv(save_every, **options)
            elif fLOG is not None:
                fLOG(
                    "geocode place {0}/{1} - errors={2} - no-result={3}".format(i, len(df), errors, no_result))

        place, zips, city, address = df.loc[
            i, [col_place, col_zip, col_city, col_address]]
        if not isinstance(zips, str):
            zips = "%05d" % zips

        def concat(s1, s2):
            if isinstance(s1, str) and len(s1) > 0:
                return s1
            if isinstance(s2, str) and len(s2) > 0:
                return s2
            return ""

        ad = "{0} {1} {2}".format(concat(address, place), zips, city).strip()
        if country is not None:
            ad += " " + country
        df.loc[i, col_full] = ad

        if numpy.isnan(df.loc[i, col_latitude]) or numpy.isnan(df.loc[i, col_longitude]):

            if ad in cache:
                geo = cache[ad]
                if geo is None:
                    raise ValueError(
                        "Do not populate the cache with None values for key '{0}'".format(ad))
                rexc = None
            else:
                geo = None
                for cod in geocoder:
                    try:
                        geo = cod.geocode(ad, exactly_one=True, timeout=30)
                        rexc = None
                        if geo is not None:
                            break
                    except (TimeoutError, GeocoderServiceError) as e:
                        geo = None
                        rexc = e

            if geo is not None:
                df.loc[i, col_longitude] = geo.longitude
                df.loc[i, col_latitude] = geo.latitude
                df.loc[i, col_geo] = geo.address
            elif rexc:
                no_result += 1
                errors += 1
                if exc:
                    if save_every is not None:
                        df.to_csv(save_every, **options)
                    raise rexc
                else:
                    warnings.warn(str(rexc))
                    continue
            else:
                no_result += 1

        if ad not in cache:
            cache[ad] = DummyClass(longitude=df.loc[i, col_longitude],
                                   latitude=df.loc[i, col_latitude],
                                   address=df.loc[i, col_geo])

    if fLOG is not None:
        fLOG(
            "geocode place {0}/{1} - errors={2} - no-result={3}".format(lasti, len(df), errors, no_result))
    if save_every is not None:
        df.to_csv(save_every, **options)
    return df
