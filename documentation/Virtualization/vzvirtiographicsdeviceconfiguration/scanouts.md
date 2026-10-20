# scanouts

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The array of output devices.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var scanouts: [VZVirtioGraphicsScanoutConfiguration] { get set }
```

```objc
@property (copy) NSArray<VZVirtioGraphicsScanoutConfiguration *> * scanouts;
```

## See Also

### Instance properties
- [class VZVirtioGraphicsScanoutConfiguration](../vzvirtiographicsscanoutconfiguration.md)
  The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiographicsdeviceconfiguration/scanouts)*