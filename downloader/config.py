files = ["http://data.discogs.com.s3-us-west-2.amazonaws.com/data/discogs_20160101_releases.xml.gz",
         "http://data.discogs.com.s3-us-west-2.amazonaws.com/data/discogs_20160201_releases.xml.gz",
         "http://data.discogs.com.s3-us-west-2.amazonaws.com/data/discogs_20160301_releases.xml.gz",
         "http://data.discogs.com.s3-us-west-2.amazonaws.com/data/discogs_20160401_releases.xml.gz",
         "http://data.discogs.com.s3-us-west-2.amazonaws.com/data/discogs_20160501_releases.xml.gz"
 ]

working_dir = "wd/"


# Loading site-specific override settings
import os
extra_settings_path = os.getenv('DISCO_SETTINGS_PATH')
if extra_settings_path is not None:
    try:
        print('Loading user-specified settings from %s' % extra_settings_path)
    except IOError:
        pass
    import imp
    extra_settings_module = imp.load_source('extra_settings', extra_settings_path)
    globals().update(dict([(key, value) for key, value in extra_settings_module.__dict__.items() if not key.startswith('__')]))

