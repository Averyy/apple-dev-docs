# interfaceOrientations

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred interface orientations for the scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign) UIInterfaceOrientationMask interfaceOrientations;
```

## Discussion

If you specify this value, the system automatically chooses an orientation from the intersection of these preferred orientations and the supported orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenegeometrypreferencesios/interfaceorientations)*