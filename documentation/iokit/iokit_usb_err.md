# iokit_usb_err

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define iokit_usb_err(return)
```

## Discussion

Errors specific to the IOUSBFamily. Note that the iokit_usb_err(x) translates to 0xe0004xxx, where xxx is the value in parenthesis as a hex number.

## See Also

### UNKNOWN OBJECT 
- [iokit_usb_msg](./iokit_usb_msg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iokit_usb_err)*