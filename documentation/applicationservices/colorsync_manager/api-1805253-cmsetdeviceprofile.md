# CMSetDeviceProfile

**Framework**: Application Services  
**Kind**: func

Change the profile used by a given device. 

## Declaration

```c
CMError CMSetDeviceProfile (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   const CMDeviceProfileScope *profileScope,
   CMDeviceProfileID profileID,
   const CMProfileLocation *profileLoc
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

This function provides a way to change a profile used by a given device by ID. It can be called after device registration by calibration applications to reset a device's profile from factory defaults to calibrated profiles. In order for this call to be made successfully, you must pass the `CMDeviceClass` and `CMDeviceID` of the device being calibrated along with the `CMDeviceProfileID` of the profile to set. (Device selection and identification can be facilitated using the function `CMIterateColorDevices`). If an invalid `CMDeviceClass` or `CMDeviceID` is passed, an error (`CMInvalidDeviceClass` or `CMInvalidDeviceID`) is returned. 

## Parameters

- `deviceClass`: The device class for the device whose profile you want to set. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: The device ID for the device whose profile you want to set.
- `profileScope`: A pointer to the structure defining the scope this profile pertains to. 
- `profileID`: The ID of the default profile for this device. 
- `deviceProfLoc`: A pointer to the `CMProfileLocation` of the profile. Since this structure is a fixed length structure, you can simply pass a pointer to a stack-based structure or memory allocated for it. 

## See Also

### Accessing Devices Profiles
- [CMGetDeviceFactoryProfiles](./api-1805240-cmgetdevicefactoryprofiles.md)
  Retrieves the original profiles for a given device. 
- [CMSetDeviceFactoryProfiles](./api-1805241-cmsetdevicefactoryprofiles.md)
  Establishes the profiles used by a given device. 
- [CMGetDeviceProfiles](./api-1805245-cmgetdeviceprofiles.md)
  Gets the profiles used by a given device.
- [CMSetDeviceProfiles](./api-1805247-cmsetdeviceprofiles.md)
  Changes the profiles used by a given device.
- [CMGetDeviceDefaultProfileID](./api-1805249-cmgetdevicedefaultprofileid.md)
  Gets the default profile ID for a given device. 
- [CMSetDeviceDefaultProfileID](./api-1805251-cmsetdevicedefaultprofileid.md)
  Sets the default profile ID for a given device. 
- [CMGetDeviceProfile](./api-1805256-cmgetdeviceprofile.md)
  Gets a profile used by a given device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805253-cmsetdeviceprofile)*