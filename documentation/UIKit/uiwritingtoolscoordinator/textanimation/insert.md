# UIWritingToolsCoordinator.TextAnimation.insert

**Framework**: UIKit  
**Kind**: case

The animation that Writing Tools performs when inserting text into your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case insert
```

#### Discussion

This type of animation shows the insertion of text to your view. When preparing for this animation, hide the text in the provided range if you haven’t already. If you support animating the reflow of your view’s text, you can also prepare any other animations you need. Writing Tools uses a preview object you provide to animate the insertion of the text.

## See Also

- [UIWritingToolsCoordinator.TextAnimation.anticipate](uiwritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [UIWritingToolsCoordinator.TextAnimation.remove](uiwritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/insert)*