# clearText

**Framework**: Kernel  
**Kind**: instm

Resets the OSSerialize object.

## Declaration

```cpp
virtual void clearText();
```

#### Overview

This function is a useful optimization if you are serializing the same object repeatedly.

## See Also

### Miscellaneous
- [addChar](./api-1808034-addchar.md)
  Appends a single character to the XML stream.
- [addString](./api-1808045-addstring.md)
  Appends a C string to the XML stream.
- [addXMLEndTag](./api-1808061-addxmlendtag.md)
  Appends an XML end tag to the XML stream.
- [addXMLStartTag](./api-1808073-addxmlstarttag.md)
  Appends an XML start tag to the XML stream.
- [previouslySerialized](./api-1808096-previouslyserialized.md)
  Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.
- [text](./api-1808110-text.md)
  Returns the XML text serialized so far.
- [withCapacity](./api-1808120-withcapacity.md)
  Creates and initializes an empty OSSerialize object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize/1808086-cleartext)*