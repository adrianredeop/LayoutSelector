# -*- coding: utf-8 -*-
"""
QGIS Plugin Init File
"""

def classFactory(iface):
    """Load LayoutSelector class from file LayoutSelector"""
    from .LayoutSelector import LayoutSelector
    return LayoutSelector(iface)
