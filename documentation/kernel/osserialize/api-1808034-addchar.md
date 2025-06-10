# addChar

**Framework**: Kernel  
**Kind**: instm

Appends a single character to the XML stream.

## Declaration

```swift
virtual bool addChar(
 const charaChar);
```

#### Return_value

`true` if `char` is successfully added to the XML stream, `false` otherwise.

## Parameters

- `aChar`: The character to append to the XML stream.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize/1808034-addchar)*