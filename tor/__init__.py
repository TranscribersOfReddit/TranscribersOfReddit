import os

__version__ = '3.11.0'
__SELF_NAME__ = 'transcribersofreddit'
__BOT_NAMES__ = os.environ.get('BOT_NAMES', 'transcribersofreddit,tor_archivist,transcribot').split(',')
__root__ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
__friendly_name__ = 'u/ToR'
