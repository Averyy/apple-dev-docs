# CWNewLinkProfile

**Framework**: Application Services  
**Kind**: func

Creates a device link profile based on the specified set of profiles.

## Declaration

```c
CMError CWNewLinkProfile (
   CMProfileRef *prof,
   const CMProfileLocation *targetLocation,
   CMConcatProfileSet *profileSet
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

This discussion is accurate for versions of ColorSync prior to 2.5. See the version notes below for changes starting with version 2.5.

You can use this function to create a new single profile containing a set of profiles and pass the device link profile to the function [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) instead of specifying each profile in an array. A device link profile provides a means of storing in concatenated format a series of device profiles and non-device profiles that are used repeatedly in the same sequence.

The only way to use a device link profile is to pass it to the `CWConcatColorWorld` function as the sole profile specified by the array passed in the `profileSet` parameter.

The zero-based `keyIndex` field of the `CMConcatProfileSet` data structure specifies the index of the profile within the device link profile whose preferred CMM is used for the entire color-matching or color-checking session. The profile header’s `CMMType` field specifies the preferred CMM for the specified profile. This CMM will fetch the profile elements necessary for the session.

The quality flag setting—indicating normal mode, draft mode, or best mode—specified by the first profile prevails for the entire session the quality flags of profiles that follow in the sequence are ignored. The quality flag setting is stored in the `flag` field of the profile header. See [`CM2Header`](../cm2header.md) for more information on the use of flags.

The rendering intent specified by the first profile is used to color match to the second profile, the rendering intent specified by the second profile is used to color match to the third profile, and so on through the series of concatenated profiles. 

The following rules govern the content and use of a device link profile:

-  The first and last profiles you specify in the profiles array for a device link profile must be device profiles. 
-  You cannot specify a named color profile. 
-  You cannot include another device link profile in the series of profiles you specify in the profiles array. 
-  The only way to use a device link profile is to pass it to the `CWConcatColorWorld` function as the sole profile specified by the array passed in the `profileSet` parameter. 
-  You cannot embed a device link profile in an image. 
-  You cannot specify `NULL` to indicate the system profile. 

This function privately maintains all the profile information required by the color world for color-matching and color-checking sessions. Therefore, after executing the `CWNewLinkProfile` function, you should call the [CMCloseProfile](./api-1804861-cmcloseprofile.md) function for each profile used to build a device link profile (to dispose of each profile reference). 

##### Version-Notes

Note that starting with version 2.5, use of the system profile has changed.

## Parameters

- `prof`: A pointer to an uninitialized profile reference of type [`CMProfileRef`](../cmprofileref.md). On return, points to the new device link profile reference. 
- `targetLocation`: On return, a pointer to a location specification for the resulting profile. A device link profile cannot be a temporary profile: that is, it cannot have a location type of `cmNoProfileBase`. 
- `profileSet`: On input, a pointer to an array of profiles describing the processing to carry out. The array is in processing order—source through destination. For a description of the [`CMConcatProfileSet`](../cmconcatprofileset.md) data type, see `CMHeader`. 

## See Also

### Creating Profiles
- [CMNewProfile](./api-1804911-cmnewprofile.md)
  Creates a new profile and associated backing copy.
- [NCWNewLinkProfile](./api-1804918-ncwnewlinkprofile.md)
  Obtains a profile reference for the specified by the profile location.
- [CMMakeProfile](./api-1804920-cmmakeprofile.md)
  Makes a display or abstract profile by modifying an existing one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804915-cwnewlinkprofile)*