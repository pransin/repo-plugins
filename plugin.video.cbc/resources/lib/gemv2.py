"""Module for the V2 Gem API."""
import json

import requests

from resources.lib.cbc import CBC

LAYOUT_MAP = {
    'featured': 'https://services.radio-canada.ca/ott/cbc-api/v2/home',
    'shows': 'https://services.radio-canada.ca/ott/cbc-api/v2/hubs/shows',
    'documentaries': 'https://services.radio-canada.ca/ott/cbc-api/v2/hubs/documentaries',
    'kids': 'https://services.radio-canada.ca/ott/cbc-api/v2/hubs/kids'
}
SHOW_BY_ID = 'https://services.radio-canada.ca/ott/cbc-api/v2/shows/{}'
CATEGORY_BY_ID = 'https://services.radio-canada.ca/ott/cbc-api/v2/categories/{}'


class GemV2:
    """V2 Gem API class."""

    @staticmethod
    def get_layout(name):
        """Get a Gem V2 layout by name."""
        url = LAYOUT_MAP[name]
        resp = CBC.get_session().get(url)
        return json.loads(resp.content)

    @staticmethod
    def get_show_layout_by_id(show_id):
        """Get a Gem V2 show layout by ID."""
        url = SHOW_BY_ID.format(show_id)
        resp = CBC.get_session().get(url)
        return json.loads(resp.content)

    @staticmethod
    def get_episode(url):
        """Get a Gem V2 episode by URL."""
        # resp = CBC.get_session().get(url)
        resp = requests.get(url)
        return json.loads(resp.content)

    @staticmethod
    def get_category(category_id):
        """Get a Gem V2 category by ID."""
        url = CATEGORY_BY_ID.format(category_id)
        resp = CBC.get_session().get(url)
        return json.loads(resp.content)

    @staticmethod
    def get_labels(show, episode):
        """Get labels for a show."""
        labels = {
            'studio': 'Canadian Broadcasting Corporation',
            'country': 'Canada',
            'tvshowtitle': episode['title'],
            'title': show['title'],
            'plot': episode['description'],
            'plotoutline': episode['description'],
            'season': episode['season'],
            'episode': episode['episode']
        }
        return labels