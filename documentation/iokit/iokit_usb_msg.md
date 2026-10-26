# iokit_usb_msg

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define iokit_usb_msg(message)
```

#### Discussion

Messages specific to the IOUSBFamily. Note that the iokit_usb_msg(x) translates to 0xe0004xxx, where xxx is the value in parenthesis as a hex number.

## See Also

### UNKNOWN OBJECT 
- [iokit_usb_err](./iokit_usb_err.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iokit_usb_msg)*