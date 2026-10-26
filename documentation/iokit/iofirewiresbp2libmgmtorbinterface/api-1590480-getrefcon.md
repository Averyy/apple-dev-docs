# getRefCon

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the current function of the management ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void *(*getRefCon)(void *self);
```

#### Return Value

Returns the function of the management ORB.

#### Discussion

Returns the function of the management ORB. This is the same value that was set with setCommandFunction.

## Parameters

- `self`: Pointer to a IOFireWireSBP2LibMgmtORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libmgmtorbinterface/1590480-getrefcon)*