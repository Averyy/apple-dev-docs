# OSMalloc_nowait

**Framework**: Kernel  
**Kind**: func

Equivalent to [`OSMalloc_noblock`](1398431-osmalloc_noblock.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
void * OSMalloc_nowait(uint32_t size, OSMallocTag tag);
```

## See Also

- [OSMalloc](1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).
- [OSMalloc_Tagalloc](1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md), returning `NULL` if it would block.
- [OSFree](1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](1398447-osmalloc.md).
- [bzero](1579350-bzero.md)
- [bzero_phys](1593364-bzero_phys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1398445-osmalloc_nowait)*