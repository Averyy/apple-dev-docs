# currentItem

**Framework**: WebKit  
**Kind**: property

The current item.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var currentItem: WebPage.BackForwardList.Item? { get }
```

#### Discussion

When the webpage has not loaded any resources, this value will be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/currentitem)*