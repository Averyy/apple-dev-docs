# MDSchemaCopyAllAttributes()

**Framework**: Core Services  
**Kind**: func

Returns an array containing all the metadata attributesdefined in the schema.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDSchemaCopyAllAttributes() -> CFArray!
```

## See Also

- [func MDSchemaCopyAttributesForContentType(CFString!) -> CFDictionary!](1444459-mdschemacopyattributesforcontent.md)
  Returns a dictionary containing the metadata attributesfor the specified UTI type.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyDisplayNameForAttribute(CFString!) -> CFString!](1450203-mdschemacopydisplaynameforattrib.md)
  Returns the localized display name of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445665-mdschemacopyallattributes)*