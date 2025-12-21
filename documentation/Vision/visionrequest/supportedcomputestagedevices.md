# supportedComputeStageDevices

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The collection of compute devices per stage that a request supports.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var supportedComputeStageDevices: [ComputeStage : [MLComputeDevice]] { get }
```

## See Also

- [func computeDevice(for: ComputeStage) -> MLComputeDevice?](visionrequest/computedevice(for:).md)
  Returns the compute device for a compute stage.
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionrequest/supportedcomputestagedevices)*