# interfaceOrientations

**Framework**: UIKit  
**Kind**: property

The preferred interface orientations for the scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var interfaceOrientations: UIInterfaceOrientationMask? { get set }
```

#### Discussion

If you specify this value, the system automatically chooses an orientation from the intersection of these preferred orientations and the supported orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/ios/interfaceorientations)*