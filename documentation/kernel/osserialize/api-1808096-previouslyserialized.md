# previouslySerialized

**Framework**: Kernel  
**Kind**: instm

Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.

## Declaration

```swift
virtual bool previouslySerialized(
 const OSMetaClassBase *object);
```

#### Return_value

`true` if `object` has already been serialized by this OSSerialize object and a reference to it is successfully added to the XML stream, `false` otherwise.

#### Overview

This function both reduces the size of generated XML by emitting shorter references to existing objects with the same value (particularly for OSString, OSSymbol, and OSData), and also preserves instance references so that the user-space I/O Kit library can reconstruct an identical graph of object relationships.

All classes that override OSObject::serialize. should call this function before doing any actual serialization; if it returns `true`, the `serialize` implementation can immediately return `true`.

## Parameters

- `object`: The object to check.

## See Also

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
- [text](osserialize/1808110-text.md)
  Returns the XML text serialized so far.
- [withCapacity](osserialize/1808120-withcapacity.md)
  Creates and initializes an empty OSSerialize object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize/1808096-previouslyserialized)*