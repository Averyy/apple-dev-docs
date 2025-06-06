# documentSource()

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Returns the receiver’s source as text.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func documentSource() -> String!
```

#### Return Value

Returns the document source associated with the receiver or `nil` if the source cannot be provided.

#### Discussion

For example, for HTML documents, the receiver should return the HTML source.

## See Also

- [func canProvideDocumentSource() -> Bool](webdocumentrepresentation/canprovidedocumentsource.md)
  Returns whether the receiver can provide content source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/documentsource())*