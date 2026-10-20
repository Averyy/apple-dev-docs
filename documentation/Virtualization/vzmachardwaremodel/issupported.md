# isSupported

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the host supports this hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isSupported: Bool { get }
```

```objc
@property (readonly, getter=isSupported) BOOL supported;
```

#### Discussion

If this hardware model isn’t supported by the host, the [`VZVirtualMachineConfiguration`](../vzvirtualmachineconfiguration.md) won’t validate.

The validation error of the `VZVirtualMachineConfiguration` provides more information about why the hardware model isn’t supported.

## See Also

### Configuring the hardware model
- [var dataRepresentation: Data](./datarepresentation.md)
  Returns the opaque data representation of the hardware model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmachardwaremodel/issupported)*