# CMGetDefaultProfileBySpace

**Framework**: Application Services  
**Kind**: func

Gets the default profile for the specified color space.

## Declaration

```c
CMError CMGetDefaultProfileBySpace (
   OSType dataColorSpace,
   CMProfileRef *prof
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMGetDefaultProfileBySpace` function currently supports the RGB, CMYK, Lab, and XYZ color spaces. The signature constants for these color spaces (shown above with the `dataColorSpace` parameter description) are described in [Color Space Signatures](../api-1560276-color_space_signatures.md). Support for additional color spaces may be provided in the future. `CMGetDefaultProfileBySpace` returns an error value of `paramErr` if you pass a color space constant it does not currently support.

The `CMGetDefaultProfileBySpace` function always attempts to return a file-based profile for a supported color space. For example, if the user has not specified a default profile in the ColorSync control panel for the specified color space, or if the profile is not found (the user may have deleted the profiles in the ColorSync Profiles folder or even the folder itself), `CMGetDefaultProfileBySpace` creates a profile, stores it on disk, and returns a reference to that profile. However, you should always check for an error return—for example, a user may have booted from a CD, so that `CMGetDefaultProfileBySpace` cannot save a profile file to disk. 

## Parameters

- `dataColorSpace`: A four-character identifier of type `OSType`. You pass a color space signature that identifies the color space you wish to get the default profile for. The currently-supported values are `cmRGBData`, `cmCMYKData`, `cmLabData`, and `cmXYZData`. These constants are a subset of the constants described in [Color Space Signatures](../api-1560276-color_space_signatures.md). If you supply a value that is not supported, the `CMGetDefaultProfileBySpace` function returns an error value of `paramErr`. 
- `prof`: A pointer to a profile reference. On return, the reference specifies the current profile for the color space specified by `dataColorSpace`. `CMGetDefaultProfileBySpace` currently supports only file-based profiles. 

## See Also

### Accessing Special Profiles
- [CMGetSystemProfile](./api-1804926-cmgetsystemprofile.md)
  Obtains a reference to the current system profile.
- [CMSetSystemProfile](./api-1804932-cmsetsystemprofile.md)
  Sets the current system profile.
- [NCMSetSystemProfile](./api-1804936-ncmsetsystemprofile.md)
  Sets the location of a color profile.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804940-cmgetdefaultprofilebyspace)*