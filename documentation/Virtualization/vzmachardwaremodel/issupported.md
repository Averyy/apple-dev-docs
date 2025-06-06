# isSupported

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the host supports this hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isSupported: Bool { get }
```

#### Discussion

If this hardware model isn’t supported by the host, the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) won’t validate.

The validation error of the `VZVirtualMachineConfiguration` provides more information about why the hardware model isn’t supported.

## See Also

- [var dataRepresentation: Data](vzmachardwaremodel/datarepresentation.md)
  Returns the opaque data representation of the hardware model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmachardwaremodel/issupported)*