# contentsRect

**Framework**: VisionKit  
**Kind**: property

A rectangle, in unit coordinate space, that describes the content area of the interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var contentsRect: CGRect { get }
```

#### Discussion

If the interaction’s view isn’t an instance of [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView), your app sets the value for this property by implementing the [`ImageAnalysisInteractionDelegate`](imageanalysisinteractiondelegate.md) callback [`contentsRect(for:)`](imageanalysisinteractiondelegate/contentsrect(for:).md). The default return value is the unit rectangle, `[0.0, 0.0, 1.0, 1.0]`, which represents the whole view contents.

## See Also

- [func setContentsRectNeedsUpdate()](imageanalysisinteraction/setcontentsrectneedsupdate.md)
  Informs the view that contains the image when the layout changes and the view needs to reload its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/contentsrect)*