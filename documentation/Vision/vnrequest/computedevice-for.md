# computeDevice(for:)

**Framework**: Vision  
**Kind**: method

Returns the compute device for a compute stage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
func computeDevice(for computeStage: VNComputeStage) -> MLComputeDevice?
```

#### Return Value

The current compute device; otherwise, `nil` if one isn’t assigned.

## Parameters

- `computeStage`: The compute stage to inspect.

## See Also

- [func setComputeDevice(MLComputeDevice?, for: VNComputeStage)](vnrequest/setcomputedevice(_:for:).md)
  Assigns a compute device for a compute stage.
- [var supportedComputeStageDevices: [VNComputeStage : [MLComputeDevice]]](vnrequest/supportedcomputestagedevices.md)
  The collection of compute devices per stage that a request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/computedevice(for:))*