# kCMMUnflattenProfile

**Framework**: Application Services  
**Kind**: econst

## Overview

In response to this request code, your CMM must create a temporary file in which to store the profile data you receive from the low-level data-transfer function supplied by the calling application or driver. Your function must return the file specification.

Changed in ColorSync 2.5: Starting with ColorSync version 2.5, the ColorSync Manager calls the function provided by the calling program directly, without going through the preferred, or any, CMM. Your CMM only needs to handle this request code for versions of ColorSync prior to version 2.5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmm_function_selectors/kcmmunflattenprofile)*