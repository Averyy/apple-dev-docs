# insertBeforeDocument

**Framework**: TVMLKit JS  
**Kind**: instm

Inserts a new document directly before a document currently on the stack.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void insertBeforeDocument(
    in Document document, 
    in optional Document beforeDocument
);
```

#### Discussion

This function searches the stack for the first instance of the document contained in the `beforeDocument` parameter and inserts the document contained in the `document` parameter on top of it.

## Parameters

- `document`: The DOM document that is to be added onto the stack.
- `beforeDocument`: A DOM document currently on the stack. The new document is placed on the stack directly after this document.

## See Also

- [pushDocument](navigationdocument/1627361-pushdocument.md)
  Pushes the specified document onto the stack.
- [replaceDocument](navigationdocument/1627430-replacedocument.md)
  Replaces a document on the stack with a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument/1627340-insertbeforedocument)*