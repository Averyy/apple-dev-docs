# CMGetProfileByAVID

**Framework**: Application Services  
**Kind**: func

Gets the current profile for a monitor.

## Declaration

```c
CMError CMGetProfileByAVID (
   CMDisplayIDType theID,
   CMProfileRef *prof
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

If the Display Manager supports ColorSync, the `CMGetProfileByAVID` function calls on the Display Manager to get the profile for the specified display. This is the case if the version of the Display Manager is 2.2.5 or higher (if `gestaltDisplayMgrAttr` has the `gestaltDisplayMgrColorSyncAware` bit set). 

## Parameters

- `theAVID`: A Display Manager ID value. You pass the ID value for the monitor for which to get the profile. 
- `prof`: A pointer to a profile reference. On return, a reference to the current profile for the monitor specified by `theAVID`. 

## See Also

### Accessing Special Profiles
- [CMGetSystemProfile](./api-1804926-cmgetsystemprofile.md)
  Obtains a reference to the current system profile.
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
- [CMSetProfileByAVID](./api-1804959-cmsetprofilebyavid.md)
  Sets the profile for the specified monitor, optionally setting video card gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804955-cmgetprofilebyavid)*