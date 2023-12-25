#  Copyright: Copyright (c) 2020., Adam Jakab
#
#  Author: Adam Jakab <adam at jakab dot pro>
#  Created: 3/13/20, 12:17 AM
#  License: See LICENSE.txt

import os

from beets.plugins import BeetsPlugin
from beets.dbcore import types
from confuse import ConfigSource, load_yaml
from beetsplug.xtractor.command import XtractorCommand


class XtractorPlugin(BeetsPlugin):
    _default_plugin_config_file_name_ = 'config_default.yml'
    item_types = {
        'average_loudness': types.Float(12),
        'beats_count': types.INTEGER,
        # 'chords_changes_rate': types.Float(12),
        # 'chords_key': types.STRING,
        # 'chords_number_rate': types.Float(12),
        # 'chords_scale': types.STRING,
        # 'key_strength': types.Float(12),
        'danceable': types.Float(12),
        'danceability': types.Float(12),
        'gender': types.STRING,
        'is_male': types.Float(12),
        'is_female': types.Float(12),
        'genre_rosamerica': types.STRING,
        'mood_acoustic': types.Float(12),
        'mood_aggressive': types.Float(12),
        'mood_electronic': types.Float(12),
        'mood_happy': types.Float(12),
        'mood_party': types.Float(12),
        'mood_relaxed': types.Float(12),
        'mood_sad': types.Float(12),
        'mood_mirex': types.STRING,
        'mood_mirex_cluster_1': types.Float(12),
        'mood_mirex_cluster_2': types.Float(12),
        'mood_mirex_cluster_3': types.Float(12),
        'mood_mirex_cluster_4': types.Float(12),
        'mood_mirex_cluster_5': types.Float(12),
        # 'rhythm': types.Float(12),
        # 'timbre': types.STRING,
        # 'tonal': types.Float(12),
        'voice_instrumental': types.STRING,
        'is_instrumental': types.Float(12),
        'is_voice': types.Float(12),
        'genre_rosamerica_cla': types.Float(12),
        'genre_rosamerica_dan': types.Float(12),
        'genre_rosamerica_hip': types.Float(12),
        'genre_rosamerica_jaz': types.Float(12),
        'genre_rosamerica_pop': types.Float(12),
        'genre_rosamerica_rhy': types.Float(12),
        'genre_rosamerica_spe': types.Float(12),                                                
    }

    def __init__(self):
        super(XtractorPlugin, self).__init__()
        config_file_path = os.path.join(os.path.dirname(__file__), self._default_plugin_config_file_name_)
        source = ConfigSource(load_yaml(config_file_path) or {}, config_file_path)
        self.config.add(source)

        # @todo: activate this to store the attributes in media files
        # field = mediafile.MediaField(
        #     mediafile.MP3DescStorageStyle(u'danceability'), mediafile.StorageStyle(u'danceability')
        # )
        # self.add_media_field('danceability', field)
        #
        # field = mediafile.MediaField(
        #     mediafile.MP3DescStorageStyle(u'beats_count'), mediafile.StorageStyle(u'beats_count')
        # )
        # self.add_media_field('beats_count', field)

    def commands(self):
        return [XtractorCommand(self.config)]
