# OSSerialize

**Framework**: Kernel  
**Kind**: cl

OSSerialize coordinates serialization of Libkern C++ objects into an XML stream.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSSerialize : OSObject
```

#### Overview

This class is for the most part internal to the OSContainer classes, used for transferring property tables between the kernel and user space. It should not be used directly. Classes that participate in serialization override the OSObject::serialize . function.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSerialize provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for serializing properties.

## Topics

### Miscellaneous
- [addChar](osserialize/1808034-addchar.md)
  Appends a single character to the XML stream.
- [addString](osserialize/1808045-addstring.md)
  Appends a C string to the XML stream.
- [addXMLEndTag](osserialize/1808061-addxmlendtag.md)
  Appends an XML end tag to the XML stream.
- [addXMLStartTag](osserialize/1808073-addxmlstarttag.md)
  Appends an XML start tag to the XML stream.
- [clearText](osserialize/1808086-cleartext.md)
  Resets the OSSerialize object.
- [previouslySerialized](osserialize/1808096-previouslyserialized.md)
  Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.
- [text](osserialize/1808110-text.md)
  Returns the XML text serialized so far.
- [withCapacity](osserialize/1808120-withcapacity.md)
  Creates and initializes an empty OSSerialize object.
### Instance Methods
- [- addBinary](osserialize/1575019-addbinary.md)
- [- addBinaryObject](osserialize/1575027-addbinaryobject.md)
- [- addChar](osserialize/1575032-addchar.md)
- [- addString](osserialize/1575014-addstring.md)
- [- addXMLEndTag](osserialize/1575029-addxmlendtag.md)
- [- addXMLStartTag](osserialize/1575026-addxmlstarttag.md)
- [- binarySerialize](osserialize/1575017-binaryserialize.md)
- [- binarySerializeInternal](osserialize/3075326-binaryserializeinternal.md)
- [- clearText](osserialize/1575024-cleartext.md)
- [- endBinaryCollection](osserialize/3075327-endbinarycollection.md)
- [- ensureCapacity](osserialize/1575028-ensurecapacity.md)
- [- free](osserialize/1575020-free.md)
- [- getCapacity](osserialize/1575030-getcapacity.md)
- [- getCapacityIncrement](osserialize/1575031-getcapacityincrement.md)
- [- getLength](osserialize/1575012-getlength.md)
- [- getMetaClass](osserialize/1575013-getmetaclass.md)
- [- initWithCapacity](osserialize/1575023-initwithcapacity.md)
- [- previouslySerialized](osserialize/1575018-previouslyserialized.md)
- [- setCapacityIncrement](osserialize/1575007-setcapacityincrement.md)
- [- setIndexed](osserialize/3075328-setindexed.md)
- [- text](osserialize/1575016-text.md)
### Type Methods
- [+ binaryWithCapacity](osserialize/1575009-binarywithcapacity.md)
- [+ withCapacity](osserialize/1575022-withcapacity.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSSerializer](osserializer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize)*