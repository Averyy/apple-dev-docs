# currentItem

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The current item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var currentItem: WKBackForwardListItem? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) WKBackForwardListItem * currentItem;
```

## See Also

### Getting the Most Recent Items
- [var backItem: WKBackForwardListItem?](./backitem.md)
  The item immediately preceding the current item, if any.
- [var forwardItem: WKBackForwardListItem?](./forwarditem.md)
  The item immediately following the current item, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/currentitem)*