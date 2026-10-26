# CMFlattenProfile

**Framework**: Application Services  
**Kind**: func

Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.

## Declaration

```c
CMError CMFlattenProfile (
   CMProfileRef prof,
   UInt32 flags,
   CMFlattenUPP proc,
   void *refCon,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The ColorSync Manager passes to the CMM the pointer to your profile-flattening function. The CMM calls your function [`CMFlattenProcPtr`](../cmflattenprocptr.md) to perform the actual data transfer.

To unflatten a profile embedded in a graphics document to an independent disk file, use the function “Accessing Profile Elements”. 

##### Version-Notes

Prior to version 2.5, the ColorSync Manager dispatches the `CMFlattenProfile` function to the CMM specified by the profile whose reference you provide. If the preferred CMM is unavailable or it does not support this function, then the default CMM is used.

Starting with ColorSync version 2.5, the ColorSync Manager calls your transfer function directly, without going through the preferred, or any, CMM. As a result, the value returned in the `preferredCMMnotfound` parameter is guaranteed to be `false`.

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile to flatten. 
- `flags`: Reserved for future use. 
- `proc`: A pointer to a function that you provide to perform the low-level data transfer. For more information, see the function [`CMFlattenProcPtr`](../cmflattenprocptr.md). 
- `refCon`: A pointer to a reference constant for application data which the color management module (CMM) passes to the `CMFlattenProcPtr` function each time it calls the function. For example, the reference constant may point to a data structure that holds information required by the `CMFlattenProcPtr` function to perform the data transfer, such as the reference number to a disk file in which the flattened profile is to be stored.

  Starting with ColorSync version 2.5, the ColorSync Manager calls your transfer function directly, without going through the preferred, or any, CMM.
- `preferredCMMnotfound`: A pointer to a flag for whether the preferred CMM was found. On return, has the value `true` if the CMM specified by the profile was not available to perform flattening or does not support this function and the default CMM was used. Has the value `false` if the profile’s preferred CMM is able to perform flattening.

  Starting with ColorSync 2.5, the ColorSync Manager calls your transfer function directly, without going through the preferred, or any, CMM. On return, the value of `preferredCMMnotfound` is guaranteed to be `false`.

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
- [NCMGetProfileLocation](./api-1804889-ncmgetprofilelocation.md)
  Obtains either a profile location structure for a specified profile or the size of the location structure for the profile.
- [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md)
  Increments the reference count for the specified profile reference.
- [CMGetProfileRefCount](./api-1804894-cmgetprofilerefcount.md)
  Obtains the current reference count for the specified profile.
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804897-cmflattenprofile)*