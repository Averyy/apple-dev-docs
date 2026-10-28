# IOAGPDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An IOService class representing an AGP primary device.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```cpp
class IOAGPDevice : IOPCIDevice
```

## Overview

The discovery of an AGP primary device by the PCI bus family results in an instance of the IOAGPDevice being created and published. It provides services specific to AGP, in addition to the PCI services supplied by its superclass IOPCIDevice.

## Topics

### Miscellaneous
- [commitAGPMemory](./ioagpdevice/api-1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](./ioagpdevice/api-1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](./ioagpdevice/api-1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](./ioagpdevice/api-1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](./ioagpdevice/api-1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](./ioagpdevice/api-1811928-getagpstatus.md)
  Returns the current state of the AGP bus.
- [releaseAGPMemory](./ioagpdevice/api-1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioagpdevice/reserved.md)
### Instance Methods
- [- commitAGPMemory](./ioagpdevice/api-1580678-commitagpmemory.md)
- [- createAGPSpace](./ioagpdevice/api-1580693-createagpspace.md)
- [- destroyAGPSpace](./ioagpdevice/api-1580697-destroyagpspace.md)
- [- getAGPRangeAllocator](./ioagpdevice/api-1580694-getagprangeallocator.md)
- [- getAGPSpace](./ioagpdevice/api-1580706-getagpspace.md)
- [- getAGPStatus](./ioagpdevice/api-1580708-getagpstatus.md)
- [- getMetaClass](./ioagpdevice/api-1580675-getmetaclass.md)
- [- releaseAGPMemory](./ioagpdevice/api-1580699-releaseagpmemory.md)
- [- resetAGP](./ioagpdevice/api-1580690-resetagp.md)

## Relationships

### Inherits From
- [IOPCIDevice](./iopcidevice.md)

## See Also

### Devices
- [Implementing a PCIe Kext for a Thunderbolt Device](./hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device.md)
  Create an IOKit driver to support Thunderbolt devices that implement features not supported in PCIDriverKit, such as wireless networking or audio. 
- [IOPCIDevice](./iopcidevice.md)
  An IOService class representing a PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice)*