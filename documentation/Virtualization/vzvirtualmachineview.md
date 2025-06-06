# VZVirtualMachineView

**Framework**: Virtualization  
**Kind**: class

A view that allows user interaction with a VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
class VZVirtualMachineView
```

#### Overview

The `VZVirtualMachineView` is a UI element that shows the contents of the VM frame buffer that you can optionally configure to respond to changes in the host’s display settings. If the VM configuration includes a keyboard and a pointing device, the view forwards keyboard and mouse events to the VM through those devices.

## Topics

### Configuring the VM
- [var automaticallyReconfiguresDisplay: Bool](vzvirtualmachineview/automaticallyreconfiguresdisplay.md)
  A Boolean value that indicates whether the graphics display associated with this view automatically reconfigures with respect to view changes.
- [var capturesSystemKeys: Bool](vzvirtualmachineview/capturessystemkeys.md)
  A Boolean value that determines whether the system should send certain system keyboard shortcuts to the guest instead of the host.
- [var virtualMachine: VZVirtualMachine?](vzvirtualmachineview/virtualmachine.md)
  The VM to display in the view.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [class VZVirtualMachine](vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview)*