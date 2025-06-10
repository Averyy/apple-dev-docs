# UIWritingToolsCoordinator.TextAnimation.anticipate

**Framework**: UIKit  
**Kind**: case

The animation that Writing Tools performs when waiting to receive results from the large language model.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case anticipate
```

#### Discussion

This type of animation applies a visual effect to the text that Writing Tools is evaluating. When preparing for this animation, hide the text that Writing Tools is about to evaluate. In the same space where that text appears, Writing Tools displays a preview image that you provide and animates changes to that image.

## See Also

- [UIWritingToolsCoordinator.TextAnimation.insert](uiwritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [UIWritingToolsCoordinator.TextAnimation.remove](uiwritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/anticipate)*