# MDSchemaCopyAllAttributes()

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns an array containing all the metadata attributesdefined in the schema.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDSchemaCopyAllAttributes() -> CFArray!
```

```c
CFArrayRef MDSchemaCopyAllAttributes(void);
```

## See Also

### MDSchema Miscellaneous Functions
- [func MDSchemaCopyAttributesForContentType(CFString!) -> CFDictionary!](./api-1444459-mdschemacopyattributesforcontent.md)
  Returns a dictionary containing the metadata attributesfor the specified UTI type.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](./api-1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyDisplayNameForAttribute(CFString!) -> CFString!](./api-1450203-mdschemacopydisplaynameforattrib.md)
  Returns the localized display name of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](./api-1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445665-mdschemacopyallattributes)*