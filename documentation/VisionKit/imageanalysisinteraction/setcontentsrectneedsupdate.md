# setContentsRectNeedsUpdate()

**Framework**: Visionkit  
**Kind**: method

Informs the view that contains the image when the layout changes and the view needs to reload its content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func setContentsRectNeedsUpdate()
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

The framework ignores calls to this method when your app adds the interaction to a [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView), which calculates the [`contentsRect`](imageanalysisinteraction/contentsrect.md) based on the image view’s [`UIView.ContentMode`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum).

When the view that contains the image isn’t an instance of [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView), call this method when the layout changes. The interaction then invokes the delegate’s [`contentsRect(for:)`](imageanalysisinteractiondelegate/contentsrect(for:).md) callback, which provides the updated content area to the system.

## See Also

- [var contentsRect: CGRect](imageanalysisinteraction/contentsrect.md)
  A rectangle, in unit coordinate space, that describes the content area of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/setcontentsrectneedsupdate())*