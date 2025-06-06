# IOServiceNotificationDispatchSource

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- DriverKit 19.0+
- macOS 10.15.4+

## Declaration

```swift
class IOServiceNotificationDispatchSource : IODispatchSource, IOServiceNotificationDispatchSourceInterface
```

## Topics

### Instance Methods
- [- Cancel](../driverkit/ioservicenotificationdispatchsource/3538743-cancel.md)
- [- Cancel_Impl](ioservicenotificationdispatchsource/3538520-cancel_impl.md)
- [- CheckForWork](../driverkit/ioservicenotificationdispatchsource/3538744-checkforwork.md)
- [- CheckForWork_Impl](ioservicenotificationdispatchsource/3538521-checkforwork_impl.md)
- [- CopyNextNotification](ioservicenotificationdispatchsource/3538522-copynextnotification.md)
- [- CopyNextNotification](../driverkit/ioservicenotificationdispatchsource/3538745-copynextnotification.md)
- [- CopyNextNotification_Impl](ioservicenotificationdispatchsource/3538523-copynextnotification_impl.md)
- [- DeliverNotifications](ioservicenotificationdispatchsource/3538529-delivernotifications.md)
- [- Dispatch](ioservicenotificationdispatchsource/3538530-dispatch.md)
- [- ServiceNotificationReady](ioservicenotificationdispatchsource/3538531-servicenotificationready.md)
- [- ServiceNotificationReady](../driverkit/ioservicenotificationdispatchsource/3538746-servicenotificationready.md)
- [- SetEnableWithCompletion](../driverkit/ioservicenotificationdispatchsource/3538747-setenablewithcompletion.md)
- [- SetEnableWithCompletion_Impl](ioservicenotificationdispatchsource/3538533-setenablewithcompletion_impl.md)
- [- SetHandler](ioservicenotificationdispatchsource/3538534-sethandler.md)
- [- SetHandler](../driverkit/ioservicenotificationdispatchsource/3538748-sethandler.md)
- [- SetHandler_Impl](ioservicenotificationdispatchsource/3538535-sethandler_impl.md)
- [- free](ioservicenotificationdispatchsource/3538537-free.md)
- [- getMetaClass](ioservicenotificationdispatchsource/3538538-getmetaclass.md)
- [- init](ioservicenotificationdispatchsource/3538539-init.md)
### Type Methods
- [+ CopyNextNotification_Invoke](ioservicenotificationdispatchsource/3538524-copynextnotification_invoke.md)
- [+ Create](ioservicenotificationdispatchsource/3538525-create.md)
- [+ Create_Call](ioservicenotificationdispatchsource/3538526-create_call.md)
- [+ Create_Impl](ioservicenotificationdispatchsource/3538527-create_impl.md)
- [+ Create_Invoke](ioservicenotificationdispatchsource/3538528-create_invoke.md)
- [+ ServiceNotificationReady_Invoke](ioservicenotificationdispatchsource/4519996-servicenotificationready_invoke.md)
- [+ ServiceNotificationReady_Invoke](ioservicenotificationdispatchsource/4519997-servicenotificationready_invoke.md)
- [+ SetHandler_Invoke](ioservicenotificationdispatchsource/3538536-sethandler_invoke.md)

## Relationships

### Inherits From
- [IODispatchSource](../driverkit/iodispatchsource.md)
- [IODispatchSource](iodispatchsource.md)
- [IOServiceNotificationDispatchSourceInterface](ioservicenotificationdispatchsourceinterface.md)

## See Also

- [IOServiceNotificationDispatchSourceInterface](ioservicenotificationdispatchsourceinterface.md)
- [IONotifier](ionotifier.md)
  An abstract base class defining common methods for controlling a notification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservicenotificationdispatchsource)*