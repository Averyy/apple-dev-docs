# getProperties

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Used to obtain the properties of the UPS device such as the name and transport.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*getProperties)(void *thisPointer, CFDictionaryRef *properties);
```

## Return Value

An IOReturn error code.

## Discussion

Property keys are defined in IOPSKeys.h. This is not an allocation method. Thus the caller does not release the CFDictionary that is returned.

## Parameters

- `thisPointer`: The UPS Interface to use.
- `properties`: Pointer to a CFDictionaryRef that contains the properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugininterface/1560771-getproperties)*