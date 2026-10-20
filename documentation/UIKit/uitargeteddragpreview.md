# UITargetedDragPreview

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UITargetedDragPreview : UITargetedPreview
```

## Topics

### Initializing a targeted drag item preview
- [convenience init(forURL: URL, target: UIDragPreviewTarget)](./uitargeteddragpreview/init%28forurl,target%29.md)
  Initializes a new targeted drag item preview with a URL and a drag item preview.
- [convenience init(forURL: URL, title: String?, target: UIDragPreviewTarget)](./uitargeteddragpreview/init%28forurl,title,target%29.md)
  Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.
### Replacing the preview
- [func retargetedPreview(with: UIDragPreviewTarget) -> UITargetedDragPreview](./uitargeteddragpreview/retargetedpreview%28with%29.md)
  Returns a new targeted drag item preview based on an existing one, but with a new geometric target.
### Initializers
- [convenience init(for: URL, target: UIDragPreviewTarget)](./uitargeteddragpreview/init%28for,target%29.md)
- [convenience init(for: URL, title: String?, target: UIDragPreviewTarget)](./uitargeteddragpreview/init%28for,title,target%29.md)
### Default Implementations
- [UITargetedDragPreview Implementations](./uitargeteddragpreview/uitargeteddragpreview-implementations.md)

## Relationships

### Inherits From
- [UITargetedPreview](./uitargetedpreview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom drag item previews
- [class UIDragPreviewParameters](./uidragpreviewparameters.md)
  A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [class UIDragPreview](./uidragpreview.md)
  A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [class UIDragPreviewTarget](./uidragpreviewtarget.md)
  A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview)*