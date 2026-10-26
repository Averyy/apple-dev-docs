# GetPhysicalSegments

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the list of physical memory ranges this address space occupies on the local machine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*GetPhysicalSegments)(IOFireWireLibPhysicalAddressSpaceRef self, UInt32 *ioSegmentCount, IOByteCount outSegments[], IOPhysicalAddress outAddresses[]);
```

## Parameters

- `self`: The address space interface to use.
- `ioSegmentCount`: Pass in a pointer to the number of list entries in outSegments and outAddress. Upon completion, this will contain the actual number of segments returned in outSegments and outAddress
- `outSegments`: A pointer to an array to hold the function results. Upon completion, this will contain the lengths of the physical segments this address space occupies on the local machine
- `outAddresses`: A pointer to an array to hold the function results. Upon completion, this will contain the addresses of the physical segments this address space occupies on the local machine. If NULL, ioSegmentCount will contain the number of physical segments in the address space.

## See Also

### Miscellaneous
- [GetBuffer](./api-1556079-getbuffer.md)
  Get a pointer to the backing store for this address space
- [GetBufferSize](./api-1556116-getbuffersize.md)
  Get the size in bytes of this address space.
- [GetFWAddress](./api-1556030-getfwaddress.md)
  Get the FireWire address of this address space
- [GetPhysicalAddress](./api-1556049-getphysicaladdress.md)
  Returns the physical address of the beginning of this address space
- [GetPhysicalSegment](./api-1555592-getphysicalsegment.md)
  Returns the physical segment containing the address at a specified offset from the beginning of this address space


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirephysicaladdressspaceinterface/1555799-getphysicalsegments)*