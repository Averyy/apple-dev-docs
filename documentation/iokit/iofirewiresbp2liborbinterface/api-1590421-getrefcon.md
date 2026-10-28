# getRefCon

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the refCon set with setRefCon.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void *(*getRefCon)(void *self);
```

## Return Value

Returns the previously stored user defined value.

## Discussion

Returns the user defined value previously stored in the ORB with setRefCon.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590421-getrefcon)*