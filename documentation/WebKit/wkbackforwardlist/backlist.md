# backList

**Framework**: Webkit  
**Kind**: property

The array of items that precede the current item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backList: [WKBackForwardListItem] { get }
```

#### Discussion

The items are in the order in which the web view originally visited them.

## See Also

- [var forwardList: [WKBackForwardListItem]](wkbackforwardlist/forwardlist.md)
  The array of items that follow the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/backlist)*