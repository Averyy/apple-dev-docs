# forwardList

**Framework**: WebKit  
**Kind**: property

The array of items that follow the current item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var forwardList: [WebPage.BackForwardList.Item] { get }
```

#### Discussion

The items are in the order in which the web view originally visited them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/forwardlist)*