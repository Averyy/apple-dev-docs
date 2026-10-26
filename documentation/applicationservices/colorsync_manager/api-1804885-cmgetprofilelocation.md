# CMGetProfileLocation

**Framework**: Application Services  
**Kind**: func

Obtains the location of a profile based on the specified profile reference.

## Declaration

```c
CMError CMGetProfileLocation (
   CMProfileRef prof,
   CMProfileLocation *location
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

When your application calls the `CMValidateProfile` function, the ColorSync Manager dispatches the function to the CMM specified by the `CMMType` header field of the profile whose reference you specify. The preferred CMM can support this function or not.

To open a profile and obtain a reference to it, use the function [CMOpenProfile](./api-1804853-cmopenprofile.md). 

##### Version-Notes

This function is not recommended for use in ColorSync 2.5.

Starting with ColorSync version 2.5, you should use the function [NCMGetProfileLocation](./api-1804889-ncmgetprofilelocation.md) instead of `CMGetProfileLocation`.

As of version 2.5, if you call `CMGetProfileLocation`, it will just call `NCMGetProfileLocation` in turn, passing the profile specified by `prof`, the profile location specified by `theProfile`, and a location size value of `cmOriginalProfileLocationSize`.

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md). Before calling `CMGetProfileLocation`, you set the reference to specify the profile you wish to obtain the location for. 
- `theProfile`: A pointer to a profile location structure of type [`CMProfileLocation`](../cmprofilelocation.md). On return, specifies the location of the profile. Commonly, a profile is disk-file based, but it may instead be temporary, handle-based, pointer-based, or accessed through a procedure supplied by your application. 

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
- [CMGetProfileHeader](./api-1804879-cmgetprofileheader.md)
  Obtains the profile header for the specified profile. 
- [CMSetProfileHeader](./api-1804882-cmsetprofileheader.md)
  Sets the header for the specified profile. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804885-cmgetprofilelocation)*