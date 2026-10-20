# setTabs(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the root tabs of the tab bar controller, with an option to animate the change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func setTabs(_ tabs: [UITab], animated: Bool)
```

```objc
- (void) setTabs:(NSArray<UITab *> *) tabs animated:(BOOL) animated;
```

## See Also

### Assigning tabs
- [var tabs: [UITab]](./tabs.md)
  An array of tabs that the tab bar displays.
- [func performBatchUpdates(() -> Void)](./performbatchupdates%28_%29.md)
  Animates multiple tab changes as a single update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/settabs(_:animated:))*