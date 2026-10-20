# addXMLStartTag

**Framework**: Kernel  
**Kind**: instm

Appends an XML start tag to the XML stream.

## Declaration

```cpp
virtual bool addXMLStartTag( 
 const OSMetaClassBase *object, 
 const char *tagString);
```

#### Return Value

`true` if an XML start tag for `tagString` is successfully added to the XML stream, `false` otherwise.

#### Overview

This function emits the named tag, enclosed within a pair of angle brackets.

A class that implements serialization should call this function with the name of the XML tag that best represents the serialized contents of the object. A limited number of tags are supported by the user-space I/O Kit library:

- array
- dict
- integer
- key
- set
- string

A call to this function must be balanced with one to addXMLEndTag using the same `tagString`.

## Parameters

- `object`: The object being serialized.
- `tagString`: The name of the XML tag to emit; for example, "string".

## See Also

### Miscellaneous
- [addChar](./api-1808034-addchar.md)
  Appends a single character to the XML stream.
- [addString](./api-1808045-addstring.md)
  Appends a C string to the XML stream.
- [addXMLEndTag](./api-1808061-addxmlendtag.md)
  Appends an XML end tag to the XML stream.
- [clearText](./api-1808086-cleartext.md)
  Resets the OSSerialize object.
- [previouslySerialized](./api-1808096-previouslyserialized.md)
  Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.
- [text](./api-1808110-text.md)
  Returns the XML text serialized so far.
- [withCapacity](./api-1808120-withcapacity.md)
  Creates and initializes an empty OSSerialize object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize/1808073-addxmlstarttag)*