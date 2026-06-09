# VZGuestMemoryMapping

**Framework**: Virtualization  
**Kind**: class

An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZGuestMemoryMapping
```

#### Overview

A `VZGuestMemoryMapping` object provides read and write access to guest’s DRAM for a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md) for Virtio devices that need to directly interact with the guest’s DRAM.

Don’t instantiate a`VZGuestMemoryMapping` objects directly. Instead, call the [`guestMemoryMapping(atPhysicalAddress:length:)`](vzcustomvirtiodevice/guestmemorymapping(atphysicaladdress:length:).md) method and the framework creates a `VZGuestMemoryMapping` object for you.

Throughout its lifetime, a `VZGuestMemoryMapping` object holds a reference to the all of the host memory allocated for the guest’s DRAM. When the virtual machine is rebooted or shutdown, the allocated host memory becomes invalidated and remapped. As such, an instance of `VZGuestMemoryMapping` can’t be used across a reboot or shutdown of the virtual machine.

## Topics

### Instance Properties
- [var length: Int](vzguestmemorymapping/length.md)
  The number of bytes contained by this guest memory mapping object.
- [var mutableBytes: UnsafeMutableRawPointer](vzguestmemorymapping/mutablebytes.md)
  A pointer to the data this guest memory mapping object contains.
- [var physicalAddress: UInt64](vzguestmemorymapping/physicaladdress.md)
  The guest’s physical memory base address of this guest memory mapping object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.
- [class VZGuestProvisioningOptions](vzguestprovisioningoptions.md)
  The base class for guest provisioning options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzguestmemorymapping)*