# getEvent

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Used to poll the current state of the UPS.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*getEvent)(void *thisPointer, CFDictionaryRef *event);
```

## Return Value

An IOReturn error code.

## Discussion

Keys are defined in IOPSKeys.h and begin with kIOPS. This is not an allocation method. Thus the caller does not release the CFDictionary that is returned.

## Parameters

- `thisPointer`: The UPS Interface to use.
- `event`: Pointer to a CFDictionaryRef that contains the current event state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugininterface/1560762-getevent)*