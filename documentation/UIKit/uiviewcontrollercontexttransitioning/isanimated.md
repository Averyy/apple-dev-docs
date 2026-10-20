# isAnimated

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the transition should be animated.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isAnimated: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAnimated) BOOL animated;
```

#### Discussion

The value of this property is always [`true`](../../Swift/true.md) for modal presentation styles other than the [`UIModalPresentationStyle.custom`](../uimodalpresentationstyle/custom.md) style. When the modal presentation style is [`UIModalPresentationStyle.custom`](../uimodalpresentationstyle/custom.md), the value is [`true`](../../Swift/true.md) if the transition should be animated or [`false`](../../Swift/false.md) if it should not. Use this value to determine whether you need to animate a custom transition into place, or whether you should install the final views into the container without animating the changes.

## See Also

### Getting the transition behaviors
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  Returns the presentation style for the view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/isanimated)*