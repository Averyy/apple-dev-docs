# IOHIDCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
typedef void (*IOHIDCallback)(void *context, IOReturn result, void *sender);
```

#### Discussion

Type and arguments of callout C function that is used when a completion routine is called.

## Parameters

- `context`: void * pointer to your data, often a pointer to an object.
- `result`: Completion result of desired operation.
- `refcon`: void * pointer to more data.
- `sender`: Interface instance sending the completion routine.

## See Also

### Callbacks
- [IOHIDDeviceCallback](./iohiddevicecallback.md)
- [IOHIDReportCallback](./iohidreportcallback.md)
- [IOHIDValueCallback](./iohidvaluecallback.md)
- [IOHIDValueMultipleCallback](./iohidvaluemultiplecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidcallback)*