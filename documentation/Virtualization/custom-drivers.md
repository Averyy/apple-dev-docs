# Custom Virtio drivers

**Framework**: Virtualization

Create custom Virtio drivers for Linux virtual machines.

## Topics

### Creating and configuring Virtio drivers
- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZCustomVirtioDeviceConfiguration](vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.
- [class VZVirtioDeviceSpecificConfiguration](vzvirtiodevicespecificconfiguration.md)
  The device-specific configuration for a Virtio device
### Responding to Virtio driver events
- [class VZCustomVirtioDeviceDelegateProvider](vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.
- [class VZCustomVirtioDeviceProvider](vzcustomvirtiodeviceprovider.md)
  A base class that describes the provider of a custom Virtio device.
### Working with VirtQueues
- [class VZVirtioQueue](vzvirtioqueue.md)
  A Virtio queue.
- [class VZVirtioQueueElement](vzvirtioqueueelement.md)
  A unit of work on a Virtio queue, also known as a descriptor chain.
### Specifying driver features
- [class VZVirtioFeatureSet](vzvirtiofeatureset.md)
  Values that represent a set of Virtio feature bits.
- [class VZNegotiatedVirtioFeatureSet](vznegotiatedvirtiofeatureset.md)
  Values that represent a set of negotiated Virtio feature bits.
### Managing shared memory
- [class VZVirtioSharedMemoryRegion](vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.
- [class VZVirtioSharedMemoryRegionConfiguration](vzvirtiosharedmemoryregionconfiguration.md)
  The configuration of a Virtio shared memory region.
### Responding to Virtio events
- [protocol VZCustomVirtioDeviceConfigurationDelegate](vzcustomvirtiodeviceconfigurationdelegate.md)
  A class that conforms to the custom Virtio device configuration delegate protocol that can provide methods for tracking the state of a custom Virtio device configuration object.
- [protocol VZCustomVirtioDeviceDelegate](vzcustomvirtiodevicedelegate.md)
  A delegate protocol that defines the methods you implement to respond to the life cycle events of a custom Virtio device.

## See Also

- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
- [Memory](memory.md)
  Configure a memory balloon device to change the allocated memory for the guest system.
- [Network](network.md)
  Configure the devices that connect the guest system to the network.
- [Randomization](randomization.md)
  Configure a device for the guest system to use to generate random numbers.
- [Serial ports](serial-ports.md)
  Configure the serial devices that you use to communicate with the guest system.
- [Shared directories](shared-directories.md)
  Configure devices that share directories from the host into the guest system.
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/custom-drivers)*