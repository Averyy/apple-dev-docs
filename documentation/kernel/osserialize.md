# OSSerialize

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

OSSerialize coordinates serialization of Libkern C++ objects into an XML stream.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class OSSerialize : OSObject
```

## Overview

This class is for the most part internal to the OSContainer classes, used for transferring property tables between the kernel and user space. It should not be used directly. Classes that participate in serialization override the OSObject::serialize . function.

**Use Restrictions**

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are **unsafe** to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSerialize provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for serializing properties.

## Topics

### Miscellaneous
- [addChar](./osserialize/api-1808034-addchar.md)
  Appends a single character to the XML stream.
- [addString](./osserialize/api-1808045-addstring.md)
  Appends a C string to the XML stream.
- [addXMLEndTag](./osserialize/api-1808061-addxmlendtag.md)
  Appends an XML end tag to the XML stream.
- [addXMLStartTag](./osserialize/api-1808073-addxmlstarttag.md)
  Appends an XML start tag to the XML stream.
- [clearText](./osserialize/api-1808086-cleartext.md)
  Resets the OSSerialize object.
- [previouslySerialized](./osserialize/api-1808096-previouslyserialized.md)
  Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.
- [text](./osserialize/api-1808110-text.md)
  Returns the XML text serialized so far.
- [withCapacity](./osserialize/api-1808120-withcapacity.md)
  Creates and initializes an empty OSSerialize object.
### Instance Methods
- [- addBinary](./osserialize/api-1575019-addbinary.md)
- [- addBinaryObject](./osserialize/api-1575027-addbinaryobject.md)
- [- addChar](./osserialize/api-1575032-addchar.md)
- [- addString](./osserialize/api-1575014-addstring.md)
- [- addXMLEndTag](./osserialize/api-1575029-addxmlendtag.md)
- [- addXMLStartTag](./osserialize/api-1575026-addxmlstarttag.md)
- [- binarySerialize](./osserialize/api-1575017-binaryserialize.md)
- [- binarySerializeInternal](./osserialize/api-3075326-binaryserializeinternal.md)
- [- clearText](./osserialize/api-1575024-cleartext.md)
- [- endBinaryCollection](./osserialize/api-3075327-endbinarycollection.md)
- [- ensureCapacity](./osserialize/api-1575028-ensurecapacity.md)
- [- free](./osserialize/api-1575020-free.md)
- [- getCapacity](./osserialize/api-1575030-getcapacity.md)
- [- getCapacityIncrement](./osserialize/api-1575031-getcapacityincrement.md)
- [- getLength](./osserialize/api-1575012-getlength.md)
- [- getMetaClass](./osserialize/api-1575013-getmetaclass.md)
- [- initWithCapacity](./osserialize/api-1575023-initwithcapacity.md)
- [- previouslySerialized](./osserialize/api-1575018-previouslyserialized.md)
- [- setCapacityIncrement](./osserialize/api-1575007-setcapacityincrement.md)
- [- setIndexed](./osserialize/api-3075328-setindexed.md)
- [- text](./osserialize/api-1575016-text.md)
### Type Methods
- [+ binaryWithCapacity](./osserialize/api-1575009-binarywithcapacity.md)
- [+ withCapacity](./osserialize/api-1575022-withcapacity.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

## See Also

### Serialization
- [OSSerializer](./osserializer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize)*