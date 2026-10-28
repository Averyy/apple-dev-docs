# CMCopyProfile

**Framework**: Application Services  
**Kind**: func

Duplicates the specified existing profile.

## Declaration

```c
CMError CMCopyProfile (
   CMProfileRef *targetProf,
   const CMProfileLocation *targetLocation,
   CMProfileRef srcProf
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CMCopyProfile` function duplicates an entire open profile whose reference you specify. If you have made temporary changes to the profile, which you have not saved by calling `CMUpdateProfile`, those changes are included in the duplicated profile. They are not saved to the original profile unless you call `CMUpdateProfile` for that profile.

The ColorSync Manager maintains a modified flag to track whether a profile has been modified. After copying a profile, the `CMCopyProfile` function sets the value of the modified flag for that profile to `false`.

Unless you are copying a profile that you created, you should not infringe on copyright protection specified by the profile creator. To obtain the copyright information, you call the function [CMGetProfileElement](./api-1804973-cmgetprofileelement.md), specifying the `cmCopyrightTag` tag signature for the copyright element (defined in the `CMICCProfile.h` header file).

You should also check the `flags` field of the profile header structure [`CM2Header`](../cm2header.md) for copyright information. You can test the `cmEmbeddedUseMask` bit of the flags field to determine whether the profile can be used independently. If the bit is set, you should use this profile as an embedded profile only and not copy the profile for your own purposes. The `cmEmbeddedUseMask` mask is described in [Flag Mask Definitions for Version 2.x Profiles](../api-1560699-x_profiles.md). The following code snippet shows how you might perform a test using the `cmEmbeddedUseMask` mask:

```occ
if (myCM2Header.flags & cmEmbeddedUseMask)
{
// profile should only be used as an embedded profile
}
else
{
// profile can be used independently
}
```

A calibration program, for example, might use the `CMCopyProfile` function to copy a device’s original profile, then modify the copy to reflect the current state of the device. Or an application might want to copy a profile after unflattening it.

To copy a profile, you must obtain a reference to that profile by either opening the profile or creating it. To open a profile, use the function [CMOpenProfile](./api-1804853-cmopenprofile.md). To create a new profile, use the function [CMNewProfile](./api-1804911-cmnewprofile.md). As an alternative to using the `CMCopyProfile` function to duplicate an entire profile, you can use the same profile reference more than once. To do so, you call the function [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md) to increment the reference count for the reference each time you reuse it. Calling the `CMCloneProfileRef` function increments the count; calling the function [CMCloseProfile](./api-1804861-cmcloseprofile.md) decrements it. The profile remains open as long as the reference count is greater than 0, indicating at least one routine retains a reference to the profile. 

## Parameters

- `targetProf`: A pointer to a profile reference of type [`CMProfileRef`](../cmprofileref.md). On return, points to the profile copy that was created. 
- `targetLocation`: A pointer to a location specification that indicates the location, such as in memory or on disk, where the ColorSync Manager is to create the copy of the profile. A profile is commonly disk-file based. However, to accommodate special requirements, you can create a handle- or pointer-based profile, you can create a profile that is accessed through a procedure provided by your application, or you can create a temporary profile that is not saved after you call the `CMCloseProfile` function. To create a temporary profile, you either specify `cmNoProfileBase` as the kind of profile in the profile location structure or specify `NULL` for this parameter. To specify the location, you use the data type [`CMProfileLocation`](../cmprofilelocation.md). 
- `srcProf`: A profile reference to the profile to duplicate.

## See Also

### Accessing Profiles
- [CMOpenProfile](./api-1804853-cmopenprofile.md)
  Opens the specified profile and returns a reference to the profile.
- [CMValidateProfile](./api-1804856-cmvalidateprofile.md)
  Indicates whether the specified profile contains the minimum set of elements required by the current color management module (CMM) for color matching or color checking.
- [CMCloseProfile](./api-1804861-cmcloseprofile.md)
  Decrements the reference count for the specified profile reference and, if the reference count reaches 0, frees all private memory and other resources associated with the profile.
- [CMUpdateProfile](./api-1804864-cmupdateprofile.md)
  Saves modifications to the specified profile.
- [CMProfileModified](./api-1804872-cmprofilemodified.md)
  Indicates whether the specified profile has been modified since it was created or last updated.
- [CMGetProfileMD5](./api-1804876-cmgetprofilemd5.md)
  Gets the MD5 checksum from the profile header (message digest)
- [CMGetProfileHeader](./api-1804879-cmgetprofileheader.md)
  Obtains the profile header for the specified profile. 
- [CMSetProfileHeader](./api-1804882-cmsetprofileheader.md)
  Sets the header for the specified profile. 
- [CMGetProfileLocation](./api-1804885-cmgetprofilelocation.md)
  Obtains the location of a profile based on the specified profile reference.
- [NCMGetProfileLocation](./api-1804889-ncmgetprofilelocation.md)
  Obtains either a profile location structure for a specified profile or the size of the location structure for the profile.
- [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md)
  Increments the reference count for the specified profile reference.
- [CMGetProfileRefCount](./api-1804894-cmgetprofilerefcount.md)
  Obtains the current reference count for the specified profile.
- [CMFlattenProfile](./api-1804897-cmflattenprofile.md)
  Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804870-cmcopyprofile)*