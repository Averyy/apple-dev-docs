# Numeric Descriptor Type Constants

**Framework**: Core Services

Specify types for numeric descriptors.

#### Overview

The constants described here specify the data type for a descriptor and show the kind of numeric data stored in a descriptor with that type. These constants are preferred over their older equivalents described in `typeSMInt`.

Descriptors are the building blocks used by the Apple Event Manager to construct Apple event attributes and parameters. A descriptor is a data structure of type [`AEDesc`](aedesc.md), which consists of data storage and a descriptor type that identifies the type of the data. A descriptor type is defined by the data type [`DescType`](desctype.md). 

AppleScript defines descriptor type constants for a wide variety of common data types. For additional types, see [`Descriptor Type Constants`](apple_events/1542788-descriptor_type_constants.md) and [`Other Descriptor Type Constants`](apple_events/1542760-other_descriptor_type_constants.md). For a complete listing, including data types such as units of length, weight, and volume, see the Apple Event Manager and Open Scripting Architecture header files. 

## Topics

### Constants
- [var typeSInt16: DescType](typesint16.md)
  16-bit signed integer.
- [var typeUInt16: DescType](typeuint16.md)
  16-bit unsigned integer.
- [var typeSInt32: DescType](typesint32.md)
  32-bit signed integer.
- [var typeUInt32: DescType](typeuint32.md)
  32-bit unsigned integer.
- [var typeSInt64: DescType](typesint64.md)
  64-bit signed integer.
- [var typeUInt64: DescType](typeuint64.md)
  64-bit unsigned integer.
- [var typeIEEE32BitFloatingPoint: DescType](typeieee32bitfloatingpoint.md)
  32-bit floating point value.
- [var typeIEEE64BitFloatingPoint: DescType](typeieee64bitfloatingpoint.md)
  64-bit floating point value.
- [var type128BitFloatingPoint: DescType](type128bitfloatingpoint.md)
  128-bit floating point value.
- [var typeDecimalStruct: DescType](typedecimalstruct.md)
  Decimal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1542872-numeric_descriptor_type_constant)*