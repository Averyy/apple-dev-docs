# initWithDMACommand

**Framework**: Kernel  
**Kind**: instm

Initialize physical address space with IODMACommand.

## Declaration

```swift
virtual bool initWithDMACommand(
 IOFireWireBus *bus,
 IODMACommand *command );
```

#### Return_value

returns true if success, else false

## Parameters

- `bus`: Points to IOFireWireBus object.
- `command`: Points to IODMACommand.

## See Also

- [checkMemoryInRange](iofwphysicaladdressspace/1812923-checkmemoryinrange.md)
  Validates the IOMemoryDescriptor, which is used to initialize the PhysicalAddressSpace.
- [complete](iofwphysicaladdressspace/1812928-complete.md)
  complete the IODMACommand used by this PhysicalAddressSpace.
- [doRead](iofwphysicaladdressspace/1812935-doread.md)
  A method for processing an address space read request
- [doWrite](iofwphysicaladdressspace/1812940-dowrite.md)
  A method for processing an address space write request
- [getDMACommand](iofwphysicaladdressspace/1812943-getdmacommand.md)
  Get the DMACommand from this PhysicalAddressSpace.
- [getLength](iofwphysicaladdressspace/1812947-getlength.md)
  Get the length of the memory backed by PhysicalAddressSpace.
- [getMemoryDescriptor](iofwphysicaladdressspace/1812953-getmemorydescriptor.md)
  Gets the memory descriptor, which is associated to this PhysicalAddressSpace.
- [getSegments](iofwphysicaladdressspace/1812956-getsegments.md)
  Returns the scatter gather list of memory segments from the IODMACommand used in this PhysicalAddressSpace.
- [init](iofwphysicaladdressspace/1812960-init.md)
  Initialize physical address space.
- [initWithDesc](iofwphysicaladdressspace/1812962-initwithdesc.md)
  Initialize physical address space with IOMemoryDescriptor.
- [isPrepared](iofwphysicaladdressspace/1812974-isprepared.md)
  Inspects whether the IODMACommand was prepared in this PhysicalAddressSpace.
- [prepare](iofwphysicaladdressspace/1812981-prepare.md)
  Prepare the IODMACommand used by this PhysicalAddressSpace.
- [setDMACommand](iofwphysicaladdressspace/1812990-setdmacommand.md)
  Set the DMACommand for this PhysicalAddressSpace.
- [setMemoryDescriptor](iofwphysicaladdressspace/1813001-setmemorydescriptor.md)
  Sets the memory descriptor, which will be associated to this PhysicalAddressSpace.
- [synchronize](iofwphysicaladdressspace/1813014-synchronize.md)
  synchronize the IODMACommand used by this PhysicalAddressSpace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwphysicaladdressspace/1812968-initwithdmacommand)*