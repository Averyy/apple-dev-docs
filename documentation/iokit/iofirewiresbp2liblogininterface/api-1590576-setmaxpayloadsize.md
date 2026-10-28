# setMaxPayloadSize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the maximum data transfer length for a normal command ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setMaxPayloadSize)(void *self, UInt32 size);
```

## Discussion

Sets the maximum data transfer length for a normal command ORB. This value is the maximum for all ORBs sent to this LUN. This can be trimmed further on an ORB by ORB basis, by a similar call in the IOFireWireSBP2ORB itself.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `size`: The desired maximum payload size in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590576-setmaxpayloadsize)*