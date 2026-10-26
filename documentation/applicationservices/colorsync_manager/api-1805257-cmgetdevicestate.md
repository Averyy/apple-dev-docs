# CMGetDeviceState

**Framework**: Application Services  
**Kind**: func

Gets the state of a device.

## Declaration

```c
CMError CMGetDeviceState (
   CMDeviceClass deviceClass,
   CMDeviceID deviceID,
   CMDeviceState *deviceState
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `deviceClass`: A device class to query. See [`CMDeviceClass`](../cmdeviceclass.md) for a list of the constants you can supply.
- `deviceID`: A device ID to query. You can pass `cmDefaultDeviceID`.
- `deviceState`: On output, points to the device state. See [Device States](../api-1560516-device_states.md) for the values that can be returned.

## See Also

### Accessing Device State and Information
- [CMSetDeviceState](./api-1805258-cmsetdevicestate.md)
  Sets the state of a device.
- [CMGetDeviceInfo](./api-1805260-cmgetdeviceinfo.md)
  Gets information about a specified device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805257-cmgetdevicestate)*