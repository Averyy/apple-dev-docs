# negotiatedFeatures

**Framework**: Virtualization  
**Kind**: property

The set of features that the driver and the device have successfully negotiated, or `nil` if no feature negotiation has taken place.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var negotiatedFeatures: VZNegotiatedVirtioFeatureSet? { get }
```

#### Discussion

The value is only valid after the framework calls [`customVirtioDeviceDidAcceptDriverOk(_:)`](vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok(_:).md). The framework calls this method when the guest driver sets `DRIVER_OK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/negotiatedfeatures)*