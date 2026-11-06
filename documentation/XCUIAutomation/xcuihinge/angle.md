# angle

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The hinge’s current angle, in radians.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
var angle: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat angle;
```

## Discussion

Setting this property can cause the device to switch between displays. Reading the angle alone does not tell you which layout your app uses.

> **Note**: On physical devices, programmatically opening the hinge while the device is closed is not supported and results in a test failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuihinge/angle)*