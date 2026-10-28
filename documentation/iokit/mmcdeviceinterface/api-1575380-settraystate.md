# SetTrayState

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a START_STOP_UNIT command to the device as defined in SBC-3.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetTrayState)(void *self, UInt8 trayState);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNotPermitted if media is inserted, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

## Discussion

Once an MMCDeviceInterface is opened and all volumes associated with that device's media have been unmounted, the client may send this command to eject the tray.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `trayState`: A UInt8 describing which tray state is desired. The tray state can be one of two values, kMMCDeviceTrayClosed or kMMCDeviceTrayOpen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575380-settraystate)*