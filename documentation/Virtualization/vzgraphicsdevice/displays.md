# displays

**Framework**: Virtualization  
**Kind**: property

The list of graphics displays configured for this graphics device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var displays: [VZGraphicsDisplay] { get }
```

#### Discussion

This is a list of the graphics displays configured on the graphics device configuration.

## See Also

- [class VZMacGraphicsDisplayConfiguration](vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZVirtioGraphicsScanoutConfiguration](vzvirtiographicsscanoutconfiguration.md)
  The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdevice/displays)*