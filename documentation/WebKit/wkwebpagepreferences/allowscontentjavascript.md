# allowsContentJavaScript

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether JavaScript from web content is allowed to run.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var allowsContentJavaScript: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsContentJavaScript;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md). If you change the value to false, the web view doesn’t execute JavaScript code referenced by the web content. That includes JavaScript code found in inline `<script>` elements, `javascript:` URLs, and all other referenced JavaScript content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/allowscontentjavascript)*