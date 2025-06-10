# selectionContainerViewBelowText(for:)

**Framework**: UIKit  
**Kind**: method

Returns the container view to hold the selection-related highlight and detail views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func selectionContainerViewBelowText(for interaction: UITextSelectionDisplayInteraction) -> UIView?
```

#### Return Value

The view in your interface you use to manage selection-related views.

#### Discussion

Implement this delegate method if you use a view other than your text input view to display selection-related content and highlights. The container view you specify must sit below the text input view itself. The interaction object uses the view you provide as the parent for the views that display the selection highlight, selection handles, and caret.

## Parameters

- `interaction`: The interaction object that manages the highlight views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteractiondelegate/selectioncontainerviewbelowtext(for:))*