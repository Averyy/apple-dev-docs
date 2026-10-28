# iokit_vendor_specific_msg

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```c
#define iokit_vendor_specific_msg(message)
```

## Discussion

iokit_vendor_specific_msg passes messages in the sub_iokit_vendor_specific subsystem. It can be used to generate messages that are used for private communication between vendor specific code with the IOService::message() etc. APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iokit_vendor_specific_msg)*