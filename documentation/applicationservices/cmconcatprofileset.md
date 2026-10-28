# CMConcatProfileSet

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains profile and other information needed to set up a color world.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMConcatProfileSet {
    ...
} CMConcatProfileSet;
```

## Overview

You can call the function [NCWNewColorWorld](./colorsync_manager/api-1805079-ncwnewcolorworld.md) to create a color world for operations such as color matching and color conversion. A color world is normally based on two profiles—source and destination. But it can include a series of profiles that describe the processing for a work-flow sequence, such as scanning, printing, and previewing an image. To create a color world that includes a series of profiles, you use the function [CWConcatColorWorld](./colorsync_manager/api-1805087-cwconcatcolorworld.md).

The array specified in the `profileSet` field identifies a concatenated profile set your application can use to establish a color world in which the sequential relationship among the profiles exists until your application disposes of the color world. Alternatively, you can create a device link profile composed of a series of linked profiles that remains intact and available for use again after your application disposes of the concatenated color world. In either case, you use a data structure of type `CMConcatProfileSet` to define the profile set. 

A device link profile accommodates users who use a specific configuration requiring a combination of device profiles and possibly non-device profiles repeatedly over time.

To set up a color world that includes a concatenated set of profiles, your application uses the function [CWConcatColorWorld](./colorsync_manager/api-1805087-cwconcatcolorworld.md) , passing it a structure of type `CMConcatProfileSet.` The array you pass may contain a set of profile references or it may contain only the profile reference of a device link profile. To create a device link profile, your application calls the function [CWNewLinkProfile](./colorsync_manager/api-1804915-cwnewlinkprofile.md), passing a structure of type `CMConcatProfileSet`. 

## Topics

### Instance Properties
- [count](./cmconcatprofileset/api-1560649-count.md)
  The one-based count of profiles in the profile array. A minimum of one profile is required.
- [keyIndex](./cmconcatprofileset/api-1560608-keyindex.md)
  A zero-based index into the array of profile references identifying the profile whose CMM is used for the entire session. The profile’s `CMMType` field identifies the CMM.
- [profileSet](./cmconcatprofileset/api-1560151-profileset.md)
  A variable-length array of profile references. The references must be in processing order from source to destination. The rules governing the types of profiles you can specify in a profile array differ depending on whether you are creating a profile set for the function [CWConcatColorWorld](./colorsync_manager/api-1805087-cwconcatcolorworld.md) or for the function [CWNewLinkProfile](./colorsync_manager/api-1804915-cwnewlinkprofile.md). See the function descriptions for details. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmconcatprofileset)*