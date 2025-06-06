# VZNetworkBlockDeviceStorageDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

A storage device attachment backed by a Network Block Device (NBD) client.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZNetworkBlockDeviceStorageDeviceAttachment
```

#### Overview

This storage device attachment provides a Network Block Device (NBD) client implementation. The NBD client connects to an NBD server referred to by an NBD Uniform Resource Indicator (URI), represented as an URL in this API. The NBD server runs outside of and isn’t controlled by the Virtualization framework. The NBD client forwards the guest’s I/O operations to the NBD server, which handles the I/O operations.

The NBD client attempts to connect to the NBD server referred to by the URL used when you started the VM with [`start()`](vzvirtualmachine/start().md). However, it’s important to note that a connection attempt isn’t made when the framework initializes the attachment object.

Reconnection attempts take place throughout the life cycle of the VM when the NBD client encounters a recoverable error such as connection timeout and unexpected connection errors. The NBD client disconnects from the server when the VM shuts down.

Using this attachment requires the app to have the [`com.apple.security.network.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.network.client) entitlement because this attachment opens an outgoing network connection.

To create a device that uses an NBD service, first initialize a `VZNetworkBlockDeviceStorageDeviceAttachment` with the URI of an NBD server, then use the attachment to configure a [`VZStorageDeviceConfiguration`](vzstoragedeviceconfiguration.md) as shown in the example below (the attachment works with any subclass of [`VZStorageDeviceConfiguration`](vzstoragedeviceconfiguration.md), not just [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md)):

For more information about Network Block Devices, see the [`Network Block Device Specification`](https://developer.apple.comhttps://github.com/NetworkBlockDevice/nbd/blob/master/doc/proto.md) on GitHub.

For more information about the NBD URL format, see the [`Network Block Device URL specification`](https://developer.apple.comhttps://github.com/NetworkBlockDevice/nbd/blob/master/doc/uri.md) on GitHub.

## Topics

### Creating network block device attachments
- [convenience init(url: URL) throws](vznetworkblockdevicestoragedeviceattachment/init(url:).md)
  Creates a new network block device (NBD) storage attachment from an NDB Uniform Resource Indicator (URI) represented as a URL that you provide.
- [init(url: URL, timeout: TimeInterval, isForcedReadOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws](vznetworkblockdevicestoragedeviceattachment/init(url:timeout:isforcedreadonly:synchronizationmode:).md)
  Creates a new network block device storage attachment from an NBD Uniform Resource Indicator (URI) represented as a URL, timeout value, and read-only and synchronization modes that you provide.
### Validating a network block device’s URL
- [class func validate(URL) throws](vznetworkblockdevicestoragedeviceattachment/validate(_:).md)
  Checks if the URL is a valid network block device URL.
### Getting information about the attachment point
- [var isForcedReadOnly: Bool](vznetworkblockdevicestoragedeviceattachment/isforcedreadonly.md)
  Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.
- [var synchronizationMode: VZDiskSynchronizationMode](vznetworkblockdevicestoragedeviceattachment/synchronizationmode.md)
  The mode in which the NBD client synchronizes data with the NBD server.
- [var timeout: TimeInterval](vznetworkblockdevicestoragedeviceattachment/timeout.md)
  The timeout value in seconds for the connection between the client and server.
- [var url: URL](vznetworkblockdevicestoragedeviceattachment/url.md)
  The URL that refers to the NBD server to which the NBD client will connect.
### Observing changes to the network block device
- [var delegate: (any VZNetworkBlockDeviceStorageDeviceAttachmentDelegate)?](vznetworkblockdevicestoragedeviceattachment/delegate.md)
  The object that receives messages about changes to the network block device attachment.
- [protocol VZNetworkBlockDeviceStorageDeviceAttachmentDelegate](vznetworkblockdevicestoragedeviceattachmentdelegate.md)
  Methods you implement to respond to changes to a network block device attachment.

## Relationships

### Inherits From
- [VZStorageDeviceAttachment](vzstoragedeviceattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZDiskBlockDeviceStorageDeviceAttachment](vzdiskblockdevicestoragedeviceattachment.md)
  A storage device attachment that uses a disk to store data.
- [class VZDiskImageStorageDeviceAttachment](vzdiskimagestoragedeviceattachment.md)
  A device that stores content in a disk image.
- [class VZStorageDeviceAttachment](vzstoragedeviceattachment.md)
  The common behaviors for storage devices in the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment)*