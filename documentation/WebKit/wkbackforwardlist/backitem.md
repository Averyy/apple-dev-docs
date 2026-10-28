# backItem

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The item immediately preceding the current item, if any.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var backItem: WKBackForwardListItem? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) WKBackForwardListItem * backItem;
```

## Discussion

If the current item is the first item in the list, the value in this property is `nil`.

## See Also

### Getting the Most Recent Items
- [var currentItem: WKBackForwardListItem?](./currentitem.md)
  The current item.
- [var forwardItem: WKBackForwardListItem?](./forwarditem.md)
  The item immediately following the current item, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/backitem)*