# negotiatedFeatures

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The set of features that the driver and the device have successfully negotiated, or `nil` if no feature negotiation has taken place.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var negotiatedFeatures: VZNegotiatedVirtioFeatureSet? { get }
```

```objc
@property (readonly, nullable) VZNegotiatedVirtioFeatureSet * negotiatedFeatures;
```

## Discussion

The value is only valid after the framework calls [`customVirtioDeviceDidAcceptDriverOk(_:)`](../vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok%28_%29.md). The framework calls this method when the guest driver sets `DRIVER_OK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/negotiatedfeatures)*