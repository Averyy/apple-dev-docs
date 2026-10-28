# CMSetSystemProfile

**Framework**: Application Services  
**Kind**: func

Sets the current system profile.

## Declaration

```c
CMError CMSetSystemProfile (
   const FSSpec *profileFileSpec
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

By default, a standard RGB profile is configured as the system profile. By calling the `CMSetSystemProfile` function, your application can specify a new system profile. You can configure only a display device profile as the system profile. 

### Version-Notes

Starting with version 2.5, use of the system profile has changed.

The function `CMSetSystemProfile` does not retrieve video card gamma data (introduced in ColorSync version 2.5) to set the video card; use the function [CMSetProfileByAVID](./api-1804959-cmsetprofilebyavid.md) instead.

## Parameters

- `profileFileSpec`: A pointer to a file specification structure. Before calling `CMSetSystemProfile`, set the structure to specify the desired system profile. 

## See Also

### Accessing Special Profiles
- [CMGetSystemProfile](./api-1804926-cmgetsystemprofile.md)
  Obtains a reference to the current system profile.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804932-cmsetsystemprofile)*