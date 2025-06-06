# setComputeDevice(_:for:)

**Framework**: Vision  
**Kind**: method

Assigns a compute device for a compute stage.

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
func setComputeDevice(_ computeDevice: MLComputeDevice?, for computeStage: VNComputeStage)
```

#### Discussion

If the parameter `computeDevice` is `nil`, the framework removes any explicit compute device assignment and allows the framework to select the device.

Configure any compute device for a given compute stage. When performing a request, the system makes a validity check. Call [`supportedComputeStageDevices`](vnrequest/supportedcomputestagedevices.md) to get valid compute devices for a request’s compute stages.

## Parameters

- `computeDevice`: The compute device to assign to the compute stage.
- `computeStage`: The compute stage.

## See Also

- [func computeDevice(for: VNComputeStage) -> MLComputeDevice?](vnrequest/computedevice(for:).md)
  Returns the compute device for a compute stage.
- [var supportedComputeStageDevices: [VNComputeStage : [MLComputeDevice]]](vnrequest/supportedcomputestagedevices.md)
  The collection of compute devices per stage that a request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/setcomputedevice(_:for:))*