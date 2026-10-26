# kCMMInit

**Framework**: Application Services  
**Kind**: econst

#### Overview

This request code is provided for backward compatibility with ColorSync 1.0. A CMM that supports ColorSync 1.0 profiles should respond to this request code by initializing any private data required for the color-matching or gamut-checking session to be held as indicated by subsequent request codes.         If your CMM supports only ColorSync 1.0 profiles or both ColorSync 1.0 profiles and ColorSync Manager version 2.x profiles, you must support this request code. If you support only ColorSync Manager version 2.x profiles, you should return an unimplemented error in response to this request code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmm_function_selectors/kcmminit)*