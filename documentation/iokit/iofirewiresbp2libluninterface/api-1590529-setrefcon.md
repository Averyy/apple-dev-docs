# setRefCon

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the ORB refCon.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setRefCon)(void *self, void *refCon);
```

## Discussion

Sets a user defined value on the ORB that can be retrieved later with the method getRefCon.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.
- `refCon`: a user defined value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590529-setrefcon)*