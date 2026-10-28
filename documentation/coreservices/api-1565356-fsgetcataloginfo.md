# FSGetCatalogInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: In macOS 10.8 and later, use [`resourceValuesForKeys:error:`](../Foundation/nsurl/resourcevalues%28forkeys%29.md) instead.

## Declaration

```c
OSErr FSGetCatalogInfo(const FSRef *ref, FSCatalogInfoBitmap whichInfo, FSCatalogInfo *catalogInfo, HFSUniStr255 *outName, FSSpecPtr fsSpec, FSRef *parentRef);
```

## Discussion

> ❗ **Important**: Avoid using this function to determine whether a file has changed. The fractional dates returned by the [`FSGetCatalogInfo`](./api-1565356-fsgetcataloginfo.md) function don't compare exactly to the fractional dates returned by the [NSURL](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-older-but-post-10.8/index.html#//apple_ref/doc/uid/TP40016592-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_20) date properties, because of differences in rounding and precision.
>
> Instead, call the [`getResourceValue:forKey:error:`](../Foundation/nsurl/getresourcevalue%28_,forkey%29.md) method of [NSURL](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-older-but-post-10.8/index.html#//apple_ref/doc/uid/TP40016592-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_20) with [`NSURLGenerationIdentifierKey`](../Foundation/urlresourcekey/generationidentifierkey.md). On file systems that don't support generation identifiers, call the [`getResourceValue:forKey:error:`](../Foundation/nsurl/getresourcevalue%28_,forkey%29.md) method with [`NSURLContentModificationDateKey`](../Foundation/urlresourcekey/contentmodificationdatekey.md).

## See Also

### Accessing Information About Files and Directories
- [PBGetCatalogInfoAsync](./api-1565934-pbgetcataloginfoasync.md)
- [PBGetCatalogInfoSync](./api-1566328-pbgetcataloginfosync.md)
- [PBSetCatalogInfoAsync](./api-1566340-pbsetcataloginfoasync.md)
- [PBSetCatalogInfoSync](./api-1565271-pbsetcataloginfosync.md)
- [FSSetCatalogInfo](./api-1566580-fssetcataloginfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565356-fsgetcataloginfo)*