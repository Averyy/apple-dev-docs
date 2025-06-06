# replaceDocument

**Framework**: TVMLKit JS  
**Kind**: instm

Replaces a document on the stack with a new document.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void replaceDocument(
    in Document document, 
    in Document oldDocument
);
```

#### Discussion

This function searches the stack for the first instance of the document to be replaced and replaces it with the new document.

## Parameters

- `document`: The DOM document that is to be added onto the stack.
- `oldDocument`: The DOM document that is being replaced.

## See Also

- [insertBeforeDocument](navigationdocument/1627340-insertbeforedocument.md)
  Inserts a new document directly before a document currently on the stack.
- [pushDocument](navigationdocument/1627361-pushdocument.md)
  Pushes the specified document onto the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument/1627430-replacedocument)*