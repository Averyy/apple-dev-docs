# setComputeDevice(_:for:)

**Framework**: Vision  
**Kind**: method  
**Required**: Yes

Assigns a compute device for a compute stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
mutating func setComputeDevice(_ computeDevice: MLComputeDevice?, for computeStage: ComputeStage)
```

#### Discussion

If the parameter `computeDevice` is `nil`, the framework removes any explicit compute device assignment and allows the framework to select the device.

Configure any compute device for a given compute stage. When performing a request, the system makes a validity check. Use [`supportedComputeStageDevices`](visionrequest/supportedcomputestagedevices.md) to get valid compute devices for a request’s compute stages.

## Parameters

- `computeDevice`: The compute device to assign to the compute stage.
- `computeStage`: The compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionrequest/setcomputedevice(_:for:))*