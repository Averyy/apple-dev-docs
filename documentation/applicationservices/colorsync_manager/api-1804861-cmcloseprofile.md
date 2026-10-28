# CMCloseProfile

**Framework**: Application Services  
**Kind**: func

Decrements the reference count for the specified profile reference and, if the reference count reaches 0, frees all private memory and other resources associated with the profile.

## Declaration

```c
CMError CMCloseProfile (
   CMProfileRef prof
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The ColorSync Manager keeps an internal reference count for each profile reference returned from a call to the [CMOpenProfile](./api-1804853-cmopenprofile.md), [CMNewProfile](./api-1804911-cmnewprofile.md), [CMCopyProfile](./api-1804870-cmcopyprofile.md), or [CWNewLinkProfile](./api-1804915-cwnewlinkprofile.md) functions. Calling the function [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md) increments the count; calling the `CMCloseProfile` function decrements it. The profile remains open as long as the reference count is greater than 0, indicating there is at least one remaining reference to the profile. When the count reaches 0, the ColorSync Manager releases all private memory, files, or resources allocated in association with that profile.

When the ColorSync Manager releases all private memory and resources associated with a profile, any temporary changes your application made to the profile are not saved unless you first call the `CMUpdateProfile` function to update the profile.

When your application passes a copy of a profile reference to an independent task, whether synchronous or asynchronous, it should call the function [CMCloneProfileRef](./api-1804891-cmcloneprofileref.md) to increment the reference count. Both the called task and the caller should call `CMCloseProfile` when finished with the profile reference.

You call `CMCloneProfileRef` after copying a profile reference, but not after duplicating an entire profile (as with the `CMCopyProfile` function).

When your application passes a copy of a profile reference internally, it may not need to call `CMCloneProfileRef`, as long as the application calls `CMCloseProfile` once for the profile.

In your application, make sure that `CMCloseProfile` is called once for each time a profile reference is created or cloned. Otherwise, the private memory and resources associated with the profile reference may not be properly freed, or an application may attempt to use a profile reference that is no longer valid.

If you create a new profile by calling the `CMNewProfile` function, the profile is saved to disk when you call the `CMCloseProfile` function unless you specified `NULL` as the profile location when you created the profile.

To save changes to a profile before closing it, use the function [CMUpdateProfile](./api-1804864-cmupdateprofile.md). 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that identifies the profile that may need to be closed. 

## See Also

### Accessing Profiles
- [CMOpenProfile](./api-1804853-cmopenprofile.md)
  Opens the specified profile and returns a reference to the profile.
- [CMValidateProfile](./api-1804856-cmvalidateprofile.md)
  Indicates whether the specified profile contains the minimum set of elements required by the current color management module (CMM) for color matching or color checking.
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
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804861-cmcloseprofile)*