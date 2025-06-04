# WKVideoGravity.resize

**Framework**: WatchKit  
**Kind**: case

Content is resized to fit the entire bounds rectangle. This option does not preserve the original aspect ratio of the content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
case resize
```

## See Also

- [WKVideoGravity.resizeAspect](resizeaspect.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/resizeaspect))
  Content is resized to fit the bounds rectangle, preserving the original aspect ratio of the content. Content that does not completely fill the bounds rectangle is centered in the partial axis.
- [WKVideoGravity.resizeAspectFill](resizeaspectfill.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/resizeaspectfill))
  Content is resized to fill the bounds rectangle completely while preserving the original aspect ratio of the content. This option results in cropping of the edges of the video in the axis it exceeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkvideogravity/resize)*