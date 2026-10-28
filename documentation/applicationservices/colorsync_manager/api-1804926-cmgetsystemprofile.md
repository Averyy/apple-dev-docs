# CMGetSystemProfile

**Framework**: Application Services  
**Kind**: func

Obtains a reference to the current system profile.

## Declaration

```c
CMError CMGetSystemProfile (
   CMProfileRef *prof
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The following functions allow you to pass `NULL` as a parameter value to specify the system profile as a source or destination profile:

- [CMNewProfile](./api-1804911-cmnewprofile.md)
- [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md)
- [NCMBeginMatching](./api-1805216-ncmbeginmatching.md)
- [NCMDrawMatchedPicture](./api-1805223-ncmdrawmatchedpicture.md)

Note that instead of passing `NULL`, you can pass a profile reference to a specific profile, including the system profile.

If you want to specify the system profile for any other function that requires a profile reference, such as [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) and [CWNewLinkProfile](./api-1804915-cwnewlinkprofile.md), you must use an explicit reference. You can obtain such a reference with the `CMGetSystemProfile` function.

There are other reasons you might need to obtain a reference to the current system profile. For example, your application might need to display the name of the current system profile to a user.

To identify the location of the physical file, call the function [CMGetProfileLocation](./api-1804885-cmgetprofilelocation.md).

When your application has finished using the current system profile, it must close the reference to the profile by calling the function [CMCloseProfile](./api-1804861-cmcloseprofile.md). 

### Version-Notes

Starting with version 2.5, use of the system profile has changed. So rather than call `CMGetSystemProfile` to obtain a reference to the system profile, you may be able to obtain a profile that is more appropriate for the current operation by calling [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for a color space or by calling [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get the profile for a specific display.

## Parameters

- `prof`: A pointer to a profile reference of type [`CMProfileRef`](../cmprofileref.md). On return, a reference to the current system profile. 

## See Also

### Accessing Special Profiles
- [CMSetSystemProfile](./api-1804932-cmsetsystemprofile.md)
  Sets the current system profile.
- [NCMSetSystemProfile](./api-1804936-ncmsetsystemprofile.md)
  Sets the location of a color profile.
- [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md)
  Gets the default profile for the specified color space.
- [CMSetDefaultProfileBySpace](./api-1804944-cmsetdefaultprofilebyspace.md)
  Sets the default profile for the specified color space.
- [CMGetDefaultProfileByUse](./api-1804948-cmgetdefaultprofilebyuse.md)
  Obtains the users’ preferred device profile setting.
- [CMSetDefaultProfileByUse](./api-1804951-cmsetdefaultprofilebyuse.md)
  Sets values for device profile settings.
- [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md)
  Gets the current profile for a monitor.
- [CMSetProfileByAVID](./api-1804959-cmsetprofilebyavid.md)
  Sets the profile for the specified monitor, optionally setting video card gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804926-cmgetsystemprofile)*