import os
fixtures_path = os.path.join(os.path.split(__file__)[0],r'..\furnace\fixtures')

for root, dirs, files in os.walk(fixtures_path):
    for file in files:
        if file.endswith('.html'):
            pass

# iterate all the subfolders of the fixtures
