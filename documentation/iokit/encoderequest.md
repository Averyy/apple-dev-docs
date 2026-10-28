# EncodeRequest

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define EncodeRequest(request, direction, type, recipient)
```

## Discussion

Macro that encodes the bRequest and bRequestType fields of a IOUSBDevRequest into a single value. It is useful when one needs to know what type of request the IOUSBDevRequest encodes and simplifies comparisons.

## See Also

### Miscellaneous
- [USBmakebmRequestType](./usbmakebmrequesttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/encoderequest)*