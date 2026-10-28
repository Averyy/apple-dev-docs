# CMGetProfileHeader

**Framework**: Application Services  
**Kind**: func

Obtains the profile header for the specified profile. 

## Declaration

```c
CMError CMGetProfileHeader (
   CMProfileRef prof,
   CMAppleProfileHeader *header
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CMGetProfileHeader` function returns the header for a ColorSync 2.x or ColorSync 1.0 profile. To return the header, the function uses a union of type [`CMAppleProfileHeader`](../api-1560290-cmappleprofileheader.md), with variants for version 1.0 and 2.x headers. 

A 32-bit version value is located at the same offset in either header. For ColorSync 2.x profiles, this is the `profileVersion` field. For ColorSync 1.0 profiles, this is the `applProfileVersion` field. You can inspect the value at this offset to determine the profile version, and interpret the remaining header fields accordingly.

To copy a profile header to a profile after you modify the header’s contents, use the function [CMSetProfileHeader](./api-1804882-cmsetprofileheader.md). 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile whose header is to be copied. 
- `header`: A pointer to a profile header. On input, depending on the profile version, you may allocate a ColorSync 2.x or 1.0 header. On return, contains the profile data. For information about the ColorSync 2.x profile header structure, see [`CM2Header`](../cm2header.md). For information about the ColorSync 1.0 header, see `CMHeader`. 

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
- [CMCopyProfile](./api-1804870-cmcopyprofile.md)
  Duplicates the specified existing profile.
- [CMProfileModified](./api-1804872-cmprofilemodified.md)
  Indicates whether the specified profile has been modified since it was created or last updated.
- [CMGetProfileMD5](./api-1804876-cmgetprofilemd5.md)
  Gets the MD5 checksum from the profile header (message digest)
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804879-cmgetprofileheader)*