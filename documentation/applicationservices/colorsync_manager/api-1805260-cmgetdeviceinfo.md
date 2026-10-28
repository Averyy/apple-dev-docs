# CMGetDeviceInfo

**Framework**: Application Services  
**Kind**: func

Gets information about a specified device.

## Declaration

```c
CMError CMGetDeviceInfo (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   CMDeviceInfo *deviceInfo
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `deviceClass`: A device class to query. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: A device ID to query. You can pass `cmDefaultDeviceID`.
- `deviceInfo`: On input, points to a device information dictionary On output, the dictionary is filled with device information. If, on input, `deviceInfo->deviceName` is `nil` then the name is not returned. If you wants the device name dictionary returned, you should provide in `deviceInfo->deviceName` the address where this routine should store the CFDictionaryRef. The caller is responsible for disposing of the name dictionary.

## See Also

### Accessing Device State and Information
- [CMGetDeviceState](./api-1805257-cmgetdevicestate.md)
  Gets the state of a device.
- [CMSetDeviceState](./api-1805258-cmsetdevicestate.md)
  Sets the state of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805260-cmgetdeviceinfo)*