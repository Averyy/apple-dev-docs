# getSessionRef

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Get the session reference.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOFireWireSessionRef (*getSessionRef)(void *self);
```

#### Return Value

Returns a sessionRef on success.

#### Discussion

Gets the sessionRef to be used with openWithSessionRef.

## Parameters

- `self`: Pointer to IOFireWireAVCLibUnitInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508859-getsessionref)*