# setNeedsSelectionUpdate()

**Framework**: UIKit  
**Kind**: method

Tells the system to update the selection UI to match the current selection state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsSelectionUpdate()
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

When the selection state changes in your text input view, call this method to notify the system of the change. The system fetches the current selection state from your text input view and updates the system UI to match.

## See Also

- [func layoutManagedSubviews()](uitextselectiondisplayinteraction/layoutmanagedsubviews.md)
  Loads the selection from the text input view and lays out the selection-related views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/setneedsselectionupdate())*