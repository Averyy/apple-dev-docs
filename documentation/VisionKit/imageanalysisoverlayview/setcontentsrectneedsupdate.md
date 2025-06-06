# setContentsRectNeedsUpdate()

**Framework**: Visionkit  
**Kind**: method

Informs the view that contains the image when the layout changes and the view needs to reload its content.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func setContentsRectNeedsUpdate()
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

The framework ignores calls to this method when the superview is of type [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView).

If the superview is a class other than `NSImageView`, call this method when the layout changes. The overlay view then invokes the delegate’s [`contentsRect(for:)`](imageanalysisoverlayviewdelegate/contentsrect(for:)-34yzu.md) method to request the new content area.

## See Also

- [var contentsRect: CGRect](imageanalysisoverlayview/contentsrect.md)
  Returns the rectangle, in unit coordinates, that contains the image within the superview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/setcontentsrectneedsupdate())*