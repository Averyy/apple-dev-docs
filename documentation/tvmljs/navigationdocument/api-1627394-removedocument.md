# removeDocument

**Framework**: TVMLKit JS  
**Kind**: instm

Removes the specified document from the stack.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void removeDocument(
    in Document document
);
```

## Parameters

- `document`: A DOM document created by parsing a TVML file.

## See Also

- [clear](navigationdocument/1627312-clear.md)
  Removes all documents currently on the stack.
- [popDocument](navigationdocument/1627397-popdocument.md)
  Removes the top most document from the stack.
- [popToDocument](navigationdocument/1627420-poptodocument.md)
  Removes all of the documents on the stack that are above the passed document. 
- [popToRootDocument](navigationdocument/1627382-poptorootdocument.md)
  Removes all documents from the stack except for the bottom-most document, which is the root document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument/1627394-removedocument)*