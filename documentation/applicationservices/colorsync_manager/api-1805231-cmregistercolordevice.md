# CMRegisterColorDevice

**Framework**: Application Services  
**Kind**: func

Registers a device with ColorSync.

## Declaration

```c
CMError CMRegisterColorDevice (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   CFDictionaryRef deviceName,
   const CMDeviceScope *deviceScope
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

For a device to be recognized by ColorSync (and possibly other parts of macOS) it needs to register itself using this function. If the device has ColorSync profiles associated with it, it should identify those u after registering with this function. Once a device is registered, it can appear as an input, output, or proofing device in ColorSync controls, as long as it has profiles associated with it. Registration need only happen once, when the device is installed. Device drivers need not register their device each time they are loaded. 

## Parameters

- `deviceSpec`: The class of the device (e.g., 'scnr' ,'cmra' ,'prtr' ,'mntr' ). 
- `deviceScope`: The unique identifier of the class (Class + ID uniquely id's device). 
- `deviceName`: Name of the device. See the CFDictionary documentation for a description of the `CFDictionaryRef` data type.
- `deviceScope`: Structure defining the user and host scope this device pertains                    to. 

## See Also

### Registering Devices
- [CMUnregisterColorDevice](./api-1805234-cmunregistercolordevice.md)
  Unregisters a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805231-cmregistercolordevice)*