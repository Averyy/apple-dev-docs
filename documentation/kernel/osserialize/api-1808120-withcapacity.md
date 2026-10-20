# withCapacity

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an empty OSSerialize object.

## Declaration

```c
static OSSerialize * withCapacity(
 unsigned intcapacity);
```

#### Return Value

A new instance of OSSerialize with a retain count of 1; `NULL` on failure.

#### Overview

The serializer will grow as needed to accommodate more data.

## Parameters

- `capacity`: The initial size of the XML buffer.

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
- [clearText](./api-1808086-cleartext.md)
  Resets the OSSerialize object.
- [previouslySerialized](./api-1808096-previouslyserialized.md)
  Checks whether the object has already been serialized into the XML stream, emitting a reference if it has.
- [text](./api-1808110-text.md)
  Returns the XML text serialized so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserialize/1808120-withcapacity)*