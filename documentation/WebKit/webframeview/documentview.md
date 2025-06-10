# documentView

**Framework**: WebKit  
**Kind**: property

The subview that displays the web content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var documentView: (any NSView & WebDocumentView)! { get }
```

#### Discussion

Use [`allowsScrolling`](webframeview/allowsscrolling.md) to enable scrolling of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/documentview)*