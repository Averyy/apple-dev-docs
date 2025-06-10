# writingToolsCoordinator(_:requestsRangeInContextWithIdentifierFor:completion:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, rangeInContextWithIdentifierFor point: CGPoint) async -> (NSRange, UUID)
```

#### Discussion

When someone interacts with your view during a proofreading operation, Writing Tools calls this method to get the location of the interaction. If the interaction occurs in the text of one of your [`UIWritingToolsCoordinator.Context`](uiwritingtoolscoordinator/context.md) objects, configure an [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) with the character’s location in that context object and a length of `1`. If the interaction occurs outside of the text of your context objects, configure the range with a location of `NSNotFound`.

When specifying the location of a character in your context object, provide a location relative to the start of your context object’s text. The first character in a context object’s text is always at location `0`, and it’s your responsibility to track the location of the context object’s text in your text storage object. When the context object’s text begins in the middle of your text storage, subtract the starting location of the context object’s text from the location you specify in your range value. For example, if the context object’s text starts at character `100` in your text storage, and an interaction occurs with the character at location `102`, specify a range with a location of `2` and a length of `1`.

## Parameters

- `writingToolsCoordinator`: The coordinator object requesting   information from your custom view.
- `point`: A point in your view’s coordinate space. Find the   location of the text under this point, if any.
- `completion`: A handler to execute with the required information.   This handler has no return value and takes an    and    as parameters. Set the range to the character’s location in one of your    objects, which you specify using   the   parameter.   You must call this handler at some point during your method’s implementation.

## See Also

- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsBoundingBezierPathsFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([UIBezierPath]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:).md)
  Asks the delegate to provide the bounding paths for the specified text in your view.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsUnderlinePathsFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([UIBezierPath]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsunderlinepathsfor:in:completion:).md)
  Asks the delegate to provide an underline shape for the specified text during a proofreading session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:))*