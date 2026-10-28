# hasActiveDrop

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the table view is currently tracking a drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasActiveDrop: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasActiveDrop;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the table view is tracking a drop session.

## See Also

### Managing drop interactions
- [var dropDelegate: (any UITableViewDropDelegate)?](./dropdelegate.md)
  The delegate object that manages the dropping of content into the table view.
- [protocol UITableViewDropDelegate](../uitableviewdropdelegate.md)
  The interface for handling drops in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/hasactivedrop)*