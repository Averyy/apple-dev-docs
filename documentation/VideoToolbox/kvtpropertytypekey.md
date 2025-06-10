# kVTPropertyTypeKey

**Framework**: Video Toolbox  
**Kind**: var

Dictionary key used to access the property type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTPropertyTypeKey: CFString
```

#### Discussion

The associated value will be either [`kVTPropertyType_Boolean`](kvtpropertytype_boolean.md), [`kVTPropertyType_Enumeration`](kvtpropertytype_enumeration.md), or [`kVTPropertyType_Number`](kvtpropertytype_number.md).

## See Also

- [Property Type Constants](property-type-constants.md)
  Supported constant values for `kVTPropertyTypeKey`.
- [let kVTPropertyReadWriteStatusKey: CFString](kvtpropertyreadwritestatuskey.md)
  Dictionary key to access the read/write status of a property.
- [Read/Write Status Constants](read-write-status-constants.md)
  Supported constant values for `kVTPropertyReadWriteStatusKey`.
- [let kVTPropertyShouldBeSerializedKey: CFString](kvtpropertyshouldbeserializedkey.md)
  Dictionary key to access the serializable status of a property.
- [let kVTPropertySupportedValueListKey: CFString](kvtpropertysupportedvaluelistkey.md)
  Dictionary key to access the array of of supported values.
- [let kVTPropertySupportedValueMaximumKey: CFString](kvtpropertysupportedvaluemaximumkey.md)
  Dictionary key to access the maximum value of a property.
- [let kVTPropertySupportedValueMinimumKey: CFString](kvtpropertysupportedvalueminimumkey.md)
  Dictionary key to access the minimum value of a property.
- [let kVTPropertyDocumentationKey: CFString](kvtpropertydocumentationkey.md)
  Dictionary key to access any documentation intended for developers only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtpropertytypekey)*