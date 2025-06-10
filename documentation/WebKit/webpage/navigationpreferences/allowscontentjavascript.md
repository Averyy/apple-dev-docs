# allowsContentJavaScript

**Framework**: WebKit  
**Kind**: property

Indicates whether JavaScript from web content is allowed to run.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var allowsContentJavaScript: Bool
```

#### Discussion

The default value of this property is `true`. If you change the value to `false`, the web page doesn’t execute JavaScript code referenced by the web content. That includes JavaScript code found in inline `<script>` elements, `javascript:` URLs, and all other referenced JavaScript content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/allowscontentjavascript)*