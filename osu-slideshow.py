# Downloads all osu seasonal backgrounds into a directory.
import argparse
import os
from urllib.parse import urlparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
parser.add_argument("--remove-old", action='store_true')
args = parser.parse_args()

print(args)
if not os.path.isdir(args.path):
    raise Exception('Path is not a directory')

if args.remove_old:
    print("Cleanup...")
    files = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
    for file in files:
        os.remove(os.path.join(args.path, file))

response = requests.get("https://osu.ppy.sh/api/v2/seasonal-backgrounds").json()
backgrounds = [background['url'] for background in response['backgrounds']]
print('Resolved backgrounds: ', backgrounds)
for background in backgrounds:
    filename = os.path.basename(urlparse(background).path)
    with open(os.path.join(args.path, filename), 'wb') as file:
        file.write(requests.get(background).content)