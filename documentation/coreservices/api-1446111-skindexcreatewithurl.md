# SKIndexCreateWithURL(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a named index in a file whose location is specified with a CFURL object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexCreateWithURL(_ inURL: CFURL!, _ inIndexName: CFString!, _ inIndexType: SKIndexType, _ inAnalysisProperties: CFDictionary!) -> Unmanaged<SKIndex>!
```

#### Return_value

 A unique reference to the newly created index.

#### Discussion

`SKIndexCreateWithURL` creates an index in a file. Search Kit indexes are initially empty. Use this function when your application needs persistent storage of an index. To create a memory-based, nonpersistent index, use [`SKIndexCreateWithMutableData(_:_:_:_:)`](1447500-skindexcreatewithmutabledata.md).

A file can contain more than one index. To add a new index to an existing file, use the same value for `inURL` and supply a new name for `inIndexName`.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

When your application no longer needs the index, dispose of it by calling [`SKIndexClose(_:)`](1442401-skindexclose.md). 

##### 1680604

You cannot use [`CFMakeCollectable`](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) with [`SKIndex`](skindex.md) objects.

## Parameters

- `inURL`: The location of the index.
- `inIndexName`: The name of the index. If you call this function with   set to  , Search Kit assigns the index the default index name  . If you then attempt to create a second index in the same file without assigning a name, no second index is created and this function returns  . Search Kit does not currently support retrieving index names from an index.
- `inIndexType`: The index type. See  .
- `inAnalysisProperties`: The text analysis properties dictionary, which optionally sets the minimum term length, stopwords, term substitutions, maximum unique terms to index, and proximity support (for phrase-based searches) when creating the index. See  . To get the analysis properties of an index, use the   function. The   parameter can be  , in which case Search Kit applies the default dictionary, which is  .

## See Also

- [func SKIndexCreateWithMutableData(CFMutableData!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1447500-skindexcreatewithmutabledata.md)
  Creates a named index stored in a `CFMutableDataRef` object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446111-skindexcreatewithurl)*