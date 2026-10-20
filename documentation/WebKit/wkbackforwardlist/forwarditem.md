# forwardItem

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The item immediately following the current item, if any.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var forwardItem: WKBackForwardListItem? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) WKBackForwardListItem * forwardItem;
```

#### Discussion

If the current item is the last item in the list, this value in this property is `nil`.

## See Also

### Getting the Most Recent Items
- [var backItem: WKBackForwardListItem?](./backitem.md)
  The item immediately preceding the current item, if any.
- [var currentItem: WKBackForwardListItem?](./currentitem.md)
  The current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/forwarditem)*