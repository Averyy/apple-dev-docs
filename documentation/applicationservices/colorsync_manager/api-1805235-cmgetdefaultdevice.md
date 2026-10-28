# CMGetDefaultDevice

**Framework**: Application Services  
**Kind**: func

Gets the default device.

## Declaration

```c
CMError CMGetDefaultDevice (
   CMDeviceClass deviceClass,
   CMDeviceID *deviceID
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

For each class of device, a device management layer may establish which of the registered devices is the default. This helps keep color management choices to a minimum and allows for some automatic features to be enabled, such as the "Default printer" as an output profile selection. 

## Parameters

- `deviceClass`: The device class whose default device you want to get. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: On return, points to the device ID for the default device.

## See Also

### Accessing Default Devices
- [CMSetDefaultDevice](./api-1805238-cmsetdefaultdevice.md)
  Sets the default device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805235-cmgetdefaultdevice)*