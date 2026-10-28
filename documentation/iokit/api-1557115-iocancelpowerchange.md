# IOCancelPowerChange

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

The caller denies an idle system sleep power state change.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IOCancelPowerChange(io_connect_t kernelPort, intptr_t notificationID);
```

## Return Value

Returns kIOReturnSuccess or an error condition if request failed.

## Discussion

Should only called in response to kIOMessageCanSystemSleep messages from IOPMrootDomain. IOCancelPowerChange has no meaning for responding to kIOMessageSystemWillSleep (which is non-abortable) or any other messages.

When an app responds to a kIOMessageCanSystemSleep message by calling IOCancelPowerChange, the app vetoes the idle sleep request. The system will stay awake. The idle timer will elapse again after a period of inactivity, and the system will send out the same kIOMessageCanSystemSleep message, and interested applications will respond gain.

## Parameters

- `kernelPort`: Port used to communicate to the kernel, from IORegisterApp or IORegisterForSystemPower.
- `notificationID`: A copy of the notification ID which came as part of the power state change notification being acknowledged.

## See Also

### Notifications
- [IOAllowPowerChange](./api-1557064-ioallowpowerchange.md)
  The caller acknowledges notification of a power state change on a device it has registered for notifications for via IORegisterForSystemPower or IORegisterApp.
- [IODeregisterApp](./api-1557129-ioderegisterapp.md)
  Disconnects the caller from an IOService after receiving power state change notifications from the IOService. (Caller must also release IORegisterApp's return io_connect_t and returned IONotificationPortRef for complete clean-up).
- [IODeregisterForSystemPower](./api-1557132-ioderegisterforsystempower.md)
  Disconnects the caller from the Root Power Domain IOService after receiving system power state change notifications. (Caller must also destroy the IONotificationPortRef returned from IORegisterForSystemPower.)
- [IORegisterApp](./api-1557102-ioregisterapp.md)
  Connects the caller to an IOService for the purpose of receiving power state change notifications for the device controlled by the IOService.
- [IORegisterForSystemPower](./api-1557114-ioregisterforsystempower.md)
  Connects the caller to the Root Power Domain IOService for the purpose of receiving sleep & wake notifications for the system. Does not provide system shutdown and restart notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557115-iocancelpowerchange)*