# forwardItem

**Framework**: WebKit  
**Kind**: property

The item immediately following the current item, if any.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var forwardItem: WKBackForwardListItem? { get }
```

#### Discussion

If the current item is the last item in the list, this value in this property is `nil`.

## See Also

- [var backItem: WKBackForwardListItem?](wkbackforwardlist/backitem.md)
  The item immediately preceding the current item, if any.
- [var currentItem: WKBackForwardListItem?](wkbackforwardlist/currentitem.md)
  The current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/forwarditem)*