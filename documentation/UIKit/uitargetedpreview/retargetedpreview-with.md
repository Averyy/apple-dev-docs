# retargetedPreview(with:)

**Framework**: UIKit  
**Kind**: method

Returns a targeted preview object with the same view and parameters, but with a different target container.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func retargetedPreview(with newTarget: UIPreviewTarget) -> UITargetedPreview
```

#### Return Value

A new targeted preview object containing the specified target and the current view.

## Parameters

- `newTarget`: The new target for the existing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargetedpreview/retargetedpreview(with:))*