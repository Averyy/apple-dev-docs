# optionalFeatures

**Framework**: Virtualization  
**Kind**: property

The set of optional features that the device offers.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var optionalFeatures: VZVirtioFeatureSet { get }
```

#### Discussion

The optional features are the set of features that the guest driver may or may not accept, see [`negotiatedFeatures`](vzcustomvirtiodevice/negotiatedfeatures.md) for the set of features that the guest accepts. A few feature bits are always set internally by default for optimal performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/optionalfeatures)*