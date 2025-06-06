# retargetedPreview(with:)

**Framework**: UIKit  
**Kind**: method

Returns a new targeted drag item preview based on an existing one, but with a new geometric target.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func retargetedPreview(with newTarget: UIDragPreviewTarget) -> UITargetedDragPreview
```

#### Return Value

A new targeted drag preview.

#### Discussion

You can use this method in the drop interaction delegate’s implementation of the [`dropInteraction(_:previewForDropping:withDefault:)`](uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:).md) method to replace the current targeted drag item preview with a different one.

## Parameters

- `newTarget`: A new drag item preview target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview/retargetedpreview(with:))*