# OSFree

**Framework**: Kernel  
**Kind**: func

Frees a block of memory allocated by [`OSMalloc`](1398447-osmalloc.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
void OSFree(void *addr, uint32_t size, OSMallocTag tag);
```

## Parameters

- `addr`: A pointer to the memory block to free.
- `size`: The size of the memory block to free.
- `tag`: The   with which   was originally allocated.

## See Also

- [OSMalloc](1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).
- [OSMalloc_Tagalloc](1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](1398431-osmalloc_noblock.md).
- [bzero](1579350-bzero.md)
- [bzero_phys](1593364-bzero_phys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1398441-osfree)*