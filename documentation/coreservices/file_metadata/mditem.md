# MDItem

**Framework**: Core Services

#### Overview

MDItem is a CF-compliant object that represents a file andthe metadata associated with the file.

For functions that expect an MDItemRef parameter, if thisparameter is not a valid MDItemRef, the behavior is undefined. `NULL` isnot a valid MDItemRef. 

## Topics

### Creating an MDItem
- [func MDItemCreate(CFAllocator!, CFString!) -> MDItem!](1426917-mditemcreate.md)
  Creates an MDItem object for a file at the specified path.
- [func MDItemCreateWithURL(CFAllocator!, CFURL!) -> MDItem!](1427034-mditemcreatewithurl.md)
  Creates an MDItem object for a file at the specified file URL.
### Getting the Type Identifier
- [func MDItemGetTypeID() -> CFTypeID](1427168-mditemgettypeid.md)
  Returns the type identifier of all MDItem instances.
### Retrieving Metadata Attributes 
- [func MDItemCopyAttribute(MDItem!, CFString!) -> CFTypeRef!](1427080-mditemcopyattribute.md)
  Returns the value of the specified attribute in the metadata item.
- [func MDItemCopyAttributes(MDItem!, CFArray!) -> CFDictionary!](1426980-mditemcopyattributes.md)
  Returns the values of the specified attributes in the metadata item.
- [func MDItemCopyAttributeNames(MDItem!) -> CFArray!](1427066-mditemcopyattributenames.md)
  Returns an array containing the attribute names existing in the metadata item.
### Data Types
- [class MDItem](mditem.md)
  A reference to a MDItem object.
### Constants
- [Common Metadata Attribute Keys](file_metadata/mditem/common_metadata_attribute_keys.md)
  Metadata attribute keys that are common to many file types.
- [Image Metadata Attribute Keys](file_metadata/mditem/image_metadata_attribute_keys.md)
  Metadata attribute keys that are common to image files.
- [Video Metadata Attribute Keys](file_metadata/mditem/video_metadata_attribute_keys.md)
  Metadata attribute keys that are common to video files.
- [Audio Metadata Attribute Keys](file_metadata/mditem/audio_metadata_attribute_keys.md)
  Metadata attribute keys that describe an audio file.
- [File System Metadata Attribute Keys](file_metadata/mditem/file_system_metadata_attribute_keys.md)
  Metadata attribute keys that describe the file system attributes for a file.

## See Also

- [MDSchema](file_metadata/mdschema.md)
- [Spotlight Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html#//apple_ref/doc/uid/TP40001268)
- [File Metadata Search Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
- [Spotlight Importer Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html#//apple_ref/doc/uid/TP40001267)
- [File Metadata Attributes Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/MetadataAttrRef.html#//apple_ref/doc/uid/TP40001689)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mditem)*