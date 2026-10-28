# presentationStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the presentation style for the view controller transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var presentationStyle: UIModalPresentationStyle { get }
```

```objc
@property (nonatomic, readonly) UIModalPresentationStyle presentationStyle;
```

## Return Value

The presentation style to use when presenting the final view controller.

## See Also

### Getting the transition behaviors
- [var isAnimated: Bool](./isanimated.md)
  A Boolean value indicating whether the transition should be animated.
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/presentationstyle)*