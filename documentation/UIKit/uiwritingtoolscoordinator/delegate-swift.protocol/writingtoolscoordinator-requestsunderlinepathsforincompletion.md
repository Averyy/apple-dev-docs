# writingToolsCoordinator(_:requestsUnderlinePathsFor:in:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to provide an underline shape for the specified text during a proofreading session.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, underlinePathsFor range: NSRange, context: UIWritingToolsCoordinator.Context) async -> [UIBezierPath]
```

#### Discussion

When applying proofreading marks to your view’s content, the coordinator calls this method to retrieve a shape to draw under the specified text. You provide the shape using one or more Bezier paths, and the coordinator draws and animates that shape during the proofreading session.

After you determine the location of the specified range of text in your view’s text storage, find the rectangle around that text. If you’re using TextKit, you can call the [`enumerateTextSegments(in:type:options:using:)`](https://developer.apple.com/documentation/AppKit/NSTextLayoutManager/enumerateTextSegments(in:type:options:using:)) method of your view’s [`NSTextLayoutManager`](NSTextLayoutManager.md) to get the rectangles for a range of text. Convert the coordinates of each rectangle to the coordinate space of the view in your coordinator’s [`decorationContainerView`](uiwritingtoolscoordinator/decorationcontainerview.md) property. Use those rectangles to create the Bezier paths for your text. For example, you might create a path with a straight or wavy line at the bottom of the rectangle.

## Parameters

- `writingToolsCoordinator`: The coordinator object requesting information   from your custom view.
- `range`: The range of text to evaluate. This range is relative to the   text in your context object, and it’s your responsibility to match that   location to the correct location in your text storage. If you initialized   the context object with the entire contents of your view’s text storage,   you can use   as-is to access that text storage. However, if you   initialized the context object with only a portion of your view’s text,   add the starting location of your context object’s text to this value   to get the correct range for that text storage.
- `context`: The context object with the target text. Use this object to   find the text in your view’s text storage.
- `completion`: A handler to execute with the required information. The   handler has no return value and takes an array of Bezier paths as a   parameter. You must call this handler at some point during your method’s implementation.

## See Also

- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsRangeInContextWithIdentifierFor: CGPoint, completion: (NSRange, UUID) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:).md)
  Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsBoundingBezierPathsFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([UIBezierPath]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:).md)
  Asks the delegate to provide the bounding paths for the specified text in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsunderlinepathsfor:in:completion:))*