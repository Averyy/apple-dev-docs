# gestureRecognizers

**Framework**: UIKit  
**Kind**: property

The gesture recognizers that are receiving the touch object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var gestureRecognizers: [UIGestureRecognizer]? { get }
```

#### Discussion

The objects in the array are instances of a subclass of the abstract base class [`UIGestureRecognizer`](uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch, this property contains an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/gesturerecognizers)*