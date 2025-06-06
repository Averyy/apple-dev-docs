# targetTransform

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

Returns a transform indicating the amount of rotation being applied during the transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var targetTransform: CGAffineTransform { get }
```

#### Return Value

An affine transform indicating the amount of rotation being applied to the interface. This transform is the identity transform when no rotation is applied; otherwise, it is a transform that applies a 90 degree, -90 degree, or 180 degree rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/targettransform)*