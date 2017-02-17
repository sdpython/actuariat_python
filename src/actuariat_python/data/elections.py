#-*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about **French** elections.
"""
import re
import os
import warnings
import pandas
import urllib.error
import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.error import HTTPError, URLError
from .data_exceptions import DataNotAvailableError, DataFormatException
from pyquickhelper.loghelper import noLOG
from pyquickhelper.filehelper import unzip_files
from pyensae.datasource import download_data
from pyensae.datasource.http_retrieve import DownloadDataException


def elections_presidentielles_local_files(load=False):
    """
    return the list of files included in this module about French elections

    @param      load        True: load the data
    @return                 list of local files

    If the data is loaded, the function returns a dictionary of dataframe,
    one per round.
    """
    this = os.path.dirname(__file__)
    data = os.path.abspath(os.path.join(this, "data_elections"))
    res = [os.path.join(data, "cdsp_presi2012t1_circ.xls"),
           os.path.join(data, "cdsp_presi2012t2_circ.xls")]
    for r in res:
        if not os.path.exists(r):
            raise FileNotFoundError(r)

    if not load:
        return res
    else:
        df1 = pandas.read_excel(res[0], sheetname=1)
        df2 = pandas.read_excel(res[1], sheetname=1)
        return dict(circ1=df1, circ2=df2)


def elections_presidentielles(url=None, local=False, agg=None):
    """
    download the data for the French elections from *data.gouv.fr*

    @param      url             url (None for default value)
    @param      local           prefer local data instead of remote
    @param      agg             kind of aggregation desired (see below)
    @return                     dictionaries of DataFrame (one entry for each round)

    The default url comes from
    `Elections présidentielle 2012 - Résultats <https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572124/>`_.
    You can get more at
    `Elections présidentielles 1965-2012 <https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/>`_.

    If url is None, we pull some data from folder
    :ref:`data/election <l-data-elections>`.

    Parameter *agg*:

    * *circ* or *None* for no aggregation
    * *dep* to aggregate per department
    """
    if agg is None:
        if local:
            return elections_presidentielles_local_files(load=True)
        else:
            if url is None:
                url = "http://static.data.gouv.fr/ff/e9c9483d39e00030815089aca1e2939f9cb99a84b0136e43056790e47bb4f0.xls"
                url0 = None
            else:
                url0 = url
            try:
                df = pandas.read_excel(url, sheetname=None)
                return df
            except (HTTPError, URLError, TimeoutError) as e:
                if url0 is None:
                    return elections_presidentielles_local_files(load=True)
                else:
                    raise DataNotAvailableError(
                        "unable to get data from " + url) from e
    else:
        res = elections_presidentielles(url=url, local=local, agg=None)
        if agg == "circ":
            return res
        elif agg == "dep":
            keys = list(res.keys())
            for k in keys:
                col = res[k].columns
                key = col[:2]
                df = res[k].groupby(list(key))
                df = df.sum()
                df = df.reset_index(drop=False)
                res["dep" + k[-1:]] = df
            return res
        else:
            raise ValueError("unkown value for agg: '{0}'".format(agg))


def elections_legislatives_bureau_vote(source=None, folder=".", fLOG=noLOG):
    """
    retrieve data from
    `Résultat des élections législatives françaises de 2012 au niveau bureau de vote <https://www.data.gouv.fr/fr/datasets/resultat-des-elections-legislatives-francaises-de-2012-au-niveau-bureau-de-vote-nd/>`_

    @param      source  should be None unless you want to use the backup plan ("xd")
    @param      folder  where to download
    @return             list of dataframe

    Others sources:

    * `Résultats élections municipales 2014 par bureau de vote <http://www.nosdonnees.fr/dataset/resultats-elections-municipales-2014-par-bureau-de-vote>`_
    * `Elections 2015 - Découpage des bureaux de Vote <https://www.data.gouv.fr/fr/datasets/elections-2015-decoupage-des-bureaux-de-vote/>`_
    * `Contours des cantons électoraux départementaux 2015 <https://www.data.gouv.fr/fr/datasets/contours-des-cantons-electoraux-departementaux-2015/>`_
    * `Découpage électoral de la commune, pour les élections législatives <https://www.data.gouv.fr/fr/datasets/circonscriptions/>`_ (weird bizarre)
    * `Statistiques démographiques INSEE sur les nouvelles circonscriptions législatives de 2012 <https://www.data.gouv.fr/fr/datasets/statistiques-demographiques-insee-sur-les-nouvelles-circonscriptions-legislatives-de-2012-nd/>`_
    """
    if source is None:
        try:
            with urllib.request.urlopen("http://www.nosdonnees.fr/") as f:
                url = "http://www.nosdonnees.fr/storage/f/2013-03-05T184148/"
                if f is None:
                    raise Exception(
                        "Not sure we can continue. Pretty sure we should stop.")
        except urllib.error.HTTPError as e:
            url = "xd"
        file = "LG12_BV_T1T2.zip"
    else:
        url = source
        file = "LG12_BV_T1T2.zip"
    data = download_data(file, website=url, whereTo=folder, fLOG=fLOG)
    res = {}
    for d in data:
        df = pandas.read_csv(d, encoding="latin-1", sep=";", low_memory=False)
        if d.endswith("_T2.txt"):
            key = "T2"
        elif d.endswith("_T1.txt"):
            key = "T1"
        else:
            raise ValueError(
                "unable to guess key for filename: '{0}'".format(d))
        res[key] = df
    return res


def elections_legislatives_circonscription_geo(source="xd", folder=".", fLOG=noLOG):
    """
    retrieve data from
    `Countours des circonscriptions des législatives <https://www.data.gouv.fr/fr/datasets/countours-des-circonscriptions-des-legislatives-nd/>`_

    @param      source  should be None unless you want to use the backup plan ("xd")
    @param      folder  where to download
    @return             list of dataframe
    """
    if source is None:
        raise NotImplementedError("use source='xd'")
    else:
        url = source
        file = "toxicode_circonscriptions_legislatives.zip"
    data = download_data(file, website=url, whereTo=folder, fLOG=fLOG)
    for d in data:
        if d.endswith(".csv"):
            df = pandas.read_csv(d, sep=",", encoding="utf-8")
            return df
    raise DataNotAvailableError(
        "unable to find any csv file in '{0}'".format(file))


def elections_vote_places_geo(source="xd", folder=".", fLOG=noLOG):
    """
    retrieve data vote places (bureaux de vote in French)
    with geocodes

    @param      source  should be None unless you want to use the backup plan ("xd")
    @param      folder  where to download
    @param      fLOG    logging function
    @return             list of dataframe
    """
    if source is None:
        raise NotImplementedError("use source='xd'")
    else:
        url = source
        file = "bureauxvotegeo.zip"
    data = download_data(file, website=url, whereTo=folder, fLOG=fLOG)
    for d in data:
        if d.endswith(".txt"):
            df = pandas.read_csv(d, sep="\t", encoding="utf-8")
            return df
    raise DataNotAvailableError(
        "unable to find any csv file in '{0}'".format(file))


def villes_geo(folder=".", as_df=False, fLOG=noLOG):
    """
    retrieve data vote places (bureaux de vote in French)
    with geocodes

    @param      folder  where to download
    @param      as_df   return as a dataframe
    @param      fLOG    logging function
    @return             list of dataframe
    """
    this = os.path.abspath(os.path.dirname(__file__))
    data = os.path.join(this, "data_elections", "villesgeo.zip")
    geo = unzip_files(data, where_to=folder)
    if isinstance(geo, list):
        res = geo[0]
    else:
        res = geo
    if as_df:
        import pandas
        return pandas.read_csv(res, encoding="utf-8", sep="\t")
    else:
        return res


class _HTMLToText(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._buf = []
        self.hide_output = False

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br') and not self.hide_output:
            self._buf.append('\n')
        elif tag in ('script', 'style'):
            self.hide_output = True

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self._buf.append('\n')

    def handle_endtag(self, tag):
        if tag == 'p':
            self._buf.append('\n')
        elif tag in ('script', 'style'):
            self.hide_output = False

    def handle_data(self, text):
        if text and not self.hide_output:
            self._buf.append(re.sub(r'\s+', ' ', text))

    def handle_entityref(self, name):
        if name in name2codepoint and not self.hide_output:
            c = name2codepoint[name]
            self._buf.append(c)

    def handle_charref(self, name):
        if not self.hide_output:
            n = int(name[1:], 16) if name.startswith('x') else int(name)
            self._buf.append(n)

    def get_text(self):
        return re.sub(r' +', ' ', ''.join(self._buf))


def html_to_text(html):
    """
    Given a piece of HTML, return the plain text it contains.
    This handles entities and char refs, but not javascript and stylesheets.
    """
    parser = _HTMLToText()
    parser.feed(html)
    parser.close()
    return parser.get_text()


_elections_vote_place_address_patterns = [
    "bureau( de vote)?[- ]*n[^0-9]([0-9]{1,3})[- ]+(.*?)[- ]+([0-9]{5})[- ]+([-a-zéèàùâêîôûïöäëü']{2,40})[. ]"]


def elections_vote_place_address(folder=".", hide_warning=False, fLOG=noLOG):
    """
    this function scrapes and extracts addresses for every vote place (bureau de vote in French)

    @param      folder          where to download the scraped pages
    @param      hide_warnings   hide warnings
    @param      fLOG            logging function
    @return                     dictionary

    The function does not retrieve everything due to the irregular format.
    Sometimes, the city is missing or written above.
    """
    global _elections_vote_place_address_patterns
    files = []
    for deps in range(1, 96):
        last = "bureaudevote%02d.htm" % deps
        url = "http://bureaudevote.fr/"
        try:
            f = download_data(last, website=url, whereTo=folder, fLOG=fLOG)
        except (urllib.error.HTTPError, DownloadDataException):
            # backup plan
            files = download_data("bureauxdevote.zip",
                                  website="xd", whereTo=folder, fLOG=fLOG)
            break
        if isinstance(f, list):
            f = f[0]
        files.append(f)

    # extract data
    regex = [re.compile(_) for _ in _elections_vote_place_address_patterns]
    rows = []
    exc = []
    for data in files:
        lrows = []
        with open(data, "r", encoding="iso-8859-1") as f:
            content = f.read().lower()
        content = html_to_text(content)
        content0 = content
        content = content.replace("\n", " ").replace("\t", " ")
        atous = []
        for reg in regex:
            atous.extend(reg.findall(content))
        if len(atous) < 4 and len(atous) > 0:
            mes = "Not enough vote places ({2}) in\n{0}\nFOUND\n{3}\nCONTENT\n{1}".format(
                data, content0, len(atous), "\n".join(str(_) for _ in atous))
            exc.append(Exception(mes))
        if len(atous) > 1:
            for t in atous:
                ad = t[-3].split("-")
                address = ad[-1].strip(" ./<>-")
                place = "-".join(ad[:-1]).strip(" ./<>-")
                if "bureau de vote" in place:
                    if not hide_warning:
                        warnings.warn("Too long address {0}".format(t))
                else:
                    try:
                        lrows.append(dict(n=int(t[1]), city=t[-1].strip(" .<>/"),
                                          zip=t[-2], address=address,
                                          place=place))
                    except ValueError as e:
                        raise DataFormatException(
                            "issue with {0}".format(t)) from e
                    if len(lrows[-1]["city"]) <= 1:
                        mes = "No City in {0}\nROWS\n{2}\nCONTENT\n{1}".format(
                            t, content0, "\n".join(str(_) for _ in lrows))
                        raise DataFormatException(mes)
        if lrows:
            rows.extend(lrows)
        elif "06.htm" in data:
            mes = "Not enough vote places ({2}) in\n{0}\nFOUND\n{3}\nCONTENT\n{1}".format(
                data, content0, len(lrows), "\n".join(str(_) for _ in lrows))
            raise DataFormatException(mes)
    if len(exc) > 2:
        mes = "Exception raised: {0}\n---------\n{1}".format(
            len(exc), "\n########################\n".join(str(_) for _ in exc))
        raise DataFormatException(mes)
    return pandas.DataFrame(rows)
