# contentsRect

**Framework**: VisionKit  
**Kind**: property

Returns the rectangle, in unit coordinates, that contains the image within the superview.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var contentsRect: CGRect { get }
```

#### Discussion

If your app displays the image with [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView) and you assign it to the [`trackingImageView`](imageanalysisoverlayview/trackingimageview.md) property, the framework doesn’t require you to implement this property.

The default value is the entire contents of the superview, which is the unit rectangle `[0.0, 0.0, 1.0, 1.0]`.

## See Also

- [func setContentsRectNeedsUpdate()](imageanalysisoverlayview/setcontentsrectneedsupdate.md)
  Informs the view that contains the image when the layout changes and the view needs to reload its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/contentsrect)*