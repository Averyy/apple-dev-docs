# allowsContentJavaScript

**Framework**: WebKit  
**Kind**: property

Indicates whether JavaScript from web content is allowed to run.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allowsContentJavaScript: Bool
```

#### Discussion

The default value of this property is `true`. If you change the value to `false`, the web page doesn’t execute JavaScript code referenced by the web content. That includes JavaScript code found in inline `<script>` elements, `javascript:` URLs, and all other referenced JavaScript content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/allowscontentjavascript)*