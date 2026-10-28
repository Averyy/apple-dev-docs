# getLength

**Framework**: Kernel  
**Kind**: instm

Accessor to get the length of the memory descriptor (over all its ranges).

## Declaration

```cpp
virtual IOByteCount getLength() const;
```

## Return Value

The byte count.

## Overview

This method returns the total length of the memory described by the descriptor, ie. the sum of its ranges' lengths.

## See Also

### Getting the Descriptor Information
- [getDirection](./api-1812765-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [- getDirection](./api-1441925-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [- getLength](./api-1442036-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- GetLength](./api-3180642-getlength.md)
  Returns the length of the memory block represented by this object.
- [- getDMAMapLength](./api-3553361-getdmamaplength.md)
- [- getFlags](./api-2870265-getflags.md)
  Returns the options used to create the memory descriptor.
- [- getMetaClass](./api-1442096-getmetaclass.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812776-getlength)*