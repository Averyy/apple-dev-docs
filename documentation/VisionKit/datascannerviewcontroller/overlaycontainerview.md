# overlayContainerView

**Framework**: Visionkit  
**Kind**: property

A view that the data scanner displays over its view without interfering with the Live Text interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var overlayContainerView: UIView { get }
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Discussion

Optionally, add custom highlights to this view that doesn’t interfere with hit-testing or the guidance objects. If you want to add interface objects above the highlights, add those objects as subviews of the [`view`](https://developer.apple.com/documentation/UIKit/UIViewController/view) property.

## See Also

- [var regionOfInterest: CGRect?](datascannerviewcontroller/regionofinterest.md)
  The area of the live video in view coordinates that the data scanner searches for items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/overlaycontainerview)*