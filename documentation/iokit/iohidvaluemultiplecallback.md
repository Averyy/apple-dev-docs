# IOHIDValueMultipleCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
typedef void (*IOHIDValueMultipleCallback)(void *context, IOReturn result, void *sender, CFDictionaryRef multiple);
```

## Discussion

Type and arguments of callout C function that is used when an element value completion routine is called.

## Parameters

- `context`: void * pointer to more data.
- `result`: Completion result of desired operation.
- `sender`: Interface instance sending the completion routine.
- `multiple`: CFDictionaryRef containing the returned element key value pairs.

## See Also

### Callbacks
- [IOHIDCallback](./iohidcallback.md)
- [IOHIDDeviceCallback](./iohiddevicecallback.md)
- [IOHIDReportCallback](./iohidreportcallback.md)
- [IOHIDValueCallback](./iohidvaluecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidvaluemultiplecallback)*