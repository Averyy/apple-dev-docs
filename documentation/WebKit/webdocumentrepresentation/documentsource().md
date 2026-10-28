# documentSource()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the receiver’s source as text.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func documentSource() -> String!
```

```objc
- (NSString *) documentSource;
```

## Return Value

Returns the document source associated with the receiver or `nil` if the source cannot be provided.

## Discussion

For example, for HTML documents, the receiver should return the HTML source.

## See Also

### Getting document source
- [func canProvideDocumentSource() -> Bool](./canprovidedocumentsource%28%29.md)
  Returns whether the receiver can provide content source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/documentsource())*