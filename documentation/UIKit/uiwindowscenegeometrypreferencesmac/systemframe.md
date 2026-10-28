# systemFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred frame of the scene, in system coordinates.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 16.0+
- tvOS
- visionOS

## Declaration

```objc
@property (nonatomic, assign) CGRect systemFrame;
```

## Discussion

This property represents the preferred frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display. The default value is [`CGRectNull`](../../CoreGraphics/cgrectnull.md), which indicates no preferred frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenegeometrypreferencesmac/systemframe)*