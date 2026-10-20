# IOServiceNotificationDispatchSource

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- DriverKit 19.0+
- macOS 10.15.4+

## Declaration

*DriverKit*

```cpp
class IOServiceNotificationDispatchSource : IODispatchSource
```

*macOS*

```cpp
class IOServiceNotificationDispatchSource : IODispatchSource, IOServiceNotificationDispatchSourceInterface
```

## Topics

### Instance Methods
- [- Cancel](../DriverKit/ioservicenotificationdispatchsource/cancel.md)
- [- Cancel_Impl](./ioservicenotificationdispatchsource/api-3538520-cancel_impl.md)
- [- CheckForWork](../DriverKit/ioservicenotificationdispatchsource/checkforwork.md)
- [- CheckForWork_Impl](./ioservicenotificationdispatchsource/api-3538521-checkforwork_impl.md)
- [- CopyNextNotification](./ioservicenotificationdispatchsource/api-3538522-copynextnotification.md)
- [- CopyNextNotification](../DriverKit/ioservicenotificationdispatchsource/copynextnotification.md)
- [- CopyNextNotification_Impl](./ioservicenotificationdispatchsource/api-3538523-copynextnotification_impl.md)
- [- DeliverNotifications](./ioservicenotificationdispatchsource/api-3538529-delivernotifications.md)
- [- Dispatch](./ioservicenotificationdispatchsource/api-3538530-dispatch.md)
- [- ServiceNotificationReady](./ioservicenotificationdispatchsource/api-3538531-servicenotificationready.md)
- [- ServiceNotificationReady](../DriverKit/ioservicenotificationdispatchsource/servicenotificationready.md)
- [- SetEnableWithCompletion](../DriverKit/ioservicenotificationdispatchsource/setenablewithcompletion.md)
- [- SetEnableWithCompletion_Impl](./ioservicenotificationdispatchsource/api-3538533-setenablewithcompletion_impl.md)
- [- SetHandler](./ioservicenotificationdispatchsource/api-3538534-sethandler.md)
- [- SetHandler](../DriverKit/ioservicenotificationdispatchsource/sethandler.md)
- [- SetHandler_Impl](./ioservicenotificationdispatchsource/api-3538535-sethandler_impl.md)
- [- free](./ioservicenotificationdispatchsource/api-3538537-free.md)
- [- getMetaClass](./ioservicenotificationdispatchsource/api-3538538-getmetaclass.md)
- [- init](./ioservicenotificationdispatchsource/api-3538539-init.md)
### Type Methods
- [+ CopyNextNotification_Invoke](./ioservicenotificationdispatchsource/api-3538524-copynextnotification_invoke.md)
- [+ Create](./ioservicenotificationdispatchsource/api-3538525-create.md)
- [+ Create_Call](./ioservicenotificationdispatchsource/api-3538526-create_call.md)
- [+ Create_Impl](./ioservicenotificationdispatchsource/api-3538527-create_impl.md)
- [+ Create_Invoke](./ioservicenotificationdispatchsource/api-3538528-create_invoke.md)
- [+ ServiceNotificationReady_Invoke](./ioservicenotificationdispatchsource/api-4519996-servicenotificationready_invoke.md)
- [+ ServiceNotificationReady_Invoke](./ioservicenotificationdispatchsource/api-4519997-servicenotificationready_invoke.md)
- [+ SetHandler_Invoke](./ioservicenotificationdispatchsource/api-3538536-sethandler_invoke.md)

## Relationships

### Inherits From
- [IODispatchSource](../DriverKit/iodispatchsource.md)
- [IODispatchSource](./iodispatchsource.md)
- [IOServiceNotificationDispatchSourceInterface](./ioservicenotificationdispatchsourceinterface.md)

## See Also

### Notifications
- [IOServiceNotificationDispatchSourceInterface](./ioservicenotificationdispatchsourceinterface.md)
- [IONotifier](./ionotifier.md)
  An abstract base class defining common methods for controlling a notification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservicenotificationdispatchsource)*