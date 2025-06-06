# SKSearchGetTypeID()

**Framework**: Core Services  
**Kind**: func

Gets the type identifier for Search Kit search objects.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSearchGetTypeID() -> CFTypeID
```

#### Return_value

A CFTypeID object containing the type identifier for the SKSearch opaque type.

#### Discussion

Search Kit represents searches with search objects ([`SKSearch`](sksearch.md) opaque types). If your code needs to determine whether a particular data type is a search object, you can use this function along with the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/corefoundation/cfgettypeid(_:)) function and perform a comparison.

Never hard-code the search type ID because it can change from one release of macOS to another.

## See Also

- [func SKSearchCreate(SKIndex!, CFString!, SKSearchOptions) -> Unmanaged<SKSearch>!](1443079-sksearchcreate.md)
  Creates an asynchronous search object for querying an index, and initiates search.
- [func SKSearchFindMatches(SKSearch!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Float>!, CFTimeInterval, UnsafeMutablePointer<CFIndex>!) -> Bool](1448608-sksearchfindmatches.md)
  Extracts search result information from a search object.
- [func SKSearchCancel(SKSearch!)](1442083-sksearchcancel.md)
  Cancels an asynchronous search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448621-sksearchgettypeid)*