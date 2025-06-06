# UITargetedDragPreview

**Framework**: UIKit  
**Kind**: class

A drag item preview used by the system during lift, drop, or cancellation animation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITargetedDragPreview
```

## Topics

### Initializing a targeted drag item preview
- [convenience init(forURL: URL, target: UIDragPreviewTarget)](uitargeteddragpreview/init(forurl:target:).md)
  Initializes a new targeted drag item preview with a URL and a drag item preview.
- [convenience init(forURL: URL, title: String?, target: UIDragPreviewTarget)](uitargeteddragpreview/init(forurl:title:target:).md)
  Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.
### Replacing the preview
- [func retargetedPreview(with: UIDragPreviewTarget) -> UITargetedDragPreview](uitargeteddragpreview/retargetedpreview(with:).md)
  Returns a new targeted drag item preview based on an existing one, but with a new geometric target.

## Relationships

### Inherits From
- [UITargetedPreview](uitargetedpreview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIDragPreviewParameters](uidragpreviewparameters.md)
  A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [class UIDragPreview](uidragpreview.md)
  A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [class UIDragPreviewTarget](uidragpreviewtarget.md)
  A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview)*