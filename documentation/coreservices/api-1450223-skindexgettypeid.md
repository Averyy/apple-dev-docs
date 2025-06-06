# SKIndexGetTypeID()

**Framework**: Core Services  
**Kind**: func

Gets the type identifier for Search Kit indexes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexGetTypeID() -> CFTypeID
```

#### Return_value

A [`CFTypeID`](https://developer.apple.com/documentation/corefoundation/cftypeid) object containing the type identifier for the [`SKIndex`](skindex.md) opaque type.

#### Discussion

Search Kit represents indexes with the [`SKIndex`](skindex.md) opaque type. If your code needs to determine whether a particular data type is an index, you can use this function along with the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/corefoundation/cfgettypeid(_:)) function and perform a comparison.

Never hard-code the index type ID because it can change from one release of macOS to another.

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
- [func SKIndexClose(SKIndex!)](1442401-skindexclose.md)
  Closes an index.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](1442236-skindexgetindextype.md)
  Gets the category of an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450223-skindexgettypeid)*