# IONotifier

**Framework**: Kernel  
**Kind**: cl

An abstract base class defining common methods for controlling a notification request.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IONotifier : OSObject
```

#### Overview

IOService notification requests are represented as implementations of the IONotifier object. It defines methods to enable, disable and remove notification requests. These actions are synchronized with invocations of the notification handler, so removing a notification request will guarantee the handler is not being executed.

## Topics

### Miscellaneous
- [disable](ionotifier/1810461-disable.md)
  Disables the notification request.
- [enable](ionotifier/1810483-enable.md)
  Sets the enable state of the notification request.
- [remove](ionotifier/1810524-remove.md)
  Removes the notification request and releases it.
### Instance Methods
- [- disable](ionotifier/1529198-disable.md)
- [- enable](ionotifier/1529202-enable.md)
- [- getMetaClass](ionotifier/1529206-getmetaclass.md)
- [- remove](ionotifier/1529200-remove.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOServiceNotificationDispatchSource](ioservicenotificationdispatchsource.md)
- [IOServiceNotificationDispatchSourceInterface](ioservicenotificationdispatchsourceinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionotifier)*