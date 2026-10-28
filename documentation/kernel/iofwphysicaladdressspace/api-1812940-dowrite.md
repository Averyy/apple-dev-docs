# doWrite

**Framework**: Kernel  
**Kind**: instm

A method for processing an address space write request

## Declaration

```cpp
virtual UInt32 doWrite(
 UInt16nodeID,
 IOFWSpeed &speed,
 FWAddressaddr,
 UInt32len, 
 const void *buf,
 IOFWRequestRefConreqrefcon);
```

## Return Value

UIn32 returns kFWResponseComplete on success

## Parameters

- `nodeID`: FireWire Write to nodeID.
- `speed`: at this 'speed'.
- `addr`: with FireWire address 'addr'.
- `len`: write 'len' bytes to nodeID.
- `buf`: obtain bytes from location given by 'buf'.
- `reqrefcon`: Can be queried for extra info about the request.

## See Also

### Miscellaneous
- [checkMemoryInRange](./api-1812923-checkmemoryinrange.md)
  Validates the IOMemoryDescriptor, which is used to initialize the PhysicalAddressSpace.
- [complete](./api-1812928-complete.md)
  complete the IODMACommand used by this PhysicalAddressSpace.
- [doRead](./api-1812935-doread.md)
  A method for processing an address space read request
- [getDMACommand](./api-1812943-getdmacommand.md)
  Get the DMACommand from this PhysicalAddressSpace.
- [getLength](./api-1812947-getlength.md)
  Get the length of the memory backed by PhysicalAddressSpace.
- [getMemoryDescriptor](./api-1812953-getmemorydescriptor.md)
  Gets the memory descriptor, which is associated to this PhysicalAddressSpace.
- [getSegments](./api-1812956-getsegments.md)
  Returns the scatter gather list of memory segments from the IODMACommand used in this PhysicalAddressSpace.
- [init](./api-1812960-init.md)
  Initialize physical address space.
- [initWithDesc](./api-1812962-initwithdesc.md)
  Initialize physical address space with IOMemoryDescriptor.
- [initWithDMACommand](./api-1812968-initwithdmacommand.md)
  Initialize physical address space with IODMACommand.
- [isPrepared](./api-1812974-isprepared.md)
  Inspects whether the IODMACommand was prepared in this PhysicalAddressSpace.
- [prepare](./api-1812981-prepare.md)
  Prepare the IODMACommand used by this PhysicalAddressSpace.
- [setDMACommand](./api-1812990-setdmacommand.md)
  Set the DMACommand for this PhysicalAddressSpace.
- [setMemoryDescriptor](./api-1813001-setmemorydescriptor.md)
  Sets the memory descriptor, which will be associated to this PhysicalAddressSpace.
- [synchronize](./api-1813014-synchronize.md)
  synchronize the IODMACommand used by this PhysicalAddressSpace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwphysicaladdressspace/1812940-dowrite)*