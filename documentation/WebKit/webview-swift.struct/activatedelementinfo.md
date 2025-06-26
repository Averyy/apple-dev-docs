# WebView.ActivatedElementInfo

**Framework**: WebKit  
**Kind**: struct

Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct ActivatedElementInfo
```

#### Overview

For links, the information contains the URL that is linked to.

## Topics

### Instance Properties
- [let linkURL: URL?](webview-swift.struct/activatedelementinfo/linkurl.md)
  The URL of the link that the user clicked.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/activatedelementinfo)*