# setResponseBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the response buffer for the management ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setResponseBuffer)(void *self, void *buf, UInt32 len);
```

## Return Value

Returns kIOReturnSuccess on a success.

## Discussion

Sets the response buffer for the management ORB. kFWSBP2QueryLogins returns a response to its query and needs to write it somewhere. This routine allows you to specify the location.

## Parameters

- `self`: Pointer to a IOFireWireSBP2LibMgmtORBInterface.
- `buf`: backing store for buffer
- `len`: length of buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libmgmtorbinterface/1590532-setresponsebuffer)*