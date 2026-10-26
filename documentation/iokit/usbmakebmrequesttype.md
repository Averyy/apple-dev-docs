# USBmakebmRequestType

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define USBmakebmRequestType(direction, type, recipient)
```

#### Discussion

Macro to encode the bRequest field of a Device Request. It is used when constructing an IOUSBDevRequest.

## See Also

### Miscellaneous
- [EncodeRequest](./encoderequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbmakebmrequesttype)*