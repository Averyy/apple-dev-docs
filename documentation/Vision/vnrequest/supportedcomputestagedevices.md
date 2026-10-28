# supportedComputeStageDevices

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The collection of compute devices per stage that a request supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var supportedComputeStageDevices: [VNComputeStage : [MLComputeDevice]] { get throws }
```

## Discussion

A dictionary of per-stage compute devices; otherwise, `nil` if an error occurs.

## See Also

### Configuring the Compute Device
- [func setComputeDevice(MLComputeDevice?, for: VNComputeStage)](./setcomputedevice%28_,for%29.md)
  Assigns a compute device for a compute stage.
- [func computeDevice(for: VNComputeStage) -> MLComputeDevice?](./computedevice%28for%29.md)
  Returns the compute device for a compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/supportedcomputestagedevices)*