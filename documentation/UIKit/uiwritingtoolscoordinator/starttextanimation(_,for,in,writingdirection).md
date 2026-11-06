# startTextAnimation(_:for:in:writingDirection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. When an issue is first identified and indicated, call this to have it animated.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
func startTextAnimation(_ textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?
```

```objc
- (NSUUID *) startTextAnimation:(UIWritingToolsCoordinatorTextAnimation) textAnimation forRange:(NSRange) range inContext:(UIWritingToolsCoordinatorContext *) context writingDirection:(NSWritingDirection) writingDirection;
```

## Discussion

The context should be large enough to contain the range being indicated, and the range should be the range of the issue within the context. Returns a UUID that can be used to cancel the animation, or nil if the animation cannot be performed. Calls delegate methods to prepare for the animation (which should hide the text), request previews (with and without underlines), and finish the animation (which should show the text).

## See Also

### Managing grammar animations
- [func showGrammarPresentation(for: NSRange, in: UIWritingToolsCoordinator.Context) -> Bool](./showgrammarpresentation%28for,in%29.md)
  Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.
- [func cancelTextAnimations(identifiers: [UUID])](./canceltextanimations%28identifiers%29.md)
  Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.
- [UIWritingToolsCoordinator.TextDecoration](./textdecoration.md)
  Use the `UIWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/starttextanimation(_:for:in:writingdirection:))*