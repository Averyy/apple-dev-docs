# writingToolsCoordinator(_:finish:for:in:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to clean up any state related to the specified Writing Tools animation.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, finish textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context) async
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Use this method to clean up any data structures you created to support the specified type of Writing Tools animation. You can also use this method to restore the visibility of any text you hid previously. When you finish your cleanup work, call the completion handler to notify Writing Tools.

Writing Tools calls this method only after previous calls to the `writingToolsCoordinator(_:requestsPreviewFor:range:context:completion:)` and `writingToolsCoordinator(_:prepareFor:range:context:completion:)` methods for the same animation type. However, Writing Tools can interleave calls to this method with calls to prepare an animation of a different type. In your implementation of this method, make sure the actions you take don’t interfere with other in-flight animations.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you   that animations are about to begin.
- `textAnimation`: The type of animation Writing Tools finished.
- `range`: The range of text that finished animating. This range is   relative to the text in your context object, and it’s your responsibility   to match that location to the correct location in your text storage. If   you initialized the context object with the entire contents of your   view’s text storage, you can use   as-is to access that text storage.   However, if you initialized the context object with only a portion of   your view’s text, add the starting location of your context object’s   text to this value to get the correct range for that text storage.
- `context`: The context object that contains the original text.
- `completion`: A completion handler to execute when you are done.   The handler has no return value and takes no parameters. You must   call this handler at some point during your implementation.

## See Also

- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsPreviewFor: UIWritingToolsCoordinator.TextAnimation, of: NSRange, in: UIWritingToolsCoordinator.Context, completion: (UITargetedPreview?) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, prepareFor: UIWritingToolsCoordinator.TextAnimation, for: NSRange, in: UIWritingToolsCoordinator.Context, completion: () -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md)
  Prepare for animations for the content that Writing Tools is evaluating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:))*