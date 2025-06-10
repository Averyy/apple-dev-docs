# snapshotWidth

**Framework**: WebKit  
**Kind**: property

The width of the captured image, in points.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var snapshotWidth: NSNumber? { get set }
```

#### Discussion

Use this property to scale the generated image to the specified width. The web view maintains the aspect ratio of the captured content, but scales it to match the width you specify.

The default value of this property is `nil`, which returns an image whose size matches the original size of the captured rectangle.

## See Also

- [var rect: CGRect](wksnapshotconfiguration/rect.md)
  The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksnapshotconfiguration/snapshotwidth)*