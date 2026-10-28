# SKIndexOpenWithURL(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Opens an existing, named index stored in a file whose location is specified with a CFURL object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexOpenWithURL(_ inURL: CFURL!, _ inIndexName: CFString!, _ inWriteAccess: Bool) -> Unmanaged<SKIndex>!
```

```c
SKIndexRef SKIndexOpenWithURL(CFURLRef inURL, CFStringRef inIndexName, Boolean inWriteAccess);
```

## Return Value

The named index, or `NULL` on failure.

## Discussion

If `inIndexName` is `NULL` and `inData` does not contain an index with the default name, this function returns `NULL`.

A call to `SKIndexOpenWithURL` retains the opened index. When your application no longer needs the index, dispose of it by calling [`SKIndexClose(_:)`](./api-1442401-skindexclose.md).

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

### Special Considerations

You cannot use [`CFMakeCollectable`](../CoreFoundation/cfmakecollectable.md) with [`SKIndex`](./skindex.md) objects.

## Parameters

- `inURL`: The location of the index.
- `inIndexName`: The name of the index. Can be `NULL`, in which case this function attempts to open the index with the default name of `IADefaultIndex`.
- `inWriteAccess`: A Boolean value indicating whether the index is open for updating. To open an index for searching only, pass `false` (`0` or `kCFBoolenFalse`). To open it for searching and updating, pass `true` (`1` or `kCFBooleanTrue`).

## See Also

### Creating, Opening, and Closing Indexes
- [func SKIndexCreateWithURL(CFURL!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](./api-1446111-skindexcreatewithurl.md)
  Creates a named index in a file whose location is specified with a CFURL object.
- [func SKIndexCreateWithMutableData(CFMutableData!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](./api-1447500-skindexcreatewithmutabledata.md)
  Creates a named index stored in a `CFMutableDataRef` object.
- [func SKIndexOpenWithData(CFData!, CFString!) -> Unmanaged<SKIndex>!](./api-1446398-skindexopenwithdata.md)
  Opens an existing, named index for searching only.
- [func SKIndexOpenWithMutableData(CFMutableData!, CFString!) -> Unmanaged<SKIndex>!](./api-1444201-skindexopenwithmutabledata.md)
  Opens an existing, named index for searching and updating.
- [func SKIndexClose(SKIndex!)](./api-1442401-skindexclose.md)
  Closes an index.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](./api-1442236-skindexgetindextype.md)
  Gets the category of an index.
- [func SKIndexGetTypeID() -> CFTypeID](./api-1450223-skindexgettypeid.md)
  Gets the type identifier for Search Kit indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449017-skindexopenwithurl)*