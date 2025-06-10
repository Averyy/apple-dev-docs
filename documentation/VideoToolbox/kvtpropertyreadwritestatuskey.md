# kVTPropertyReadWriteStatusKey

**Framework**: Video Toolbox  
**Kind**: var

Dictionary key to access the read/write status of a property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTPropertyReadWriteStatusKey: CFString
```

#### Discussion

The associated value will be either [`kVTPropertyReadWriteStatus_ReadOnly`](kvtpropertyreadwritestatus_readonly.md) or  [`kVTPropertyReadWriteStatus_ReadWrite`](kvtpropertyreadwritestatus_readwrite.md).

## See Also

- [let kVTPropertyTypeKey: CFString](kvtpropertytypekey.md)
  Dictionary key used to access the property type.
- [Property Type Constants](property-type-constants.md)
  Supported constant values for `kVTPropertyTypeKey`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtpropertyreadwritestatuskey)*