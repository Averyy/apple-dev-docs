# MDSchema

**Framework**: Core Services  
**Role**: API Collection

## Overview

The MDSchema functions provide information about the metadatareturned for an item including the type of metadata provided fora file type, the localized display name for a metadata attributekey, and the schema for a metadata attribute key.

## Topics

### MDSchema Miscellaneous Functions
- [func MDSchemaCopyAllAttributes() -> CFArray!](../api-1445665-mdschemacopyallattributes.md)
  Returns an array containing all the metadata attributesdefined in the schema.
- [func MDSchemaCopyAttributesForContentType(CFString!) -> CFDictionary!](../api-1444459-mdschemacopyattributesforcontent.md)
  Returns a dictionary containing the metadata attributesfor the specified UTI type.
- [func MDSchemaCopyDisplayDescriptionForAttribute(CFString!) -> CFString!](../api-1442582-mdschemacopydisplaydescriptionfo.md)
  Returns the localized description of a metadata attributekey.
- [func MDSchemaCopyDisplayNameForAttribute(CFString!) -> CFString!](../api-1450203-mdschemacopydisplaynameforattrib.md)
  Returns the localized display name of a metadata attributekey.
- [func MDSchemaCopyMetaAttributesForAttribute(CFString!) -> CFDictionary!](../api-1450052-mdschemacopymetaattributesforatt.md)
  Returns a dictionary describing the values for the specifiedmetadata attribute key.
### Constants
- [Available Metadata Attribute Keys](./mdschema/available_metadata_attribute_keys.md)
  Specify the available metadata attribute keys for a contenttype.
- [Metadata Attribute Schema Description Keys](./mdschema/metadata_attribute_schema_description_keys.md)
  Specify the schema of a metadata attribute key.

## See Also

### Opaque Types
- [MDItem](./mditem.md)
### Related Documentation
- [Spotlight Overview](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html#//apple_ref/doc/uid/TP40001268)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdschema)*