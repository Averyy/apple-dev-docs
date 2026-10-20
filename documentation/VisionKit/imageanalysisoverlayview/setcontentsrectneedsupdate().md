# setContentsRectNeedsUpdate()

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that contains the image when the layout changes and the view needs to reload its content.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func setContentsRectNeedsUpdate()
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

#### Discussion

The framework ignores calls to this method when the superview is of type [`NSImageView`](../../AppKit/nsimageview.md).

If the superview is a class other than `NSImageView`, call this method when the layout changes. The overlay view then invokes the delegate’s [`contentsRect(for:)`](../imageanalysisoverlayviewdelegate/contentsrect%28for%29-34yzu.md) method to request the new content area.

## See Also

### Managing custom image views
- [var contentsRect: CGRect](./contentsrect.md)
  Returns the rectangle, in unit coordinates, that contains the image within the superview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/setcontentsrectneedsupdate())*