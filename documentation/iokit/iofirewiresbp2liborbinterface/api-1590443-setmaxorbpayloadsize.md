# setMaxORBPayloadSize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets max payload size for the ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setMaxORBPayloadSize)(void *self, UInt32 size);
```

## Discussion

This sets the maximum payload size for this ORB only. This size is clipped by the global max payload size set in the login object.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.
- `size`: The maximum payload size in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590443-setmaxorbpayloadsize)*