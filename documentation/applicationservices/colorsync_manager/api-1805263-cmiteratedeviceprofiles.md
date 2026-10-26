# CMIterateDeviceProfiles

**Framework**: Application Services  
**Kind**: func

Iterates through the device profiles available on the system and returns information about profiles of the devices to a callback you supply.

## Declaration

```c
CMError CMIterateDeviceProfiles (
   CMIterateDeviceProfileProcPtr proc,
   UInt32 *seed,
   UInt32 *count,
   UInt32 flags,
   void *refCon
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `proc`: A pointer to a function that iterates through device information available on the system. This is optional, but allows you to obtain profile information for each device. If provided, your callback is invoked once for each registered device.
- `seed`: A pointer to a seed value. This is optional. If you pass a pointer to a seed value that is the same as the current seed value, then the callback function specified by the `proc `parameter is not invoked.
- `count`: On output, the number of color devices available on the system.
- `flags`: A value that specifies which set of profiles you want to iterate through. It can have the following values: `cmIterateFactoryDeviceProfiles`, `cmIterateCustomDeviceProfiles`, `cmIterateCurrentDeviceProfiles`, `cmIterateAllDeviceProfiles` or `0`. Supplying `0` is the same as supplying `cmIterateCurrentDeviceProfiles`.
- `refCon`: An optional value that passed to your callback.

## See Also

### Iterating Over Devices and Device Profiles
- [CMIterateColorDevices](./api-1805262-cmiteratecolordevices.md)
  Iterates through the color devices available on the system, returning device information to a callback you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805263-cmiteratedeviceprofiles)*