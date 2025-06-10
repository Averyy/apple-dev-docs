# IOHIDElementType

**Framework**: Kernel  
**Kind**: tdef

Describes different types of HID elements.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef enum IOHIDElementType IOHIDElementType;
```

#### Discussion

Used by the IOHIDFamily to identify the type of element processed. Represented by the key kIOHIDElementTypeKey in the dictionary describing the element.

## Topics

### Constants
- [kIOHIDElementTypeInput_Misc](iohidelementtype/kiohidelementtypeinput_misc.md)
- [kIOHIDElementTypeInput_Button](iohidelementtype/kiohidelementtypeinput_button.md)
- [kIOHIDElementTypeInput_Axis](iohidelementtype/kiohidelementtypeinput_axis.md)
- [kIOHIDElementTypeInput_ScanCodes](iohidelementtype/kiohidelementtypeinput_scancodes.md)
- [kIOHIDElementTypeOutput](iohidelementtype/kiohidelementtypeoutput.md)
- [kIOHIDElementTypeFeature](iohidelementtype/kiohidelementtypefeature.md)
- [kIOHIDElementTypeCollection](iohidelementtype/kiohidelementtypecollection.md)
- [kIOHIDElementTypeInput_NULL](iohidelementtype/kiohidelementtypeinput_null.md)

## See Also

- [IOHIDElementCollectionType](iohidelementcollectiontype.md)
  Describes different types of HID collections.
- [IOHIDElementCommitDirection](iohidelementcommitdirection.md)
- [IOHIDElementCookie](iohidelementcookie.md)
  Abstract data type used as a unique identifier for an element.
- [IOHIDElementFlags](iohidelementflags.md)
- [IOHIDValueOptions](iohidvalueoptions.md)
  Describes options for gathering element values.
- [IOHIDElementType](../iokit/iohidelementtype.md)
  Describes different types of HID elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidelementtype)*