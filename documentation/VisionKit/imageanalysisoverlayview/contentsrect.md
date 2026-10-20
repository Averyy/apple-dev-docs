# contentsRect

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

Returns the rectangle, in unit coordinates, that contains the image within the superview.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var contentsRect: CGRect { get }
```

#### Discussion

If your app displays the image with [`NSImageView`](../../AppKit/nsimageview.md) and you assign it to the [`trackingImageView`](./trackingimageview.md) property, the framework doesn’t require you to implement this property.

The default value is the entire contents of the superview, which is the unit rectangle `[0.0, 0.0, 1.0, 1.0]`.

## See Also

### Managing custom image views
- [func setContentsRectNeedsUpdate()](./setcontentsrectneedsupdate%28%29.md)
  Informs the view that contains the image when the layout changes and the view needs to reload its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/contentsrect)*