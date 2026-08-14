# VZVirtualMachineView

**Framework**: Virtualization  
**Kind**: class

A view that allows user interaction with a VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtualMachineView
```

#### Overview

The `VZVirtualMachineView` is a UI element that shows the contents of the VM frame buffer that you can optionally configure to respond to changes in the host’s display settings. If the VM configuration includes a keyboard and a pointing device, the view forwards keyboard and mouse events to the VM through those devices.

For a [`Sendable`](https://developer.apple.com/documentation/swift/sendable) wrapper that connects a virtual machine view to a virtual machine, see [`VZVirtualMachineViewAdaptor`](vzvirtualmachineviewadaptor.md).

## Topics

### Configuring a view adaptor
- [var adaptor: VZVirtualMachineViewAdaptor?](vzvirtualmachineview/adaptor.md)
  The virtual machine view adaptor.
### Configuring the VM
- [var automaticallyReconfiguresDisplay: Bool](vzvirtualmachineview/automaticallyreconfiguresdisplay.md)
  A Boolean value that indicates whether the graphics display associated with this view automatically reconfigures with respect to view changes.
- [var capturesSystemKeys: Bool](vzvirtualmachineview/capturessystemkeys.md)
  A Boolean value that determines whether the system should send certain system keyboard shortcuts to the guest instead of the host.
- [var virtualMachine: VZVirtualMachine?](vzvirtualmachineview/virtualmachine.md)
  The VM to display in the view.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## See Also

- [class VZVirtualMachine](vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview)*