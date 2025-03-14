"""Test deployment of fusion-tools
"""

import os
import sys

from fusion_tools.fusion.vis import get_layout

def main():

    dsa_url = os.environ.get('DSA_URL')
    app_port = os.environ.get('APP_PORT')

    initial_items = [
        '6495a4e03e6ae3107da10dc5',
        '6495a4df3e6ae3107da10dc2'
    ] 

    args_dict = {
        'girderApiUrl': dsa_url,
        'user': None,
        'pword': None,
        'initialItems': initial_items,
        'app_options': {
            'host': '0.0.0.0',
            'port': int(app_port)
        }
    }

    fusion_vis = get_layout(args_dict)

    fusion_vis.start()

if __name__=='__main__':
    main()

