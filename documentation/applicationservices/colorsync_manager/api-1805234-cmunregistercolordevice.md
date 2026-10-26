# CMUnregisterColorDevice

**Framework**: Application Services  
**Kind**: func

Unregisters a device.

## Declaration

```c
CMError CMUnregisterColorDevice (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

When a device is no longer to be used on a system (as opposed to being offline), it should be unregistered. If a device is temporarily shut down or disconnected, it does not to be unregistered unless either of the following is true:

- The device driver is being removed (uninstalled)
- The device driver can’t access the device profiles without the device

## Parameters

- `deviceClass`: The device class of the device you want to unregister. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply. 
- `deviceID`: The device ID of the device you want to unregister.

## See Also

### Registering Devices
- [CMRegisterColorDevice](./api-1805231-cmregistercolordevice.md)
  Registers a device with ColorSync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805234-cmunregistercolordevice)*