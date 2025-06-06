# virtualMachine(_:networkDevice:attachmentWasDisconnectedWithError:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when an error causes a VM’s network attachment to disconnect.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func virtualMachine(_ virtualMachine: VZVirtualMachine, networkDevice: VZNetworkDevice, attachmentWasDisconnectedWithError error: any Error)
```

#### Discussion

The system invokes this method when the network interface fails to start, which results in the disconnection of the network attachment. This can happen in many situations such as initial boot, device reset, reboot, and so on. The system may invoke this method several times during a VM’s life cycle. After the system calls this method, the [`attachment`](vznetworkdevice/attachment.md) property is `nil`.

## Parameters

- `virtualMachine`: The VM invoking the delegate method.
- `networkDevice`: The disconnected network device.
- `error`: The error that describes why the virtual machine disconnected the network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate/virtualmachine(_:networkdevice:attachmentwasdisconnectedwitherror:))*