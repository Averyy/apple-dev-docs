# isAnimated

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the transition should be animated.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isAnimated: Bool { get }
```

#### Discussion

The value of this property is always [`true`](https://developer.apple.com/documentation/swift/true) for modal presentation styles other than the [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md) style. When the modal presentation style is [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md), the value is [`true`](https://developer.apple.com/documentation/swift/true) if the transition should be animated or [`false`](https://developer.apple.com/documentation/swift/false) if it should not. Use this value to determine whether you need to animate a custom transition into place, or whether you should install the final views into the container without animating the changes.

## See Also

- [var isInteractive: Bool](uiviewcontrollercontexttransitioning/isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var presentationStyle: UIModalPresentationStyle](uiviewcontrollercontexttransitioning/presentationstyle.md)
  Returns the presentation style for the view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/isanimated)*