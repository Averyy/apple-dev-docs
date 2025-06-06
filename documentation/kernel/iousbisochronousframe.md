# IOUSBIsochronousFrame

**Framework**: Kernel  
**Kind**: struct

A structure representing a single frame in an isochronous transfer.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typedef struct IOUSBIsochronousFrame {
    ...
} IOUSBIsochronousFrame;
```

## Topics

### Getting the Frame Properties
- [status](iousbisochronousframe/3294856-status.md)
  The completion status for this individual frame.
- [requestCount](iousbisochronousframe/3294855-requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](iousbisochronousframe/3294854-completecount.md)
  The number of bytes that the system actually transferred for this frame.
- [reserved](iousbisochronousframe/3377598-reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/3294857-timestamp.md)
  The frame’s observed completion time.

## See Also

- [USB Device Descriptors](hardware_families/usb/usb_device_descriptors.md)
  Structures and functions for working with device descriptors.
- [Additional Specifications](hardware_families/usb/additional_specifications.md)
  Structures related to hubs, devices, and endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisochronousframe)*