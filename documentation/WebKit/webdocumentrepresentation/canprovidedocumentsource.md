# canProvideDocumentSource()

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Returns whether the receiver can provide content source.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func canProvideDocumentSource() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver can provide source for the document content (for example, HTML source), [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The receiver should return [`true`](https://developer.apple.com/documentation/swift/true) only if it makes sense for someone to view the source of the document in question. For example, a web view returns [`false`](https://developer.apple.com/documentation/swift/false) if the content is an image, was produced by a plug-in, or contains text content already.

## See Also

- [func documentSource() -> String!](webdocumentrepresentation/documentsource.md)
  Returns the receiver’s source as text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/canprovidedocumentsource())*