# OSMalloc_Tagfree

**Framework**: Kernel  
**Kind**: func

Frees a tag used with OSMalloc functions.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void OSMalloc_Tagfree(OSMallocTag tag);
```

#### Discussion

OSMalloc tags must not be freed while any memory blocks allocated with them still exist. Any OSMalloc function called on those blocks will result in a panic.

## Parameters

- `tag`: The   to free.

## See Also

- [OSMalloc](1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).
- [OSMalloc_Tagalloc](1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_noblock](1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](1398431-osmalloc_noblock.md).
- [OSFree](1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](1398447-osmalloc.md).
- [bzero](1579350-bzero.md)
- [bzero_phys](1593364-bzero_phys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1398439-osmalloc_tagfree)*