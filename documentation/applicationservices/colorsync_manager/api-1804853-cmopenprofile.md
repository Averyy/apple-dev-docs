# CMOpenProfile

**Framework**: Application Services  
**Kind**: func

Opens the specified profile and returns a reference to the profile.

## Declaration

```c
CMError CMOpenProfile (
   CMProfileRef *prof,
   const CMProfileLocation *theProfile
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

If the `CMOpenProfile` function executes successfully, the profile reference refers to the opened profile. Your application uses this reference, for example, when it calls functions to color match, copy, and update a profile, and validate its contents.

The ColorSync Manager maintains private storage for each request to open a profile, allowing more than one application to use a profile concurrently.

When you create a new profile or modify the elements of an existing profile, the ColorSync Manager stores the new or modified elements in the private storage it maintains for your application. Any new or changed profile elements are not incorporated into the profile itself unless your application calls the function [CMUpdateProfile](./api-1804864-cmupdateprofile.md) to update the profile. If you call the function [CMCopyProfile](./api-1804870-cmcopyprofile.md) to create a copy of an existing profile under a new name, any changes you have made are incorporated in the profile duplicate but the original profile remains unchanged.

Before you call the `CMOpenProfile` function, you must set the `CMProfileLocation` data structure to identify the location of the profile to open. Most commonly, a profile is stored in a disk file. If the profile is in a disk file, use the profile location data type to provide its file specification. If the profile is in memory, use the profile location data type to specify a handle or pointer to the profile. If the profile is accessed through a procedure provided by your application, use the profile location data type to supply a universal procedure pointer to your procedure.

Your application must obtain a profile reference before you copy or validate a profile, and before you flatten the profile to embed it.

For example, your application can:

-  open a profile 
-  call the `CMGetProfileHeader` function to obtain the profile’s header to modify its values 
-  set new values 
-  call the `CMSetProfileHeader` function to replace the modified header 
-  pass the profile reference to a function such as [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) as the source or destination profile in a color world for a color-matching session 
-  When you close your reference to the profile by calling the function [CMCloseProfile](./api-1804861-cmcloseprofile.md), your changes are discarded (unless you called the `CMUpdateProfile` function). 

## Parameters

- `prof`: A pointer to a profile reference of type [`CMProfileRef`](../cmprofileref.md). On return, the reference refers to the opened profile. 
- `theProfile`: A pointer to a profile location of type [`CMProfileLocation`](../cmprofilelocation.md) for the profile to open. Commonly a profile is disk-file based, but it may instead be temporary, handle-based, pointer-based, or accessed through a procedure supplied by your application. 

## See Also

### Accessing Profiles
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
- [NCMUnflattenProfile](./api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804853-cmopenprofile)*