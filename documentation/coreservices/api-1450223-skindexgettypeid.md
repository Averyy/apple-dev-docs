# SKIndexGetTypeID()

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the type identifier for Search Kit indexes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKIndexGetTypeID() -> CFTypeID
```

```c
CFTypeID SKIndexGetTypeID(void);
```

## Return Value

A [`CFTypeID`](../CoreFoundation/cftypeid.md) object containing the type identifier for the [`SKIndex`](./skindex.md) opaque type.

## Discussion

Search Kit represents indexes with the [`SKIndex`](./skindex.md) opaque type. If your code needs to determine whether a particular data type is an index, you can use this function along with the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function and perform a comparison.

Never hard-code the index type ID because it can change from one release of macOS to another.

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
- [func SKIndexOpenWithURL(CFURL!, CFString!, Bool) -> Unmanaged<SKIndex>!](./api-1449017-skindexopenwithurl.md)
  Opens an existing, named index stored in a file whose location is specified with a CFURL object.
- [func SKIndexClose(SKIndex!)](./api-1442401-skindexclose.md)
  Closes an index.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](./api-1442236-skindexgetindextype.md)
  Gets the category of an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450223-skindexgettypeid)*