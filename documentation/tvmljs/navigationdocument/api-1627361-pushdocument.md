# pushDocument

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Pushes the specified document onto the stack.

**Availability**:
- tvOS 9.0+

## Declaration

```
void pushDocument(
    in Document document
);
```

## Discussion

The document being pushed onto the stack must be a valid parsed DOM object.

## Parameters

- `document`: The DOM document that is to be added onto the stack.

## See Also

### Adding Documents to the Stack
- [insertBeforeDocument](./api-1627340-insertbeforedocument.md)
  Inserts a new document directly before a document currently on the stack.
- [replaceDocument](./api-1627430-replacedocument.md)
  Replaces a document on the stack with a new document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument/1627361-pushdocument)*