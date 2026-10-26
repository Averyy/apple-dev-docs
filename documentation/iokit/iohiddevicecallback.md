# IOHIDDeviceCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
typedef void (*IOHIDDeviceCallback)(void *context, IOReturn result, void *sender, IOHIDDeviceRef device);
```

#### Discussion

Type and arguments of callout C function that is used when a device routine is called.

## Parameters

- `context`: void * pointer to more data.
- `result`: Completion result of desired operation.
- `device`: IOHIDDeviceRef containing the sending device.

## See Also

### Callbacks
- [IOHIDCallback](./iohidcallback.md)
- [IOHIDReportCallback](./iohidreportcallback.md)
- [IOHIDValueCallback](./iohidvaluecallback.md)
- [IOHIDValueMultipleCallback](./iohidvaluemultiplecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicecallback)*