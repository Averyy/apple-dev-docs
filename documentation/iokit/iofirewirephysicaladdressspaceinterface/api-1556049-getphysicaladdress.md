# GetPhysicalAddress

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the physical address of the beginning of this address space

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOPhysicalAddress (*GetPhysicalAddress)(IOFireWireLibPhysicalAddressSpaceRef self);
```

## Return Value

The physical address of the start of this address space

## Parameters

- `self`: The address space interface to use.

## See Also

### Miscellaneous
- [GetBuffer](./api-1556079-getbuffer.md)
  Get a pointer to the backing store for this address space
- [GetBufferSize](./api-1556116-getbuffersize.md)
  Get the size in bytes of this address space.
- [GetFWAddress](./api-1556030-getfwaddress.md)
  Get the FireWire address of this address space
- [GetPhysicalSegment](./api-1555592-getphysicalsegment.md)
  Returns the physical segment containing the address at a specified offset from the beginning of this address space
- [GetPhysicalSegments](./api-1555799-getphysicalsegments.md)
  Returns the list of physical memory ranges this address space occupies on the local machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirephysicaladdressspaceinterface/1556049-getphysicaladdress)*