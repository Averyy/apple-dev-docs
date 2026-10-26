# copyMatchingElements

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains a CFArrayRef containing the IOHIDDeviceDeviceInterface elements that match the passed matching dictionary.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*copyMatchingElements)(void *self, CFDictionaryRef matchingDict, CFArrayRef *pElements, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

Objects contained in the returned array are of type IOHIDElementRef. Please see IOHIDElement.h for additional API information. Elemenet properties are prefixed by kIOHIDElement and declared in IOHIDKeys.h.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `matchingDict`: CFDictionaryRef containing the element properties to match on.
- `pElements`: CFArrayRef containing matched elements.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395733-copymatchingelements)*