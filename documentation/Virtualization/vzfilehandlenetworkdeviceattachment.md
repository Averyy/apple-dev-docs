# VZFileHandleNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

A network device that transmits raw network packets and frames using a datagram socket.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZFileHandleNetworkDeviceAttachment
```

#### Overview

A [`VZFileHandleNetworkDeviceAttachment`](vzfilehandlenetworkdeviceattachment.md) object maps a network interface to a connected datagram socket. This attachment transmits data at the data link layer. You configure and manage the socket in your app, and manage the corresponding data transfers.

To configure a network device with a socket-based file handle:

1. Create a socket with the `SOCK_DGRAM` type in your app.
2. Create a [`FileHandle`](https://developer.apple.com/documentation/Foundation/FileHandle) from the socket’s file descriptor.
3. Create the [`VZFileHandleNetworkDeviceAttachment`](vzfilehandlenetworkdeviceattachment.md) object using the file handle.
4. Assign the attachment object to the [`attachment`](vznetworkdeviceconfiguration/attachment.md) property of a [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md) object.
5. Add the [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md) object to the [`networkDevices`](vzvirtualmachineconfiguration/networkdevices.md) property of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md).

This attachment doesn’t require your app to have the [`com.apple.vm.networking`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.networking) entitlement.

## Topics

### Creating the attachment point
- [init(fileHandle: FileHandle)](vzfilehandlenetworkdeviceattachment/init(filehandle:).md)
  Creates the attachment from a file handle that contains a connected datagram socket.
### Getting the file handle
- [var fileHandle: FileHandle](vzfilehandlenetworkdeviceattachment/filehandle.md)
  The file handle assigned to this attachment.
### Specifying the network packet size
- [var maximumTransmissionUnit: Int](vzfilehandlenetworkdeviceattachment/maximumtransmissionunit.md)
  An integer value that indicates the maximum transmission unit (MTU) associated with this attachment.

## Relationships

### Inherits From
- [VZNetworkDeviceAttachment](vznetworkdeviceattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZBridgedNetworkDeviceAttachment](vzbridgednetworkdeviceattachment.md)
  A network device that interacts directly with a physical network interface on the host computer.
- [class VZNATNetworkDeviceAttachment](vznatnetworkdeviceattachment.md)
  A device that routes network requests through the host computer and performs network address translation on the resulting packets.
- [class VZVmnetNetworkDeviceAttachment](vzvmnetnetworkdeviceattachment.md)
  A network device attachment that allows a custom network topology.
- [class VZNetworkDeviceAttachment](vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandlenetworkdeviceattachment)*