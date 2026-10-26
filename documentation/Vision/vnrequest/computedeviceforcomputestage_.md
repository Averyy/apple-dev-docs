# computeDeviceForComputeStage:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the compute device for a compute stage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (id<MLComputeDeviceProtocol>) computeDeviceForComputeStage:(VNComputeStage) computeStage;
```

#### Return Value

The current compute device; otherwise, `nil` if one isn’t assigned.

## Parameters

- `computeStage`: The compute stage to inspect.

## See Also

### Configuring the Compute Device
- [- setComputeDevice:forComputeStage:](./setcomputedevice_forcomputestage_.md)
  Assigns a compute device for a compute stage.
- [- supportedComputeStageDevicesAndReturnError:](./supportedcomputestagedevicesandreturnerror_.md)
  The collection of compute devices per stage that a request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/computedeviceforcomputestage:)*