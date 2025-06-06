# MDSchemaCopyDisplayNameForAttribute(_:)

**Framework**: Core Services  
**Kind**: func

Returns the localized display name of a metadata attributekey.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDSchemaCopyDisplayNameForAttribute(_ name: CFString!) -> CFString!
```

#### Return_value

The localized displayname of the metadata attribute, or `NULL` ifno localized display name is available.

## Parameters

- `name`: The name of the metadata attribute key.

## See Also

- [func MDSchemaCopyAllAttributes() -> CFArray!](1445665-mdschemacopyallattributes.md)
  Returns an array containing all the metadata attributesdefined in the schema.
- [func MDSchemaCopyAttributesForContentType(CFString!) -> CFDictionary!](1444459-mdschemacopyattributesforcontent.md)
  Returns a dictionary containing the metadata attributesfor the specified UTI type.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450203-mdschemacopydisplaynameforattrib)*