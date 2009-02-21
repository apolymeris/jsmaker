#!/usr/local/bin/python
# -*- coding: utf-8 -*-

CONFIG = { 
    "VARS" : {
        "version"    : "0.1",
        "authors"   : "Michał Łowicki"
    },
    "FILES" : [
        {
            "output"   : "output#1.js",
            "dirs"       : [
                "dir#1",
                "dir#2",
                "dir#3"
            ]
        },
        {
            "output"   : "output#2.js",
            "dirs"       : [
                "dir#4",
                "dir#5",
                "dir#6",
                "dir#7"
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