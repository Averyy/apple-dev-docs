# CMValidateProfile

**Framework**: Application Services  
**Kind**: func

Indicates whether the specified profile contains the minimum set of elements required by the current color management module (CMM) for color matching or color checking.

## Declaration

```c
CMError CMValidateProfile (
   CMProfileRef prof,
   Boolean *valid,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

When your application calls the `CMValidateProfile` function, the ColorSync Manager dispatches the function to the CMM specified by the `CMMType` header field of the profile whose reference you specify. The preferred CMM can support this function or not.

If the preferred CMM supports this function, it determines if the profile contains the baseline elements for the profile class, which the CMM requires to perform color matching or gamut checking. For each profile class, such as a device profile, there is a specific set of required tagged elements defined by the ICC that the profile must include. The ICC also defines optional tags, which may be included in a profile. A CMM might use these optional elements to optimize or improve its processing. Additionally, a profile might include private tags defined to provide a CMM with processing capability particular to the needs of that CMM. The profile developer can define these private tags, register the tag signatures with the ICC, and include the tags in a profile. The CMM checks only for the existence of profile elements it does not check the element’s content and size.

If the preferred CMM does not support the `CMValidateProfile` function request, the ColorSync Manager calls the default CMM to handle the validation request. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile to validate. 
- `valid`: A pointer to a valid profile flag. On return, has the value `true` if the profile contains the minimum set of elements to be valid and `false` if it does not. 
- `preferredCMMnotfound`: A pointer to a flag for whether the preferred CMM was found. On return, has the value `true` if the CMM specified by the profile was not available to perform validation or does not support this function and the default CMM was used. Has the value `false` if the profile’s preferred CMM is able to perform validation.

## See Also

### Accessing Profiles
- [CMOpenProfile](./api-1804853-cmopenprofile.md)
  Opens the specified profile and returns a reference to the profile.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804856-cmvalidateprofile)*