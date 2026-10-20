# evaluate(_:contextNode:resolver:type:in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```swift
func evaluate(_ expression: String!, contextNode: DOMNode!, resolver: (any DOMXPathNSResolver)!, type: UInt16, in inResult: DOMXPathResult!) -> DOMXPathResult!
```

```objc
- (DOMXPathResult *) evaluate:(NSString *) expression contextNode:(DOMNode *) contextNode resolver:(id<DOMXPathNSResolver>) resolver type:(unsigned short) type inResult:(DOMXPathResult *) inResult;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domdocument/evaluate(_:contextnode:resolver:type:in:))*