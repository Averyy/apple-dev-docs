# CMSetProfileByAVID

**Framework**: Application Services  
**Kind**: func

Sets the profile for the specified monitor, optionally setting video card gamma.

## Declaration

```c
CMError CMSetProfileByAVID (
   CMDisplayIDType theID,
   CMProfileRef prof
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

If you specify a profile that contains the optional profile tag for video card gamma, `CMSetProfileByAVID` extracts the tag and sets the video card based on the tag data. This is the only ColorSync function that sets video card gamma. The tag constant `cmVideoCardGammaTag` is described in [Video Card Gamma Tags](../api-1560164-video_card_gamma_tags.md).

When a user sets a display profile using the Monitors & Sound control panel, the system profile is set to the same profile. When you call `CMSetProfileByAVID` to set a profile for a monitor, you may also wish to make that profile the system profile. If so, you must call [CMSetSystemProfile](./api-1804932-cmsetsystemprofile.md) explicitly—calling `CMSetProfileByAVID` alone has no affect on the system profile.

Note that if the Display Manager supports ColorSync, the `CMSetProfileByAVID` function calls on the Display Manager to set the profile for the specified display. This is the case if the version of the Display Manager is 2.2.5 or higher (if `gestaltDisplayMgrAttr` has the `gestaltDisplayMgrColorSyncAware` bit set). 

## Parameters

- `theAVID`: A Display Manager ID value. You pass the ID value for the monitor for which to set the profile.
- `prof`: A profile reference. Before calling `CMSetProfileByAVID`, set the reference to identify the profile for the monitor specified by `theAVID`. 

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
- [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md)
  Gets the current profile for a monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804959-cmsetprofilebyavid)*