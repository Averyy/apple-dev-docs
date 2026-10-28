# supportedComputeStageDevicesAndReturnError:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

The collection of compute devices per stage that a request supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (NSDictionary<NSString *,NSArray<id<MLComputeDeviceProtocol>> *> *) supportedComputeStageDevicesAndReturnError:(NSError **) error;
```

## Return Value

A dictionary of per-stage compute devices; otherwise, `nil` if an error occurs.

## See Also

### Configuring the Compute Device
- [- setComputeDevice:forComputeStage:](./setcomputedevice_forcomputestage_.md)
  Assigns a compute device for a compute stage.
- [- computeDeviceForComputeStage:](./computedeviceforcomputestage_.md)
  Returns the compute device for a compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/supportedcomputestagedevicesandreturnerror:)*