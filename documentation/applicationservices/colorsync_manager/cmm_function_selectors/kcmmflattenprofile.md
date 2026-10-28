# kCMMFlattenProfile

**Framework**: Application Services  
**Kind**: econst

## Overview

In response to this request code, your CMM must extract the profile data from the profile to flatten, identified by the `prof` parameter, and pass the profile data to the function specified in the `proc` parameter. For more information, see the function [CMFlattenProfile](../api-1804897-cmflattenprofile.md). 

Changed in ColorSync 2.5: Starting with ColorSync version 2.5, the ColorSync Manager calls the function provided by the calling program directly, without going through the preferred, or any, CMM. Your CMM only needs to handle this request code for versions of ColorSync prior to version 2.5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmm_function_selectors/kcmmflattenprofile)*