# performsFirstActionWithFullSwipe

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether a full swipe automatically performs the first action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var performsFirstActionWithFullSwipe: Bool { get set }
```

```objc
@property (nonatomic) BOOL performsFirstActionWithFullSwipe;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), a full swipe in the row performs the first action listed in the [`actions`](./actions.md) property. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Getting the swipe action information
- [var actions: [UIContextualAction]](./actions.md)
  The swipe actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/performsfirstactionwithfullswipe)*