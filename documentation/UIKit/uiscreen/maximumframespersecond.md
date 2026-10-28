# maximumFramesPerSecond

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of frames per second a screen can render.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+

## Declaration

```swift
var maximumFramesPerSecond: Int { get }
```

```objc
@property (readonly) NSInteger maximumFramesPerSecond;
```

## Discussion

In iOS, the value of this property can be up to `120` for devices with ProMotion displays.

In tvOS, the value of this property depends on the hardware capabilities of the attached screen and the user’s selected resolution on Apple TV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/maximumframespersecond)*