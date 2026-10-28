# canProvideDocumentSource()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns whether the receiver can provide content source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func canProvideDocumentSource() -> Bool
```

```objc
- (BOOL) canProvideDocumentSource;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver can provide source for the document content (for example, HTML source), [`false`](../../Swift/false.md) otherwise.

## Discussion

The receiver should return [`true`](../../Swift/true.md) only if it makes sense for someone to view the source of the document in question. For example, a web view returns [`false`](../../Swift/false.md) if the content is an image, was produced by a plug-in, or contains text content already.

## See Also

### Getting document source
- [func documentSource() -> String!](./documentsource%28%29.md)
  Returns the receiver’s source as text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/canprovidedocumentsource())*