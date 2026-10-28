# IORegisterForSystemPower

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Connects the caller to the Root Power Domain IOService for the purpose of receiving sleep & wake notifications for the system. Does not provide system shutdown and restart notifications.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
io_connect_t IORegisterForSystemPower(void *refcon, IONotificationPortRef *thePortRef, IOServiceInterestCallback callback, io_object_t *notifier);
```

## Return Value

Returns a io_connect_t session for the IOPMrootDomain or MACH_PORT_NULL if request failed. Caller must close return value via IOServiceClose() after calling IODeregisterForSystemPower on the notifier argument.

## Discussion

Provides sleep/wake notifications to applications. Requires that applications acknowledge some, but not all notifications. Register for sleep/wake notifications will deliver these messages over the sleep/wake lifecycle:

- kIOMessageSystemWillSleep is delivered at the point the system is initiating a non-abortable sleep. Callers MUST acknowledge this event by calling [`IOAllowPowerChange`](./api-1557064-ioallowpowerchange.md). If a caller does not acknowledge the sleep notification, the sleep will continue anyway after a 30 second timeout (resulting in bad user experience). Delivered before any hardware is powered off.

- kIOMessageSystemWillPowerOn is delivered at early wakeup time, before most hardware has been powered on. Be aware that any attempts to access disk, network, the display, etc. may result in errors or blocking your process until those resources become available. Caller must NOT acknowledge kIOMessageSystemWillPowerOn; the caller must simply return from its handler.

- kIOMessageSystemHasPoweredOn is delivered at wakeup completion time, after all device drivers and hardware have handled the wakeup event. Expect this event 1-5 or more seconds after initiating system wakeup. Caller must NOT acknowledge kIOMessageSystemHasPoweredOn; the caller must simply return from its handler.

- kIOMessageCanSystemSleep indicates the system is pondering an idle sleep, but gives apps the chance to veto that sleep attempt. Caller must acknowledge kIOMessageCanSystemSleep by calling [`IOAllowPowerChange`](./api-1557064-ioallowpowerchange.md) or [`IOCancelPowerChange`](./api-1557115-iocancelpowerchange.md). Calling IOAllowPowerChange will not veto the sleep; any app that calls IOCancelPowerChange will veto the idle sleep. A kIOMessageCanSystemSleep notification will be followed up to 30 seconds later by a kIOMessageSystemWillSleep message. or a kIOMessageSystemWillNotSleep message.

- kIOMessageSystemWillNotSleep is delivered when some app client has vetoed an idle sleep request. kIOMessageSystemWillNotSleep may follow a kIOMessageCanSystemSleep notification, but will not otherwise be sent. Caller must NOT acknowledge kIOMessageSystemWillNotSleep; the caller must simply return from its handler.

To deregister for sleep/wake notifications, the caller must make two calls, in this order: - Call IODeregisterForSystemPower with the 'notifier' argument returned here. - Then call IONotificationPortDestroy passing the 'thePortRef' argument returned here.

## Parameters

- `refcon`: Caller may provide data to receive s an argument to 'callback' on power state changes.
- `thePortRef`: On return, thePortRef is a pointer to an IONotificationPortRef, which will deliver the power notifications. The port is allocated by this function and must be later released by the caller (after calling [`IODeregisterForSystemPower`](./api-1557132-ioderegisterforsystempower.md)). The caller should also enable IONotificationPortRef by calling [`IONotificationPortGetRunLoopSource`](./api-1514599-ionotificationportgetrunloopsour.md), or [`IONotificationPortGetMachPort`](./api-1514875-ionotificationportgetmachport.md), or [`IONotificationPortSetDispatchQueue`](./api-1514596-ionotificationportsetdispatchque.md).
- `callback`: A c-function which is called during the notification.
- `notifier`: On success, returns a pointer to a unique notifier which caller must keep and pass to a subsequent call to IODeregisterForSystemPower.

## See Also

### Notifications
- [IOAllowPowerChange](./api-1557064-ioallowpowerchange.md)
  The caller acknowledges notification of a power state change on a device it has registered for notifications for via IORegisterForSystemPower or IORegisterApp.
- [IOCancelPowerChange](./api-1557115-iocancelpowerchange.md)
  The caller denies an idle system sleep power state change.
- [IODeregisterApp](./api-1557129-ioderegisterapp.md)
  Disconnects the caller from an IOService after receiving power state change notifications from the IOService. (Caller must also release IORegisterApp's return io_connect_t and returned IONotificationPortRef for complete clean-up).
- [IODeregisterForSystemPower](./api-1557132-ioderegisterforsystempower.md)
  Disconnects the caller from the Root Power Domain IOService after receiving system power state change notifications. (Caller must also destroy the IONotificationPortRef returned from IORegisterForSystemPower.)
- [IORegisterApp](./api-1557102-ioregisterapp.md)
  Connects the caller to an IOService for the purpose of receiving power state change notifications for the device controlled by the IOService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557114-ioregisterforsystempower)*