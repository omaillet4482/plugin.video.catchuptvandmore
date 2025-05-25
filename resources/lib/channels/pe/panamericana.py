# -*- coding: utf-8 -*-
# Copyright: (c) 2022, joaopa
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
import json

# noinspection PyUnresolvedReferences
from codequick import Resolver
import urlquick

from resources.lib import resolver_proxy, web_utils

# TODO
# Add Replay

URL_API = "https://kick.com/api/v2/channels/ptv5/livestream"


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):
    headers = {
        "User-Agent": web_utils.get_random_ua(),
        'Referer': 'https://player.kick.com/'
    }
    resp = urlquick.get(URL_API, headers=headers, max_age=-1)
    video_url = json.loads(resp.text)['data']['playback_url']

    return resolver_proxy.get_stream_with_quality(plugin, video_url)
