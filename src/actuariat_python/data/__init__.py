"""
@file
@brief shortcuts to data
"""

from .data_exceptions import DataFormatException
from .elections import elections_presidentielles, elections_presidentielles_local_files, elections_legislatives_bureau_vote
from .elections import elections_legislatives_circonscription_geo, elections_vote_place_address, elections_vote_places_geo
from .geocoding import geocode
from .population import population_france_2015, table_mortalite_france_00_02, fecondite_france, table_mortalite_euro_stat
from .wolf import wolf_xml, enumerate_wolf_xml_row, enumerate_wolf_synonyms
