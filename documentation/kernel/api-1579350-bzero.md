# bzero

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
void bzero(void *s, size_t n);
```

## See Also

### Memory
- [OSMalloc](./api-1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](./osmalloctag.md).
- [OSMalloc_Tagalloc](./api-1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](./api-1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](./api-1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](./osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](./api-1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](./api-1398431-osmalloc_noblock.md).
- [OSFree](./api-1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](./api-1398447-osmalloc.md).
- [bzero_phys](./api-1593364-bzero_phys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579350-bzero)*