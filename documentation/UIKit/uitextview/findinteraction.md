# findInteraction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text view’s built-in find interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var findInteraction: UIFindInteraction? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIFindInteraction * findInteraction;
```

## Discussion

Set [`isFindInteractionEnabled`](./isfindinteractionenabled.md) to `true` to enable the text view’s built-in find interaction. This method returns `nil` when the interaction isn’t enabled.

Call [`presentFindNavigator(showingReplace:)`](../uifindinteraction/presentfindnavigator%28showingreplace%29.md) on the [`UIFindInteraction`](../uifindinteraction.md) object returned by this method to invoke the find interaction and display the find panel.

## See Also

### Supporting Find and Replace
- [var isFindInteractionEnabled: Bool](./isfindinteractionenabled.md)
  A Boolean value that enables a text view’s built-in find interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/findinteraction)*