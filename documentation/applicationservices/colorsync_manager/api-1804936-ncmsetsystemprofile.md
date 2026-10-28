# NCMSetSystemProfile

**Framework**: Application Services  
**Kind**: func

Sets the location of a color profile.

## Declaration

```c
CMError NCMSetSystemProfile (
   const CMProfileLocation *profLoc
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Prior to ColorSync 2.6, the function for setting the system profile supported only the `FSSpec` file specification type as a way of specifying a profile. This function allows for greater flexibility when specifying a system profile. 

## Parameters

- `profLoc`: The location of the profile. Commonly a profile is disk-file based. However, the profile may be a file-based profile, a handle-based profile, or a pointer-based profile. 

## See Also

### Accessing Special Profiles
- [CMGetSystemProfile](./api-1804926-cmgetsystemprofile.md)
  Obtains a reference to the current system profile.
- [CMSetSystemProfile](./api-1804932-cmsetsystemprofile.md)
  Sets the current system profile.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804936-ncmsetsystemprofile)*