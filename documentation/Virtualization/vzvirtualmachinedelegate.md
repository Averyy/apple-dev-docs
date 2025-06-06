# VZVirtualMachineDelegate

**Framework**: Virtualization  
**Kind**: protocol

The methods you use to respond to changes in the state of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
protocol VZVirtualMachineDelegate : NSObjectProtocol
```

## Topics

### Stopping the VM
- [func guestDidStop(VZVirtualMachine)](vzvirtualmachinedelegate/guestdidstop(_:).md)
  Tells the delegate that the guest operating system stopped the VM.
- [func virtualMachine(VZVirtualMachine, didStopWithError: any Error)](vzvirtualmachinedelegate/virtualmachine(_:didstopwitherror:).md)
  Tells the delegate that the VM stopped because of an error.
### Responding to network device errors
- [func virtualMachine(VZVirtualMachine, networkDevice: VZNetworkDevice, attachmentWasDisconnectedWithError: any Error)](vzvirtualmachinedelegate/virtualmachine(_:networkdevice:attachmentwasdisconnectedwitherror:).md)
  The method the framework calls when an error causes a VM’s network attachment to disconnect.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any VZVirtualMachineDelegate)?](vzvirtualmachine/delegate.md)
  A custom object you use to determine when the VM stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate)*