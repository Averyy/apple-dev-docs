# gestaltDiskCacheSize

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

A selector that you pass to the `Gestalt` function. If the function returns `noErr`, the `response` parameter contains the size of the disk cache’s buffer. See the Gestalt Manager Reference for more information on the `Gestalt` function.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltDiskCacheSize = 'dcsz'
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471577-disk_cache_size_selector/gestaltdiskcachesize)*