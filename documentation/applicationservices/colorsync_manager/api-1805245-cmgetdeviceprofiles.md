# CMGetDeviceProfiles

**Framework**: Application Services  
**Kind**: func

Gets the profiles used by a given device.

## Declaration

```c
CMError CMGetDeviceProfiles (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   UInt32 *arraySize,
   CMDeviceProfileArray *deviceProfiles
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `deviceClass`: The device class for the device whose profiles you want to get. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: The device ID for the device whose profiles you want to get.
- `arraySize`: A pointer to the size of the array to be returned. You can first call this routine to get the size returned, then call it again with the size of the buffer to receive the array. 
- `deviceProfiles`: On output, an array of profiles used by the device. You can first pass `NULL` in this parameter to receive the size of the array in the `arraySize` parameter. Then, once the appropriate amount of storage has been allocated, a pointer to it can be passed in this parameter to have the array copied to that storage. 

## See Also

### Accessing Devices Profiles
- [CMGetDeviceFactoryProfiles](./api-1805240-cmgetdevicefactoryprofiles.md)
  Retrieves the original profiles for a given device. 
- [CMSetDeviceFactoryProfiles](./api-1805241-cmsetdevicefactoryprofiles.md)
  Establishes the profiles used by a given device. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805245-cmgetdeviceprofiles)*