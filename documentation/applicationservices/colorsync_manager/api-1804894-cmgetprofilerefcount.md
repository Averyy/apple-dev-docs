# CMGetProfileRefCount

**Framework**: Application Services  
**Kind**: func

Obtains the current reference count for the specified profile.

## Declaration

```c
CMError CMGetProfileRefCount (
   CMProfileRef prof,
   long *count
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The ColorSync Manager keeps an internal reference count for each profile reference returned from calls such as [CMOpenProfile](./api-1804853-cmopenprofile.md) or [CMNewProfile](./api-1804911-cmnewprofile.md). Calling the function [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md) increments the count; calling the function [CMCloseProfile](./api-1804861-cmcloseprofile.md) decrements it. The profile remains open as long as the reference count is greater than 0, indicating at least one routine retains a reference to the profile. When the count reaches 0, the ColorSync Manager releases all memory, files, or resources allocated in association with that profile.

An application that manages profiles closely can call the `CMGetProfileRefCount` function to obtain the reference count for a profile reference, then perform special handling if necessary, based on the reference count.

To copy a profile with the function [CMCopyProfile](./api-1804870-cmcopyprofile.md), you must obtain a reference to that profile by either opening the profile or creating it. To open a profile, use the function [CMOpenProfile](./api-1804853-cmopenprofile.md). To create a new profile, use the function [CMNewProfile](./api-1804911-cmnewprofile.md). As an alternative to using the `CMCopyProfile` function to duplicate an entire profile, you can use the same profile reference more than once. To do so, you call the function [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md) to increment the reference count for the reference each time you reuse it. Calling the `CMCloneProfileRef` function increments the count; calling the function [CMCloseProfile](./api-1804861-cmcloseprofile.md) decrements it. The profile remains open as long as the reference count is greater than 0, indicating at least one routine retains a reference to the profile. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile whose reference count is obtained. 
- `count`: A pointer to a reference count. On return, the reference count for the specified profile reference. 

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
- [CMFlattenProfile](./api-1804897-cmflattenprofile.md)
  Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804894-cmgetprofilerefcount)*