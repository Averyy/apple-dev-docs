# documentView

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The subview that displays the web content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var documentView: (any NSView & WebDocumentView)! { get }
```

```objc
@property (nonatomic, strong, readonly) NSView<WebDocumentView> * documentView;
```

## Discussion

Use [`allowsScrolling`](./allowsscrolling.md) to enable scrolling of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/documentview)*