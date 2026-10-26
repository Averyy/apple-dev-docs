# IOHIDReportCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
typedef void (*IOHIDReportCallback)(void *context, IOReturn result, void *sender, IOHIDReportType type, uint32_t reportID, uint8_t *report, CFIndex reportLength);
```

#### Discussion

Type and arguments of callout C function that is used when a HID report completion routine is called.

## Parameters

- `context`: void * pointer to your data, often a pointer to an object.
- `result`: Completion result of desired operation.
- `refcon`: void * pointer to more data.
- `sender`: Interface instance sending the completion routine.
- `type`: The type of the report that was completed.
- `reportID`: The ID of the report that was completed.
- `report`: Pointer to the buffer containing the contents of the report.
- `reportLength`: Size of the buffer received upon completion.

## See Also

### Callbacks
- [IOHIDCallback](./iohidcallback.md)
- [IOHIDDeviceCallback](./iohiddevicecallback.md)
- [IOHIDValueCallback](./iohidvaluecallback.md)
- [IOHIDValueMultipleCallback](./iohidvaluemultiplecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidreportcallback)*