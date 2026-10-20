# flags

**Framework**: Kernel  
**Kind**: structp

PREALLOCATE: preallocate allocation blocks. ALLOCATECONTIG: allocate contigious space. ALLOCATEALL: allocate all requested space or no space at all. FREEREMAINDER: deallocate allocated but unfilled blocks. ALLOCATEFROMPEOF: allocate from the physical eof. ALLOCATEFROMVOL: allocate from the volume offset.

## See Also

### Fields
- [vp](./api-1807403-vp.md)
  The vnode for which to preallocate space.
- [length](./api-1807414-length.md)
  Desired preallocated file length.
- [bytesallocated](./api-1807437-bytesallocated.md)
  Additional bytes set aside for file. Set to 0 if none are allocated OR if the file is contracted.
- [offset](./api-1807450-offset.md)
  Hint for where to find free blocks.
- [ctx](./api-1807464-ctx.md)
  Context to authenticate for allocation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vnop_pagein_args/1807426-flags)*