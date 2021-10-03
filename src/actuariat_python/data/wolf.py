# -*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about population
"""
import os
import re
from pyquickhelper.loghelper import noLOG
from pymyinstall.installcustom import download_page
from pyensae.datasource import download_data
from pyensae.datasource.http_retrieve import DownloadDataException
from pyrsslocal.xmlhelper import xml_filter_iterator
from .data_exceptions import LinkNotFoundError


def wolf_xml(url="http://pauillac.inria.fr/~sagot/index.html", temp_folder=".", fLOG=noLOG):
    """
    The `WOLF <http://alpage.inria.fr/~sagot/wolf-en.html>`_
    (Wordnet Libre du Français, Free French Wordnet) is a free semantic
    lexical resource (wordnet) for French.

    This data is licensed under `Cecill-C license
    <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>`_.
    Language is French.

    @param      url             url
    @param      fLOG            logging function
    @param      temp_folder     where to download
    @return                     list of files
    """
    link = url
    page = download_page(link)
    reg = re.compile("href=\\\"(https.*?wolf.*?[.]bz2)\\\"")
    alls = reg.findall(page)
    if len(alls) == 0:
        raise LinkNotFoundError(  # pragma: no cover
            "unable to find a link on a .bz2 file on page\n{}".format(page))

    url = alls[0]
    spl = url.split("/")
    url = "/".join(spl[:-1]) + "/"
    url2 = "/".join(spl[:-2]) + "/31718/"
    try:
        dtd = download_data("debvisdic-strict.dtd", url=[url2, "xd"],
                            fLOG=fLOG, whereTo=temp_folder)
    except DownloadDataException:
        dtd = None
    name = spl[-1].strip('.')

    try:
        local = download_data(
            name, url=[url, "xd"], fLOG=fLOG, whereTo=temp_folder)
    except DownloadDataException:
        local = None
    if local is not None and isinstance(local, str):
        local = [local]
    # We check the file was downloaded.
    expected = os.path.join(temp_folder, "wolf-1.0b4.xml")
    if local is None or not os.path.exists(expected):  # pragma: no cover
        res = download_data("wolf-1.0b4.xml.zip",
                            whereTo=temp_folder, fLOG=fLOG)
        if not os.path.exists(expected):
            raise FileNotFoundError(expected)
        return res
    elif isinstance(dtd, list):
        return local + dtd
    return local + [dtd]  # pragma: no cover


def enumerate_wolf_xml_row(filename, fLOG=noLOG, xmlformat=False, encoding="utf-8", errors=None):
    """
    walk through an XML file returned by function
    @see fn wolf_xml

    @param      filename        filename
    @param      fLOG            logging function
    @param      xmlformat       if True, return the xml, otherwise return the node,
                                see `XMLHandlerDictNode <http://www.xavierdupre.fr/app/pyrsslocal/
                                helpsphinx/pyrsslocal/xmlhelper/xml_tree_node.html#
                                module-pyrsslocal.xmlhelper.xml_tree_node>`_
    @param      encoding        encoding
    @param      errors          what to do with errors
    @return                     elements
    """
    for row in xml_filter_iterator(filename, xmlformat=xmlformat, fLOG=fLOG, encoding=encoding, errors=errors):
        yield row


def enumerate_wolf_synonyms(filename, fLOG=noLOG, encoding="utf-8", errors=None):
    """
    enumerate list of synonyms
    Language is French.

    @param      filename        xml file
    @param      fLOG            logging function
    @param      encoding        encoding
    @param      errors          what to do with errors
    @return                     iterator on list of words
    """
    for row in enumerate_wolf_xml_row(
            filename, fLOG=fLOG, encoding=encoding, errors=errors):
        syn = [v for k, v in row.iterfields() if k == "SYNSET/SYNONYM/LITERAL/_"]
        if len(syn) > 1:
            yield syn
