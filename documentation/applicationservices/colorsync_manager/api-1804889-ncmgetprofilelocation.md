# NCMGetProfileLocation

**Framework**: Application Services  
**Kind**: func

Obtains either a profile location structure for a specified profile or the size of the location structure for the profile.

## Declaration

```c
CMError NCMGetProfileLocation (
   CMProfileRef prof,
   CMProfileLocation *theProfile,
   UInt32 *locationSize
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `NCMGetProfileLocation` function is available starting with ColorSync version 2.5. It differs from its predecessor, [CMGetProfileLocation](./api-1804885-cmgetprofilelocation.md), in that the newer version has a parameter for the size of the location structure for the specified profile.

You should use `NCMGetProfileLocation` rather than `CMGetProfileLocation` for the following reasons:

-  Code using the older version (`CMGetProfileLocation`) may not be as easily ported to other platforms. 
-  Specifying the size of the profile location structure ensures that it can grow, if necessary, in the future. 

The best way to use `NCMGetProfileLocation` is to call it twice:

1.  Pass a reference to the profile to locate in the `prof` parameter and `NULL` for the `profLoc` parameter. `NCMGetProfileLocation` returns the size of the location structure in the `locationSize` parameter. 
2.  Allocate enough space for a structure of the returned size, then call the function again, passing a pointer in the `profLoc` parameter; on return, the structure specifies the location of the profile. 

It is possible to call `NCMGetProfileLocation` just once, using the constant `cmCurrentProfileLocationSize` for the size of the allocated profile location structure and passing the same constant for the `locationSize` parameter. The constant `cmCurrentProfileLocationSize` may change in the future, but will be consistent within the set of headers you build your application with. However, if the size of the `CMProfileLocation` structure changes in a future version of ColorSync (and the value of `cmCurrentProfileLocationSize` as well) and you do not rebuild your application, `NCMGetProfileLocation` may return an error. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md). Before calling `NCMGetProfileLocation`, you set the reference to specify the profile for which you wish to obtain the location or location structure size. 
- `theProfile`: A pointer to a profile location structure, as described in [`CMProfileLocation`](../cmprofilelocation.md). If you pass `NULL`, `NCMGetProfileLocation` returns the size of the profile location structure for the profile specified by `prof` in the `locationSize` parameter. If you instead pass a pointer to memory you have allocated for the structure, on return, the structure specifies the location of the profile specified by `prof`. 
- `locationSize`: A pointer to a value of type `long`. If you pass `NULL` for the `profLoc` parameter, on return, `locationSize` contains the size in bytes of the profile location structure for the profile specified by `prof`. If you pass a pointer to a profile location structure in `profLoc`, set `locationSize` to the size of the structure before calling `NCMGetProfileLocation`, using the constant `cmCurrentProfileLocationSize`. 

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
- [CMGetProfileLocation](./api-1804885-cmgetprofilelocation.md)
  Obtains the location of a profile based on the specified profile reference.
- [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md)
  Increments the reference count for the specified profile reference.
- [CMGetProfileRefCount](./api-1804894-cmgetprofilerefcount.md)
  Obtains the current reference count for the specified profile.
- [CMFlattenProfile](./api-1804897-cmflattenprofile.md)
  Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804889-ncmgetprofilelocation)*