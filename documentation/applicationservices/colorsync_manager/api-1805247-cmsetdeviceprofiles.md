# CMSetDeviceProfiles

**Framework**: Application Services  
**Kind**: func

Changes the profiles used by a given device.

## Declaration

```c
CMError CMSetDeviceProfiles (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   const CMDeviceProfileScope *profileScope,
   const CMDeviceProfileArray *deviceProfiles
);
```

#### Return Value

A `CMError` value. If you pass a n invalid `CMDeviceClass` or `CMDeviceID`, the function returns `CMInvalidDeviceClass` or `CMInvalidDeviceID`. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

This function provides a way to change the profiles used by a given device. It can be called after device registration by calibration applications to reset a device's profiles from factory defaults to calibrated profiles. In order for this call to be made successfully, the caller must pass the `CMDeviceClass` and `CMDeviceID` device being calibrated. (You can call the function `CMIterateColorDevices` to find available device classes and IDs.). 

## Parameters

- `deviceClass`: The device class for the device whose profiles you want to set. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: The device ID for the device whose profiles you want to set.
- `profileScope`: A pointer to the structure defining the scope these profiles pertain to. 
- `deviceProfiles`: A pointer to the profile array that contains replacements for the factory profiles. You don’t have to replace all the original profiles with this call. The array can contain as few as one profile or as many profiles as there are in the original factory array. You supply only those profiles you want to replace. Profiles are replaced by ID. 

## See Also

### Accessing Devices Profiles
- [CMGetDeviceFactoryProfiles](./api-1805240-cmgetdevicefactoryprofiles.md)
  Retrieves the original profiles for a given device. 
- [CMSetDeviceFactoryProfiles](./api-1805241-cmsetdevicefactoryprofiles.md)
  Establishes the profiles used by a given device. 
- [CMGetDeviceProfiles](./api-1805245-cmgetdeviceprofiles.md)
  Gets the profiles used by a given device.
- [CMGetDeviceDefaultProfileID](./api-1805249-cmgetdevicedefaultprofileid.md)
  Gets the default profile ID for a given device. 
- [CMSetDeviceDefaultProfileID](./api-1805251-cmsetdevicedefaultprofileid.md)
  Sets the default profile ID for a given device. 
- [CMSetDeviceProfile](./api-1805253-cmsetdeviceprofile.md)
  Change the profile used by a given device. 
- [CMGetDeviceProfile](./api-1805256-cmgetdeviceprofile.md)
  Gets a profile used by a given device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805247-cmsetdeviceprofiles)*