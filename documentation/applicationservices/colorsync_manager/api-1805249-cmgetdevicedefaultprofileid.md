# CMGetDeviceDefaultProfileID

**Framework**: Application Services  
**Kind**: func

Gets the default profile ID for a given device. 

## Declaration

```c
CMError CMGetDeviceDefaultProfileID (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   CMDeviceProfileID *defaultProfID
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Device drivers and host software can set the default profile for a given device using the function `CMSetDeviceDefaultProfileID`. 

## Parameters

- `deviceClass`: The device class to query. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: The device ID to query.
- `defaultID`: On output, points to the id of the default profile for this device. 

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
- [CMSetDeviceDefaultProfileID](./api-1805251-cmsetdevicedefaultprofileid.md)
  Sets the default profile ID for a given device. 
- [CMSetDeviceProfile](./api-1805253-cmsetdeviceprofile.md)
  Change the profile used by a given device. 
- [CMGetDeviceProfile](./api-1805256-cmgetdeviceprofile.md)
  Gets a profile used by a given device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805249-cmgetdevicedefaultprofileid)*