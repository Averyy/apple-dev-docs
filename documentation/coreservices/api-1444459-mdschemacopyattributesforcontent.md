# MDSchemaCopyAttributesForContentType(_:)

**Framework**: Core Services  
**Kind**: func

Returns a dictionary containing the metadata attributesfor the specified UTI type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDSchemaCopyAttributesForContentType(_ contentTypeUTI: CFString!) -> CFDictionary!
```

#### Return_value

A dictionary containing `kMDAttributeDisplayValues` and `kMDAttributeAllValues` keys.Returns `NULL` if the UTItype is unknown.

#### Discussion

This function returns the metadata attributes for the specifiedUTI type only.

## Parameters

- `utiType`: The UTI type.

## See Also

- [func MDSchemaCopyAllAttributes() -> CFArray!](1445665-mdschemacopyallattributes.md)
  Returns an array containing all the metadata attributesdefined in the schema.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyDisplayNameForAttribute(CFString!) -> CFString!](1450203-mdschemacopydisplaynameforattrib.md)
  Returns the localized display name of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444459-mdschemacopyattributesforcontent)*