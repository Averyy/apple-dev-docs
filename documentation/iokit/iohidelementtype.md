# IOHIDElementType

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

Describes different types of HID elements.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef enum IOHIDElementType : unsigned int {
    ...
} IOHIDElementType;
```

#### Overview

Used by the IOHIDFamily to identify the type of element processed. Represented by the key kIOHIDElementTypeKey in the dictionary describing the element.

## Topics

### Constants
- [kIOHIDElementTypeInput_Misc](./iohidelementtype/kiohidelementtypeinput_misc.md)
- [kIOHIDElementTypeInput_Button](./iohidelementtype/kiohidelementtypeinput_button.md)
- [kIOHIDElementTypeInput_Axis](./iohidelementtype/kiohidelementtypeinput_axis.md)
- [kIOHIDElementTypeInput_ScanCodes](./iohidelementtype/kiohidelementtypeinput_scancodes.md)
- [kIOHIDElementTypeOutput](./iohidelementtype/kiohidelementtypeoutput.md)
- [kIOHIDElementTypeFeature](./iohidelementtype/kiohidelementtypefeature.md)
- [kIOHIDElementTypeCollection](./iohidelementtype/kiohidelementtypecollection.md)
- [kIOHIDElementTypeInput_NULL](./iohidelementtype/kiohidelementtypeinput_null.md)

## See Also

### Related Documentation
- [IOHIDElementType](./iohidelementtype.md)
  Describes different types of HID elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidelementtype)*