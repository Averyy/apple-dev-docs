# findInteraction

**Framework**: UIKit  
**Kind**: property

The text view’s built-in find interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var findInteraction: UIFindInteraction? { get }
```

#### Discussion

Set [`isFindInteractionEnabled`](uitextview/isfindinteractionenabled.md) to `true` to enable the text view’s built-in find interaction. This method returns `nil` when the interaction isn’t enabled.

Call [`presentFindNavigator(showingReplace:)`](uifindinteraction/presentfindnavigator(showingreplace:).md) on the [`UIFindInteraction`](uifindinteraction.md) object returned by this method to invoke the find interaction and display the find panel.

## See Also

- [var isFindInteractionEnabled: Bool](uitextview/isfindinteractionenabled.md)
  A Boolean value that enables a text view’s built-in find interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/findinteraction)*