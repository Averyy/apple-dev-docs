# filterStrength

**Framework**: Video Toolbox  
**Kind**: property

A parameter to control the strength of noise-filtering. The value can range from the minimum strength of 0.0 to the maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to processing the source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var filterStrength: Float { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/filterstrength)*