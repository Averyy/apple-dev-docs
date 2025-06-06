# SKIndexCreateWithMutableData(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a named index stored in a `CFMutableDataRef` object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexCreateWithMutableData(_ inData: CFMutableData!, _ inIndexName: CFString!, _ inIndexType: SKIndexType, _ inAnalysisProperties: CFDictionary!) -> Unmanaged<SKIndex>!
```

#### Return_value

 The newly created index.

#### Discussion

[`SKIndexCreateWithMutableData(_:_:_:_:)`](1447500-skindexcreatewithmutabledata.md) creates an index in memory as a [`CFMutableData`](https://developer.apple.com/documentation/corefoundation/cfmutabledata) object. Search Kit indexes are initially empty. A memory-based index is useful for quick searching and when your application doesn’t need persistent storage. To create a disk-based, persistent index, use the [`SKIndexCreateWithURL(_:_:_:_:)`](1446111-skindexcreatewithurl.md) function.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

This function retains the data object you provide in the `inData` parameter.

When your application no longer needs the index, dispose of it by calling [`SKIndexClose(_:)`](1442401-skindexclose.md).

##### 1680638

You cannot use [`CFMakeCollectable`](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) with [`SKIndex`](skindex.md) objects.

## Parameters

- `inData`: An empty   object to contain the index being created.
- `inIndexName`: The name of the index. If you call this function with   set to  , Search Kit assigns the index the default index name  . If you then attempt to create a second index in the same file without assigning a name, no second index is created and this function returns  . Search Kit does not support retrieving index names from an index.
- `inIndexType`: The index type. See  .
- `inAnalysisProperties`: The text analysis properties dictionary, which optionally sets the minimum term length, stopwords, term substitutions, maximum unique terms to index, and proximity support (for phrase-based searches) when creating the index. See  . The   parameter can be  , in which case Search Kit applies the default dictionary, which is  .

## See Also

- [func SKIndexCreateWithURL(CFURL!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1446111-skindexcreatewithurl.md)
  Creates a named index in a file whose location is specified with a CFURL object.
- [func SKIndexOpenWithData(CFData!, CFString!) -> Unmanaged<SKIndex>!](1446398-skindexopenwithdata.md)
  Opens an existing, named index for searching only.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447500-skindexcreatewithmutabledata)*