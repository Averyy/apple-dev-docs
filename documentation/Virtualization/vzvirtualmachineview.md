# VZVirtualMachineView

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A view that allows user interaction with a VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtualMachineView
```

```objc
@interface VZVirtualMachineView : NSView
```

#### Overview

The `VZVirtualMachineView` is a UI element that shows the contents of the VM frame buffer that you can optionally configure to respond to changes in the host’s display settings. If the VM configuration includes a keyboard and a pointing device, the view forwards keyboard and mouse events to the VM through those devices.

For a [`Sendable`](../Swift/sendable.md) wrapper that connects a virtual machine view to a virtual machine, see [`VZVirtualMachineViewAdaptor`](./vzvirtualmachineviewadaptor.md).

## Topics

### Configuring a view adaptor
- [var adaptor: VZVirtualMachineViewAdaptor?](./vzvirtualmachineview/adaptor.md)
  The virtual machine view adaptor.
### Configuring the VM
- [var automaticallyReconfiguresDisplay: Bool](./vzvirtualmachineview/automaticallyreconfiguresdisplay.md)
  A Boolean value that indicates whether the graphics display associated with this view automatically reconfigures with respect to view changes.
- [var capturesSystemKeys: Bool](./vzvirtualmachineview/capturessystemkeys.md)
  A Boolean value that determines whether the system should send certain system keyboard shortcuts to the guest instead of the host.
- [var virtualMachine: VZVirtualMachine?](./vzvirtualmachineview/virtualmachine.md)
  The VM to display in the view.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)

## See Also

### Runtime
- [class VZVirtualMachine](./vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview)*