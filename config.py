#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#
# basic configuration
#

CONFIG = { 
    "VARS" : {
        "version"    : "0.1",
        "authors"   : "Michał Łowicki"
    },
    "MODULES" : [
        {
            "output"   : "build/output#1.js",
            "dirs"       : [
                "js/js#1",
                "js/js#2"
            ]
        },
        {
            "output"   : "build/output#2.js",
            "dirs"       : [
                "js/js#3"
            ]
        }
    ],
    "DEBUG" : {
    
    },
    "RELEASE" : {
        "methods": [
            "console.debug",
            "console.log",
            "opera.postError"
        ]
    }
}