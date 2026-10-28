# computeDevice(for:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the compute device for a compute stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
func computeDevice(for computeStage: ComputeStage) -> MLComputeDevice?
```

## Return Value

The current compute device; otherwise, `nil` if one isn’t assigned.

## Parameters

- `computeStage`: The compute stage to inspect.

## Default Implementations

### VisionRequest Implementations
- [func computeDevice(for: ComputeStage) -> MLComputeDevice?](./computedevice%28for%29-52l0g.md)
  Returns the compute device for a compute stage.

## See Also

### Getting the compute device
- [var supportedComputeStageDevices: [ComputeStage : [MLComputeDevice]]](./supportedcomputestagedevices.md)
  The collection of compute devices per stage that a request supports.
- [enum ComputeStage](../computestage.md)
  Types that represent the compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionrequest/computedevice(for:))*