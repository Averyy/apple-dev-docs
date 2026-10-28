# actions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The swipe actions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var actions: [UIContextualAction] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<UIContextualAction *> * actions;
```

## Discussion

The first object in this array corresponds to the default action, which is the action that’s performed in response to a full swipe.

## See Also

### Getting the swipe action information
- [var performsFirstActionWithFullSwipe: Bool](./performsfirstactionwithfullswipe.md)
  A Boolean value indicating whether a full swipe automatically performs the first action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/actions)*