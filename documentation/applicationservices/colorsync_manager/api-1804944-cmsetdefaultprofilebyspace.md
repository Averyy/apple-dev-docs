# CMSetDefaultProfileBySpace

**Framework**: Application Services  
**Kind**: func

Sets the default profile for the specified color space.

## Declaration

```c
CMError CMSetDefaultProfileBySpace (
   OSType dataColorSpace,
   CMProfileRef prof
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMSetDefaultProfileBySpace` function currently supports the RGB, CMYK, Lab, and XYZ color spaces. The signature constants for these color spaces (shown above with the `dataColorSpace` parameter description) are described in [Color Space Signatures](../api-1560276-color_space_signatures.md). Support for additional color spaces may be provided in the future. `CMSetDefaultProfileBySpace` returns a value of `paramErr` if you pass a color space constant it does not currently support.

Note that a user can also use the ColorSync control panel to specify a default profile for the RGB and CMYK color spaces. 

## Parameters

- `dataColorSpace`: A four-character identifier of type `OSType`. You pass a color space signature that identifies the color space you wish to set the default profile for. The currently-supported values are `cmRGBData`, `cmCMYKData`, `cmLabData`, and `cmXYZData`. These constants are a subset of the constants described in [Color Space Signatures](../api-1560276-color_space_signatures.md). If you supply a value that is not supported, the `CMGetDefaultProfileBySpace` function returns an error value of `paramErr`. 
- `prof`: A profile reference. Before calling `CMSetDefaultProfileBySpace`, set the reference to specify the default profile for the color space. The profile must be file-based; otherwise, the function returns a `CMInvalidProfileLocation` error. 

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
- [CMGetDefaultProfileByUse](./api-1804948-cmgetdefaultprofilebyuse.md)
  Obtains the users’ preferred device profile setting.
- [CMSetDefaultProfileByUse](./api-1804951-cmsetdefaultprofilebyuse.md)
  Sets values for device profile settings.
- [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md)
  Gets the current profile for a monitor.
- [CMSetProfileByAVID](./api-1804959-cmsetprofilebyavid.md)
  Sets the profile for the specified monitor, optionally setting video card gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804944-cmsetdefaultprofilebyspace)*