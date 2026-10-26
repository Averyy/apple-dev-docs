# IODeregisterForSystemPower

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Disconnects the caller from the Root Power Domain IOService after receiving system power state change notifications. (Caller must also destroy the IONotificationPortRef returned from IORegisterForSystemPower.)

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IODeregisterForSystemPower(io_object_t *notifier);
```

#### Return Value

Returns kIOReturnSuccess or an error condition if request failed.

## Parameters

- `notifier`: The object returned from IORegisterForSystemPower.

## See Also

### Notifications
- [IOAllowPowerChange](./api-1557064-ioallowpowerchange.md)
  The caller acknowledges notification of a power state change on a device it has registered for notifications for via IORegisterForSystemPower or IORegisterApp.
- [IOCancelPowerChange](./api-1557115-iocancelpowerchange.md)
  The caller denies an idle system sleep power state change.
- [IODeregisterApp](./api-1557129-ioderegisterapp.md)
  Disconnects the caller from an IOService after receiving power state change notifications from the IOService. (Caller must also release IORegisterApp's return io_connect_t and returned IONotificationPortRef for complete clean-up).
- [IORegisterApp](./api-1557102-ioregisterapp.md)
  Connects the caller to an IOService for the purpose of receiving power state change notifications for the device controlled by the IOService.
- [IORegisterForSystemPower](./api-1557114-ioregisterforsystempower.md)
  Connects the caller to the Root Power Domain IOService for the purpose of receiving sleep & wake notifications for the system. Does not provide system shutdown and restart notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557132-ioderegisterforsystempower)*