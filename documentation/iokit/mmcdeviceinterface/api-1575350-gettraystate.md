# GetTrayState

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a GET_EVENT_STATUS_NOTIFICATION command to the device as defined in MMC-2.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetTrayState)(void *self, UInt8 *trayState);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

## Discussion

Once an MMCDeviceInterface is opened, the client may send this command to find out if the device's medium tray is open.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `trayState`: Pointer to a UInt8 which will hold the tray state on completion of the routine. The tray state can be one of two values, kMMCDeviceTrayClosed or kMMCDeviceTrayOpen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575350-gettraystate)*