# CMSetDeviceFactoryProfiles

**Framework**: Application Services  
**Kind**: func

Establishes the profiles used by a given device. 

## Declaration

```c
CMError CMSetDeviceFactoryProfiles (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   CMDeviceProfileID defaultProfID,
   const CMDeviceProfileArray *deviceProfiles
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

This function establishes the profiles used by a given device. It should be called after device registration to notify ColorSync of the device's profiles. Note that factory device profiles and the current device profiles might not be the same, since the latter may contain modifications to the factory set. 

## Parameters

- `deviceClass`: The device class for the device whose factory profiles you want to establish. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply. 
- `deviceID`: The device ID for the device whose factory profiles you want to establish.
- `defaultProfID`: The ID of the default profile for this device.
- `deviceProfiles`: On output, points to array that contains the factory device profiles. 

## See Also

### Accessing Devices Profiles
- [CMGetDeviceFactoryProfiles](./api-1805240-cmgetdevicefactoryprofiles.md)
  Retrieves the original profiles for a given device. 
- [CMGetDeviceProfiles](./api-1805245-cmgetdeviceprofiles.md)
  Gets the profiles used by a given device.
- [CMSetDeviceProfiles](./api-1805247-cmsetdeviceprofiles.md)
  Changes the profiles used by a given device.
- [CMGetDeviceDefaultProfileID](./api-1805249-cmgetdevicedefaultprofileid.md)
  Gets the default profile ID for a given device. 
- [CMSetDeviceDefaultProfileID](./api-1805251-cmsetdevicedefaultprofileid.md)
  Sets the default profile ID for a given device. 
- [CMSetDeviceProfile](./api-1805253-cmsetdeviceprofile.md)
  Change the profile used by a given device. 
- [CMGetDeviceProfile](./api-1805256-cmgetdeviceprofile.md)
  Gets a profile used by a given device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805241-cmsetdevicefactoryprofiles)*