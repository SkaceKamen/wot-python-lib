# wot-python-lib
Library for working with world of tanks resources.

## Credits
Thanks Coffee_ for doing most of the hard work. I just rewritten his scripts to python.

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
Reads visual model. Returns Primitive

## Primitive
Contains data about wot model. Refer to ModelWriter for more informations

##### RenderSet[] renderSets
Contains render sets, which then contains primitive groups.

##### float[[],[]] boundingBox
Contains model bounding box in following format [[min_x, min_y, min_z], [max_x, max_y, max_z]]

##### dict nodes
Contains nodes and their transforms. Those nodes are used for positions of stuff... not for model

## RenderSet
Contains data about one render set

##### string[] nodes
Nodes used in this render set. Purpose unknown.

##### PrimitiveGroup[] groups
Contains primitive groups data

## PrimitiveGroup
Contains raw group data

##### float[] origin

##### Material material
Group material

##### Vertice[] vertices
Group vertices

##### int[] indices
Group indices, 3 indices = one triangle

## OBJModelWriter

##### write(primitive, filename, filename_material=None)
Exports primitive to OBJ (and mtl if set)

##### bool material
export material

##### bool normals
export normals
##### bool uv
export uv
##### bool compress
compress result obj and mtl using zlib

##### string textureBase
textures root used in mlt

##### callable textureCallback
Receives params: (texture_path, texture_type). Returns new texture_path used in mtl. This callback overrides the textureBase prop
