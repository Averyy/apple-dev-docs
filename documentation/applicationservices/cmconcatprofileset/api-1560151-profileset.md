# profileSet

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

A variable-length array of profile references. The references must be in processing order from source to destination. The rules governing the types of profiles you can specify in a profile array differ depending on whether you are creating a profile set for the function [CWConcatColorWorld](../colorsync_manager/api-1805087-cwconcatcolorworld.md) or for the function [CWNewLinkProfile](../colorsync_manager/api-1804915-cwnewlinkprofile.md). See the function descriptions for details. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
CMProfileRef profileSet[1];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmconcatprofileset/1560151-profileset)*