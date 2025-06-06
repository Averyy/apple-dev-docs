# Metadata Attribute Schema Description Keys

**Framework**: Core Services

Specify the schema of a metadata attribute key.

#### Overview

These keys are in the dictionary returned by the function `MDSchemaCopyMetaAttributesForAttribute`.

## Topics

### Constants
- [let kMDAttributeName: CFString!](kmdattributename.md)
  A string containing the name of the metadataattribute key.
- [let kMDAttributeType: CFString!](kmdattributetype.md)
  A CFNumberRef or CFTypeId describing thetype of data returned as the value of the metadata attribute key.
- [let kMDAttributeMultiValued: CFString!](kmdattributemultivalued.md)
  A boolean that indicates if the metadataattribute value is multi-valued. If this is `TRUE`,the metadata attribute value is an array of the types specifiedin `kMDAttributeType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdschema/metadata_attribute_schema_description_keys)*