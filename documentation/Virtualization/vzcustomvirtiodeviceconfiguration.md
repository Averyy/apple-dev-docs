# VZCustomVirtioDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

An object that defines a custom Virtio Device configuration.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZCustomVirtioDeviceConfiguration
```

#### Overview

`VZCustomVirtioDeviceConfiguration` defines the configuration of a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md).

In order for a guest to be able to discover a Virtio device, you need to configure the following properties in the custom device configuration:

- [`deviceID`](vzcustomvirtiodeviceconfiguration/deviceid.md)
- [`pciClassID`](vzcustomvirtiodeviceconfiguration/pciclassid.md)
- [`pciSubclassID`](vzcustomvirtiodeviceconfiguration/pcisubclassid.md)
- [`virtioQueueCount`](vzcustomvirtiodeviceconfiguration/virtioqueuecount.md)

The remaining custom device configuration properties define additional features and configurations that are specific to the kind of Virtio device you’re defining.

If the `VZCustomVirtioDeviceConfiguration` you configure is valid, the Virtualization framework creates a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md) upon the creation of the [`VZVirtualMachine`](vzvirtualmachine.md). The framework notifies you upon creating the device by calling [`customVirtioConfiguration(_:didCreateDevice:)`](vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:).md) on the delegate method you provide.

## Topics

### Instance Properties
- [var deviceID: UInt16](vzcustomvirtiodeviceconfiguration/deviceid.md)
  The Virtio device ID of the device.
- [var deviceSpecificConfiguration: VZVirtioDeviceSpecificConfiguration?](vzcustomvirtiodeviceconfiguration/devicespecificconfiguration.md)
  The device-specific configuration for the device.
- [var mandatoryFeatures: VZVirtioFeatureSet](vzcustomvirtiodeviceconfiguration/mandatoryfeatures.md)
  The set of mandatory features that the device offers and the guest must accept.
- [var optionalFeatures: VZVirtioFeatureSet](vzcustomvirtiodeviceconfiguration/optionalfeatures.md)
  The set of optional features that the device offers.
- [var pciClassID: UInt8](vzcustomvirtiodeviceconfiguration/pciclassid.md)
  The PCI class ID of the device.
- [var pciSubclassID: UInt8](vzcustomvirtiodeviceconfiguration/pcisubclassid.md)
  The PCI subclass ID of the device.
- [var provider: VZCustomVirtioDeviceProvider?](vzcustomvirtiodeviceconfiguration/provider.md)
  The custom Virtio device provider.
- [var sharedMemoryRegions: [VZVirtioSharedMemoryRegionConfiguration]](vzcustomvirtiodeviceconfiguration/sharedmemoryregions.md)
  The list of shared memory regions.
- [var supportsSaveRestore: Bool](vzcustomvirtiodeviceconfiguration/supportssaverestore.md)
- [var virtioQueueCount: UInt16](vzcustomvirtiodeviceconfiguration/virtioqueuecount.md)
  The number of virtqueues (Virtio queues) on this device.
### Type Properties
- [class var maximumAllowedSharedMemoryRegionCount: Int](vzcustomvirtiodeviceconfiguration/maximumallowedsharedmemoryregioncount.md)
  The maximum number of Virtio shared memory regions the framework allows.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [protocol VZCustomVirtioDeviceConfigurationDelegate](vzcustomvirtiodeviceconfigurationdelegate.md)
  A class that conforms to the custom Virtio device configuration delegate protocol that can provide methods for tracking the state of a custom Virtio device configuration object.
- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZVirtioDeviceSpecificConfiguration](vzvirtiodevicespecificconfiguration.md)
  The device-specific configuration for a Virtio device


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration)*