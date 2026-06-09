# mandatoryFeatures

**Framework**: Virtualization  
**Kind**: property

The set of mandatory features that the device offers and the guest must accept.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var mandatoryFeatures: VZVirtioFeatureSet { get }
```

#### Discussion

The mandatory features are the set of features that the device offers and the guest must accept. The framework won’t successfully initialize the device if the guest driver fails to accept this set of features. The feature bit `VIRTIO_F_VERSION_1` is always set to `1` internally by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/mandatoryfeatures)*