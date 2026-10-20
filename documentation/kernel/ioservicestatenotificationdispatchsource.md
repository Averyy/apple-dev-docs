# IOServiceStateNotificationDispatchSource

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- DriverKit 21.0+
- macOS 12.0+

## Declaration

*DriverKit*

```cpp
class IOServiceStateNotificationDispatchSource : IODispatchSource
```

*macOS*

```cpp
class IOServiceStateNotificationDispatchSource : IODispatchSource, IOServiceStateNotificationDispatchSourceInterface
```

## Topics

### Instance Methods
- [- Cancel](../DriverKit/ioservicestatenotificationdispatchsource/cancel.md)
- [- Cancel_Impl](./ioservicestatenotificationdispatchsource/api-3753350-cancel_impl.md)
- [- Dispatch](./ioservicestatenotificationdispatchsource/api-3753355-dispatch.md)
- [- SetEnableWithCompletion](../DriverKit/ioservicestatenotificationdispatchsource/setenablewithcompletion.md)
- [- SetEnableWithCompletion_Impl](./ioservicestatenotificationdispatchsource/api-3753356-setenablewithcompletion_impl.md)
- [- SetHandler](./ioservicestatenotificationdispatchsource/api-3753357-sethandler.md)
- [- SetHandler](../DriverKit/ioservicestatenotificationdispatchsource/sethandler.md)
- [- SetHandler_Impl](./ioservicestatenotificationdispatchsource/api-3753358-sethandler_impl.md)
- [- StateNotificationBegin](./ioservicestatenotificationdispatchsource/api-3753360-statenotificationbegin.md)
- [- StateNotificationBegin](../DriverKit/ioservicestatenotificationdispatchsource/statenotificationbegin.md)
- [- StateNotificationBegin_Impl](./ioservicestatenotificationdispatchsource/api-3753361-statenotificationbegin_impl.md)
- [- StateNotificationReady](./ioservicestatenotificationdispatchsource/api-3753363-statenotificationready.md)
- [- StateNotificationReady](../DriverKit/ioservicestatenotificationdispatchsource/statenotificationready.md)
- [- free](./ioservicestatenotificationdispatchsource/api-3753366-free.md)
- [- getMetaClass](./ioservicestatenotificationdispatchsource/api-3753367-getmetaclass.md)
- [- init](./ioservicestatenotificationdispatchsource/api-3753368-init.md)
### Type Methods
- [+ Create](./ioservicestatenotificationdispatchsource/api-3753351-create.md)
- [+ Create_Call](./ioservicestatenotificationdispatchsource/api-3753352-create_call.md)
- [+ Create_Impl](./ioservicestatenotificationdispatchsource/api-3753353-create_impl.md)
- [+ Create_Invoke](./ioservicestatenotificationdispatchsource/api-3753354-create_invoke.md)
- [+ SetHandler_Invoke](./ioservicestatenotificationdispatchsource/api-3753359-sethandler_invoke.md)
- [+ StateNotificationBegin_Invoke](./ioservicestatenotificationdispatchsource/api-3753362-statenotificationbegin_invoke.md)
- [+ StateNotificationReady_Invoke](./ioservicestatenotificationdispatchsource/api-4519998-statenotificationready_invoke.md)
- [+ StateNotificationReady_Invoke](./ioservicestatenotificationdispatchsource/api-4519999-statenotificationready_invoke.md)

## Relationships

### Inherits From
- [IODispatchSource](../DriverKit/iodispatchsource.md)
- [IODispatchSource](./iodispatchsource.md)
- [IOServiceStateNotificationDispatchSourceInterface](./ioservicestatenotificationdispatchsourceinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservicestatenotificationdispatchsource)*