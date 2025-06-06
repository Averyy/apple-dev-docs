# OSMalloc

**Framework**: Kernel  
**Kind**: func

Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
void * OSMalloc(uint32_t size, OSMallocTag tag);
```

#### Return_value

A pointer to the memory on success, `NULL` on failure.

#### Discussion

If `tag` was created with the `OSMT_PAGEABLE` attribute ` size` is a full page or larger, the allocated memory is pageable; otherwise it is wired.

## Parameters

- `size`: The size of the memory block to allocate.
- `tag`: The   under which to allocate the memory.

## See Also

- [OSMalloc_Tagalloc](1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](1398431-osmalloc_noblock.md).
- [OSFree](1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](1398447-osmalloc.md).
- [bzero](1579350-bzero.md)
- [bzero_phys](1593364-bzero_phys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1398447-osmalloc)*