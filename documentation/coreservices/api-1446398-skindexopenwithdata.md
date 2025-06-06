# SKIndexOpenWithData(_:_:)

**Framework**: Core Services  
**Kind**: func

Opens an existing, named index for searching only.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexOpenWithData(_ inData: CFData!, _ inIndexName: CFString!) -> Unmanaged<SKIndex>!
```

#### Return_value

 The named index, or `NULL` on failure.

#### Discussion

An index opened by `SKIndexOpenWithData` can be searched but not updated. To open an index for updating, use [`SKIndexOpenWithMutableData(_:_:)`](1444201-skindexopenwithmutabledata.md).

If `inIndexName` is `NULL` and `inData` does not contain an index with the default name, this function returns `NULL`.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

A call to `SKIndexOpenWithData` retains the opened index. When your application no longer needs the index, dispose of it by calling [`SKIndexClose(_:)`](1442401-skindexclose.md).

##### 1680655

You cannot use [`CFMakeCollectable`](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) with [`SKIndex`](skindex.md) objects.

## Parameters

- `inData`: The index to open.
- `inIndexName`: The name of the index. Can be  , in which case this function attempts to open the index with the default name of  .

## See Also

- [func SKIndexCreateWithURL(CFURL!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1446111-skindexcreatewithurl.md)
  Creates a named index in a file whose location is specified with a CFURL object.
- [func SKIndexCreateWithMutableData(CFMutableData!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1447500-skindexcreatewithmutabledata.md)
  Creates a named index stored in a `CFMutableDataRef` object.
- [func SKIndexOpenWithMutableData(CFMutableData!, CFString!) -> Unmanaged<SKIndex>!](1444201-skindexopenwithmutabledata.md)
  Opens an existing, named index for searching and updating.
- [func SKIndexOpenWithURL(CFURL!, CFString!, Bool) -> Unmanaged<SKIndex>!](1449017-skindexopenwithurl.md)
  Opens an existing, named index stored in a file whose location is specified with a CFURL object.
- [func SKIndexClose(SKIndex!)](1442401-skindexclose.md)
  Closes an index.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](1442236-skindexgetindextype.md)
  Gets the category of an index.
- [func SKIndexGetTypeID() -> CFTypeID](1450223-skindexgettypeid.md)
  Gets the type identifier for Search Kit indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446398-skindexopenwithdata)*