# kCMMMatchPixMap

**Framework**: Application Services  
**Kind**: econst

#### Overview

In response to this request code, your CMM must match the colors of the pixel map image pointed to by the `myPixMap` parameter to the gamut of the destination device, replacing the original pixel colors with their corresponding colors as specified in the data color space of the destination device’s color gamut. To perform the matching, you use the profiles specified by a previous `kNCMMInit`, `kCMMInit`, or `kCMMConcatInit `request to your CMM. For more information, see the function [CWMatchPixMap](../api-1805211-cwmatchpixmap.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmm_function_selectors/kcmmmatchpixmap)*