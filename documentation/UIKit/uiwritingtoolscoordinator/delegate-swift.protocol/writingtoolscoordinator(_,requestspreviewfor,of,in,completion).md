# writingToolsCoordinator(_:requestsPreviewFor:of:in:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for a preview image and layout information for the specified text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, of range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable (UITargetedPreview?) -> Void)
```

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, previewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, range: NSRange, context: UIWritingToolsCoordinator.Context) async -> UITargetedPreview?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) writingToolsCoordinator:(UIWritingToolsCoordinator *) writingToolsCoordinator requestsPreviewForTextAnimation:(UIWritingToolsCoordinatorTextAnimation) textAnimation ofRange:(NSRange) range inContext:(UIWritingToolsCoordinatorContext *) context completion:(void (^)(UITargetedPreview *)) completion;
```

*watchOS*

```objc
- (void) writingToolsCoordinator:(UIWritingToolsCoordinator *) writingToolsCoordinator requestsPreviewForTextAnimation:(UIWritingToolsCoordinatorTextAnimation) textAnimation ofRange:(NSRange) range inContext:(UIWritingToolsCoordinatorContext *) context completion:(void (^)(UIView *)) completion;
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](../../adding-writing-tools-support-to-a-custom-uiview.md)

## Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. As part of the preparation for those animations, Writing Tools asks you to provide a preview of the affected content in your view. Writing Tools uses this preview to build and execute the animations in the view stored in the [`effectContainerView`](../effectcontainerview.md) property of the coordinator object.

To build a preview of your content in iOS, render the specified range of text into an image with a transparent background. Install the image in a [`UIImageView`](../../uiimageview.md) and use that to build your preview object. Set the frame rectangle of your image view to the rectangle in your view’s coordinate space that contains the text you captured. When creating the [`UITargetedPreview`](../../uitargetedpreview.md) object, include both a [`UIPreviewParameters`](../../uipreviewparameters.md) and a [`UIPreviewTarget`](../../uipreviewtarget.md) object. Create the [`UIPreviewTarget`](../../uipreviewtarget.md) object with your text view as the container, and set the center point to the center of your text view. Create the [`UIPreviewParameters`](../../uipreviewparameters.md) object using `init(textLineRects:)`, passing an array containing one rectangle per line of the selected text, which you get from your view’s layout manager.

> ❗ **Important**: Provide one rectangle per line in `textLineRects`. Writing Tools uses each rectangle to animate its line independently, layering a bounce effect on top of the shimmer. If you provide a single rectangle that spans the entire range instead, Writing Tools can only animate the text as one unit, which produces a shimmer only, without the bounce.

For a single animation type, the system calls this method, followed sequentially by the `writingToolsCoordinator(_:prepareFor:range:context:completion:)` and [`writingToolsCoordinator(_:finish:for:in:completion:)`](./writingtoolscoordinator%28_,finish,for,in,completion%29.md) methods. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` parameter to differentiate sequences.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you that animations are about to begin.
- `textAnimation`: The type of animation Writing Tools is preparing.
- `range`: The range of text that requires a preview image. This range is relative to the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.
- `context`: The context object that contains the original text. Use this object to fetch the current text, and to match that text to your underlying text storage.
- `completion`: A completion handler to execute when you are done. The handler has no return value and takes a [`UITargetedPreview`](../../uitargetedpreview.md) object as a parameter. You must call this handler at some point during your implementation.

## See Also

### Animating inline text changes
- [func writingToolsCoordinator(UIWritingToolsCoordinator, prepareFor: UIWritingToolsCoordinator.TextAnimation, for: NSRange, in: UIWritingToolsCoordinator.Context, completion: () -> Void)](./writingtoolscoordinator%28_,preparefor,for,in,completion%29.md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, finish: UIWritingToolsCoordinator.TextAnimation, for: NSRange, in: UIWritingToolsCoordinator.Context, completion: () -> Void)](./writingtoolscoordinator%28_,finish,for,in,completion%29.md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:))*