# Available Metadata Attribute Keys

**Framework**: Core Services

Specify the available metadata attribute keys for a contenttype.

#### Overview

These keys are in the dictionary returned by the function `MDSchemaCopyAttributesForContentType`.

## Topics

### Constants
- [let kMDAttributeDisplayValues: CFString!](kmdattributedisplayvalues.md)
  An array of strings containing the availabledisplay metadata attribute keys, or `NULL` ifthe type is not known by the system.
- [let kMDAttributeAllValues: CFString!](kmdattributeallvalues.md)
  An array of strings containing the availablemetadata attribute keys, or `NULL` ifthe type is not known by the system.
- [let kMDAttributeReadOnlyValues: CFString!](kmdattributereadonlyvalues.md)
  An array of strings containing the read-onlymetadata attribute keys, or `NULL` ifthe type is not known by the system.
- [let kMDExporterAvaliable: CFString!](kmdexporteravaliable.md)
  A CFBoolean that indicates if an exporter is available for this UTI type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdschema/available_metadata_attribute_keys)*