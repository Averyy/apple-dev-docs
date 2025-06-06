# regionOfInterest

**Framework**: Visionkit  
**Kind**: property

The area of the live video in view coordinates that the data scanner searches for items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var regionOfInterest: CGRect? { get set }
```

#### Discussion

If you add interface objects to the live video (using the [`overlayContainerView`](datascannerviewcontroller/overlaycontainerview.md) property) that might hide items from a person, set this property to restrict the scanning area. The default value is the bounds of the view.

## See Also

- [var overlayContainerView: UIView](datascannerviewcontroller/overlaycontainerview.md)
  A view that the data scanner displays over its view without interfering with the Live Text interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/regionofinterest)*