# GetBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Get a pointer to the backing store for this address space

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void *(*GetBuffer)(IOFireWireLibPhysicalAddressSpaceRef self);
```

## Return Value

A pointer to the backing store of this address space.

## Parameters

- `self`: The address space interface to use.

## See Also

### Miscellaneous
- [GetBufferSize](./api-1556116-getbuffersize.md)
  Get the size in bytes of this address space.
- [GetFWAddress](./api-1556030-getfwaddress.md)
  Get the FireWire address of this address space
- [GetPhysicalAddress](./api-1556049-getphysicaladdress.md)
  Returns the physical address of the beginning of this address space
- [GetPhysicalSegment](./api-1555592-getphysicalsegment.md)
  Returns the physical segment containing the address at a specified offset from the beginning of this address space
- [GetPhysicalSegments](./api-1555799-getphysicalsegments.md)
  Returns the list of physical memory ranges this address space occupies on the local machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirephysicaladdressspaceinterface/1556079-getbuffer)*