#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# replace_module_test.py
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

# Built-in/Generic Imports
from codegenlib.templateStreaming import TemplateStreaming
from codegenlib.templateFile import TemplateFile
from codegenlib.templateModule import TemplateModule

activity_name = "ListActivity"
package_name = "com.myapp"
adapter_name = "ListAdapter"
list_activity_layout_xml = "list_activity_layout"
list_item_layout_xml = "list_item_layout"
kotlin_extension = ".kt"
xml_extension = ".xml"

activity_TF = TemplateFile(
    name = "list_activity_mustache",
    dict = {"package_name": "com.myapp", "activity_name" : activity_name , "list_activity_layout_xml_name" : list_activity_layout_xml},
    output_file = activity_name + kotlin_extension
)
list_activit_layout_xml_TF = TemplateFile(
    name = "list_activity_layout_xml_mustache",
    dict = {"activity_name" : activity_name },
    output_file = list_activity_layout_xml + xml_extension
)
list_adapter_TF = TemplateFile(
    name = "list_adapter_mustache",
    dict = {"adapter_name" : adapter_name , "package_name" : package_name , "list_item_xml_name" : list_item_layout_xml},
    output_file = adapter_name + kotlin_extension
)
list_item_layout_xml_TF = TemplateFile(
    name = "list_item_xml_mustache",
    dict = {},
    output_file = list_item_layout_xml + xml_extension
)

# should be name property in root modules folder
# all mustache files belonging to for this module
#modules/android-kotlin-list
listModule = TemplateModule(
    # module name, same time folder name
    name="android-kotlin-list",
    # All files belonging to this module can be defined under this property.
    mustache_folder = "modules",
    # All files to generate can  use array
    templates_files = [activity_TF, list_activit_layout_xml_TF, list_adapter_TF, list_item_layout_xml_TF]
)
# output folder of generated files
listModule.outputDirectory = "output"
# all files always append on over written
listModule.isAppendOutputPath = True

tStreaming = TemplateStreaming(
    template_module = listModule
)
# the run command
tStreaming.execute()
