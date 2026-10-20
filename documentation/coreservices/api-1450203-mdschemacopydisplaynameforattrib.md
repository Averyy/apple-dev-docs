# MDSchemaCopyDisplayNameForAttribute(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the localized display name of a metadata attributekey.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDSchemaCopyDisplayNameForAttribute(_ name: CFString!) -> CFString!
```

```c
CFStringRef MDSchemaCopyDisplayNameForAttribute(CFStringRef name);
```

#### Return Value

The localized displayname of the metadata attribute, or `NULL` ifno localized display name is available.

## Parameters

- `name`: The name of the metadata attribute key.

## See Also

### MDSchema Miscellaneous Functions
- [func MDSchemaCopyAllAttributes() -> CFArray!](./api-1445665-mdschemacopyallattributes.md)
  Returns an array containing all the metadata attributesdefined in the schema.
- [func MDSchemaCopyAttributesForContentType(CFString!) -> CFDictionary!](./api-1444459-mdschemacopyattributesforcontent.md)
  Returns a dictionary containing the metadata attributesfor the specified UTI type.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](./api-1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](./api-1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450203-mdschemacopydisplaynameforattrib)*