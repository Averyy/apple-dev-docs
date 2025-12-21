# nextFrames

**Framework**: Video Toolbox  
**Kind**: property

Future reference frames in presentation time order that you use to process the source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var nextFrames: [VTFrameProcessorFrame] { get }
```

#### Discussion

The number of frames can vary from 0 to the number specified by the `nextFrameCount` property in `VTTemporalNoiseFilterConfiguration`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/nextframes)*