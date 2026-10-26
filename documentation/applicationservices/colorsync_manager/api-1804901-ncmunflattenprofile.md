# NCMUnflattenProfile

**Framework**: Application Services  
**Kind**: func

Unflattens a previously flattened profile.

## Declaration

```c
CMError NCMUnflattenProfile (
   CMProfileLocation *targetLocation,
   CMFlattenUPP proc,
   void *refCon,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `targetLocation`: The location of the profile you want to unflatten. Commonly a profile is disk-file based. However, the profile may be a file-based profile, a handle-based profile, or a pointer-based profile. 
- `proc`: A user-defined procedure which is called during the unflatten operation. 
- `refCon`: A reference constant containing data specified by the calling application program. 
- `preferredCMMnotfound`: A return value indicating whether or not the CMM specified in the profile was found. 

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
- [CMFlattenProfile](./api-1804897-cmflattenprofile.md)
  Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804901-ncmunflattenprofile)*