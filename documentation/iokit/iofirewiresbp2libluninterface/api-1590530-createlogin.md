# createLogin

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates a new IOFireWireSBP2LibLoginInterface object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IUnknownVTbl **(*createLogin)(void *self, REFIID iid);
```

#### Return Value

Returns a pointer to a new IOFireWireSBP2LibLoginInterface.

#### Discussion

Creates a new IOFireWireSBP2LibLoginInterface object for the LUN. Login objects supply most of the SBP2 APIs related to login maintenance and Normal Command ORB execution.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.
- `iid`: UUID for desired type of IOFireWireSBP2LibLoginInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590530-createlogin)*