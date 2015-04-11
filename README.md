# wot-python-lib
Library for working with world of tanks resources.

## PackageReader
Allows you to extract file from wot packages without knowing in which package file actually is.
You can cache package index for faster use.

##### __init__(wot_path = None, cache_path = None)
    wot_path   - path to World of Tanks root directory
    cache_path - cache path or None to disable caching

##### setCache(cache_path)
    cache_path - cache path or None to disable caching
Cache path is used for storing package index and maybe more in future

##### setWotPath(wot_path)
    wot_path   - path to World of Tanks root directory

##### extract(package_file, result_file)
    package_file - path to file inside packages
    result_file  - where to should be file extracted
Extracts file from packages

##### open(package_file, mode)
    package_file - path to file inside packages
    mode         - mode to be opened in
Opens file inside package. Note this file will have limited functionality. Refer to the zipfile.open.

##### walk(path, recursive = False)
    path      - path to walk throught
    recursive - cycle all files inside path (only files directly inside path will be listed otherwise)
Will yeild paths to files inside path

## XmlUnpacker
Unpacks wot packed xml files

##### read(stream)
    stream - file handle to read data from
Returns xml.etree.ElementTree of root

## ModelReader
Enables you to read wot models

##### read(primitives_fh, visual_fh)
    primitives_fh - file handle of primitives file
    visual_fh     - file handle of associated visual file
Reads visual model. Returns Model

## Model
Contains data about wot model

##### getObjMtl(name_prefix="", v_index_start=0, normals=True, uv=True, materials=False):
    name_prefix   - prefix to be used in names
    v_index_start - from what vertice should export start
    normals       - export normals
    ui            - export uv
    materials     - include materials
Returns dict with obj and mtl contents ({obj: '..', mtl: '..'})

##### getObj(name_prefix="", v_index_start=0, normals=True, uv=True, materials=False):
    name_prefix   - prefix to be used in names
    v_index_start - from what vertice should export start
    normals       - export normals
    ui            - export uv
    materials     - include materials reference
Returns obj file contents

##### getMtl(name_prefix="")
    name_prefix - prefix to be used in names
Returns mtl file contents

##### getVericesCount()
Returns sum of vertices

## ModelGroup
Contains vertice group data

##### getFaces()
Returns list of object faces

##### getObj(name_prefix="group_", v_index_start=0, normals=True, uv=True, material=None)
    name_prefix   - prefix to be used in names
    v_index_start - from what vertice should export start
    normals       - export normals
    ui            - export uv
    material      - material name
Returns obj file contents

#### getMtl(name_prefix="material_")
    name_prefix - prefix to be used in names
Returns mtl file contents

