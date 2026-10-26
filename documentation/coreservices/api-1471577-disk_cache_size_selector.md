# Disk Cache Size Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies size information for the disk cache buffer.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltDiskCacheSize](./api-1471577-disk_cache_size_selector/gestaltdiskcachesize.md)
  A selector that you pass to the `Gestalt` function. If the function returns `noErr`, the `response` parameter contains the size of the disk cache’s buffer. See the Gestalt Manager Reference for more information on the `Gestalt` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471577-disk_cache_size_selector)*