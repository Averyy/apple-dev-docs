# isSupported

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

Reports whether the system supports this processor on the current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class var isSupported: Bool { get }
```

```objc
@property (class, nonatomic, readonly, getter=isSupported) BOOL supported;
```

## See Also

### Determining processor availability
- [class func supportedScaleFactors(frameWidth: Int, frameHeight: Int) -> [Float]](./supportedscalefactors%28framewidth,frameheight%29.md)
- [maximumDimensions](./maximumdimensions.md)
  Maximum dimensions for a source frame for the processor.
- [minimumDimensions](./minimumdimensions.md)
  Minimum dimensions for a source frame for the processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration/issupported)*