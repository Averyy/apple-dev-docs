# FSCatalogSearch

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSCatalogSearch(FSIterator iterator, const FSSearchParams *searchCriteria, ItemCount maximumObjects, ItemCount *actualObjects, Boolean *containerChanged, FSCatalogInfoBitmap whichInfo, FSCatalogInfo *catalogInfos, FSRef *refs, FSSpecPtr specs, HFSUniStr255 *names);
```

## See Also

### Searching a Volume Using a Catalog Iterator
- [PBCatalogSearchSync](./api-1565713-pbcatalogsearchsync.md)
- [PBCatalogSearchAsync](./api-1566401-pbcatalogsearchasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565862-fscatalogsearch)*