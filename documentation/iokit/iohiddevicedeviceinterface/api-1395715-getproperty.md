# getProperty

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains a property related to the IOHIDDevice.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getProperty)(void *self, CFStringRef key, CFTypeRef *pProperty);
```

#### Return Value

Returns kIOReturnSuccess if successful.

#### Discussion

Property keys are prefixed by kIOHIDDevice and declared in IOHIDKeys.h.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `key`: CFStringRef key
- `pProperty`: Pointer to a CFTypeRef property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395715-getproperty)*