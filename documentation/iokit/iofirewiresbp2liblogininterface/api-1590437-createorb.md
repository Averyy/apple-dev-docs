# createORB

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates a new IOFireWireSBP2ORB for this login.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IUnknownVTbl **(*createORB)(void *self, REFIID iid);
```

#### Return Value

Returns a pointer to the new ORB object.

#### Discussion

Create a new IOFireWireSBP2ORB for this login. It can be configured with it's accessors and executed with submitORB below.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `iid`: UUID for the desired type of IOFireWireSBP2LibLoginInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590437-createorb)*