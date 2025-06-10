# currentItem

**Framework**: WebKit  
**Kind**: property

The current item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var currentItem: WebPage.BackForwardList.Item? { get }
```

#### Discussion

When the webpage has not loaded any resources, this value will be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/currentitem)*