# provider

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The custom Virtio device provider.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var provider: VZCustomVirtioDeviceProvider? { get set }
```

```objc
@property (strong, readwrite, nullable) VZCustomVirtioDeviceProvider * provider;
```

## Discussion

This data defines how the virtual device is implemented.

## See Also

### Related Documentation
- [class VZCustomVirtioDeviceDelegateProvider](../vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/provider)*