# OSMalloc_Tagalloc

**Framework**: Kernel  
**Kind**: func

Creates a tag for use with OSMalloc functions.

**Availability**:
- macOS 10.4+

## Declaration

```swift
OSMallocTag OSMalloc_Tagalloc(const char *name, uint32_t flags);
```

#### Return_value

An opaque tag to be used with OSMalloc functions for tracking memory usage.

#### Discussion

OSMalloc tags can have arbitrary names of a length up to 63 characters. Calling this function twice with the same name creates two tags, which share that name.

`flags` can be the bitwise OR of the following flags:

- `OSMT_DEFAULT` - allocations are wired. This is the 'zero' bitmask value and is overridden by any other flag specified.
- `OSMT_PAGEABLE` - allocations of a full page size or greater are pageable; allocations smaller than a page are wired.

## Parameters

- `name`: The name of the tag to create.
- `flags`: A bitmask that controls allocation behavior; see description.

## See Also

- [OSMalloc](1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1398437-osmalloc_tagalloc)*