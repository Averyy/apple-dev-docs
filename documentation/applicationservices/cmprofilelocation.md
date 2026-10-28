# CMProfileLocation

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains profile location information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMProfileLocation {
    ...
} CMProfileLocation;
```

## Overview

Your application passes a profile location structure of type `CMProfileLocation` when it calls:

-  the function [CMOpenProfile](./colorsync_manager/api-1804853-cmopenprofile.md), specifying the location of a profile to open 
-  the [CMNewProfile](./colorsync_manager/api-1804911-cmnewprofile.md), [CWNewLinkProfile](./colorsync_manager/api-1804915-cwnewlinkprofile.md), or [CMCopyProfile](./colorsync_manager/api-1804870-cmcopyprofile.md) functions, specifying the location of a profile to create or duplicate 

## Topics

### Instance Properties
- [locType](./cmprofilelocation/api-1560341-loctype.md)
  The type of data structure that the `u` field’s `CMProfLoc` union holds—a file specification, a handle, a pointer, or a universal procedure pointer. To specify the type, you use the constants defined in the enumeration described in [Profile Location Type](./api-1560599-profile_location_type.md).
- [u](./cmprofilelocation/api-1560083-u.md)
  A union of type [`CMProfLoc`](./api-1560460-cmprofloc.md) identifying the profile location. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmprofilelocation)*