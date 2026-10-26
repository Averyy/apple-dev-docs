# CMIterateColorDevices

**Framework**: Application Services  
**Kind**: func

Iterates through the color devices available on the system, returning device information to a callback you supply.

## Declaration

```c
CMError CMIterateColorDevices (
   CMIterateDeviceInfoProcPtr proc,
   UInt32 *seed,
   UInt32 *count,
   void *refCon
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

This routine gets device information about all registered color devices. If provided, the supplied callback functions is called once for each registered device, passing in the device info and the supplied refcon. 

## Parameters

- `proc`: A pointer to a function that iterates through device information available on the system. This is optional, but allows you to obtain device information. If provided, your callback is invoked once for each registered device.
- `seed`: A pointer to a seed value. This is optional. If you pass a pointer to a seed value that is the same as the current seed value, then the callback function specified by the `proc `parameter is not invoked.
- `count`: On output, the number of color devices available on the system.
- `refCon`: An optional value that passed to your callback.

## See Also

### Iterating Over Devices and Device Profiles
- [CMIterateDeviceProfiles](./api-1805263-cmiteratedeviceprofiles.md)
  Iterates through the device profiles available on the system and returns information about profiles of the devices to a callback you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805262-cmiteratecolordevices)*