# SKIndexClose(_:)

**Framework**: Core Services  
**Kind**: func

Closes an index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKIndexClose(_ inIndex: SKIndex!)
```

#### Discussion

When your application no longer needs an index that it has opened or created, call [`SKIndexClose(_:)`](1442401-skindexclose.md). Calling this function is equivalent to calling [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) on an index.

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

## Parameters

- `inIndex`: The index to close.

## See Also

- [func SKIndexCreateWithURL(CFURL!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1446111-skindexcreatewithurl.md)
  Creates a named index in a file whose location is specified with a CFURL object.
- [func SKIndexCreateWithMutableData(CFMutableData!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](1447500-skindexcreatewithmutabledata.md)
  Creates a named index stored in a `CFMutableDataRef` object.
- [func SKIndexOpenWithData(CFData!, CFString!) -> Unmanaged<SKIndex>!](1446398-skindexopenwithdata.md)
  Opens an existing, named index for searching only.
- [func SKIndexOpenWithMutableData(CFMutableData!, CFString!) -> Unmanaged<SKIndex>!](1444201-skindexopenwithmutabledata.md)
  Opens an existing, named index for searching and updating.
- [func SKIndexOpenWithURL(CFURL!, CFString!, Bool) -> Unmanaged<SKIndex>!](1449017-skindexopenwithurl.md)
  Opens an existing, named index stored in a file whose location is specified with a CFURL object.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](1442236-skindexgetindextype.md)
  Gets the category of an index.
- [func SKIndexGetTypeID() -> CFTypeID](1450223-skindexgettypeid.md)
  Gets the type identifier for Search Kit indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442401-skindexclose)*