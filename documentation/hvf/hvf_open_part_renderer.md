# HVF_open_part_renderer

**Framework**: hvf  
**Kind**: func  
**Role**: Function

Create a part renderer in the storage provided.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```c
int HVF_open_part_renderer(const void *hvgl, size_t hvglSize, const void *hvpm, size_t hvpmSize, void *storage, size_t storageSize);
```

## Discussion

The storage must be at least as large as what’s returned by `HVF_part_renderer_storage_size()`. This storage must be on a double boundary. The passed-in `hvgl` table must also be on a double boundary. The `hvpm` table is optional and may be NULL and zero size.

The return value is 0 for success, nonzero for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvf_open_part_renderer)*