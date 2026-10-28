# getLoginID

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the current login ID.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 (*getLoginID)(void *self);
```

## Return Value

Returns a UInt32 containing the current login ID.

## Discussion

When we successfully login to a device. The device gives us a unique login id. This is used internally for reconnecting to the device after bus resets and for certain other management ORBs. Most drivers are probably not interested in this value.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590456-getloginid)*