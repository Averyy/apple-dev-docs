# getCapabilities

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Used to obtain the capabilities of the UPS device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*getCapabilities)(void *thisPointer, CFSetRef *capabilities);
```

## Return Value

An IOReturn error code.

## Discussion

Keys are defined in IOPSKeys.h and begin with kIOPS. This is not an allocation method. Thus the caller does not release the CFSet that is returned.

## Parameters

- `thisPointer`: The UPS Interface to use.
- `capabilities`: Pointer to a CFSetRef that contains the capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugininterface/1560784-getcapabilities)*