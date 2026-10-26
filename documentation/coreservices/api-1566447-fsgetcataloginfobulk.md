# FSGetCatalogInfoBulk

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: In macOS 10.8 and later, use [`contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:`](../Foundation/filemanager/contentsofdirectory%28at,includingpropertiesforkeys,options%29.md) or [`enumeratorAtPath:`](../Foundation/filemanager/enumerator%28atpath%29.md) instead.

## Declaration

```c
OSErr FSGetCatalogInfoBulk(FSIterator iterator, ItemCount maximumObjects, ItemCount *actualObjects, Boolean *containerChanged, FSCatalogInfoBitmap whichInfo, FSCatalogInfo *catalogInfos, FSRef *refs, FSSpecPtr specs, HFSUniStr255 *names);
```

#### Discussion

> ❗ **Important**: [`FSGetCatalogInfoBulk`](./api-1566447-fsgetcataloginfobulk.md) returns directory entries in a different order on APFS and HFS+ volumes. Don't rely on any specific ordering of returned values; instead, explicitly sort directory entries as necessary.

## See Also

### Obtaining File and Directory Information Using a Catalog Iterator on HFS Plus Volumes
- [PBGetCatalogInfoBulkSync](./api-1565707-pbgetcataloginfobulksync.md)
- [PBGetCatalogInfoBulkAsync](./api-1566399-pbgetcataloginfobulkasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1566447-fsgetcataloginfobulk)*