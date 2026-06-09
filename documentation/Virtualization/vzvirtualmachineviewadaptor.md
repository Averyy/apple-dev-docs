# VZVirtualMachineViewAdaptor

**Framework**: Virtualization  
**Kind**: struct

A sendable wrapper that connects a virtual machine view to a virtual machine.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct VZVirtualMachineViewAdaptor
```

#### Discussion

`VZVirtualMachineViewAdaptor` enables Swift 6 strict concurrency when using [`VZVirtualMachineView`](vzvirtualmachineview.md). Since [`VZVirtualMachine`](vzvirtualmachine.md) operates on a specific dispatch queue and is not [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable), assigning it directly to [`virtualMachine`](vzvirtualmachineview/virtualmachine.md) would be a compiler error when crossing isolation boundaries. The adaptor holds a strong reference to the virtual machine, allowing you to  safely copy it  across actor boundaries.

The following example demonstrates how to create and run a `VZVirtualMachineViewAdaptor` from the main actor.

```swift
    // Create an adaptor from a virtual machine.
    let adaptor = VZVirtualMachineViewAdaptor(virtualMachine: vm)


    // Pass the adaptor to a view on the main actor.
    await MainActor.run {
        view.adaptor = adaptor
    }
```

## Topics

### Initializers
- [init(virtualMachine: VZVirtualMachine)](vzvirtualmachineviewadaptor/init(virtualmachine:).md)
  Initialize an adaptor for a virtual machine.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VZGraphicsDevice](vzgraphicsdevice.md)
  A class that represents a graphics device in a VM.
- [class VZGraphicsDisplay](vzgraphicsdisplay.md)
  A class that represents a graphics display in a VM.
- [class VZMacGraphicsDevice](vzmacgraphicsdevice.md)
  An object that represents a Mac graphics device.
- [class VZVirtioGraphicsScanout](vzvirtiographicsscanout.md)
  A Virtio graphics scanout that corresponds to a Virtio graphics scanout configuration.
- [class VZMacGraphicsDisplay](vzmacgraphicsdisplay.md)
  An object that represents the graphics display on a Mac.
- [class VZVirtioGraphicsDevice](vzvirtiographicsdevice.md)
  A Virtio graphics device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineviewadaptor)*