# SKSearchCancel(_:)

**Framework**: Core Services  
**Kind**: func

Cancels an asynchronous search request.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSearchCancel(_ inSearch: SKSearch!)
```

#### Discussion

Call this function when you want to cancel an asynchronous search that you initiated with [`SKSearchCreate(_:_:_:)`](1443079-sksearchcreate.md). This function stops the search process if it is still in progress at the time. It does not dispose of the search object (SKSearchRef).

Search Kit is thread-safe. You can use separate indexing and searching threads. Your application is responsible for ensuring that no more than one process is open at a time for writing to an index.

## Parameters

- `inSearch`: The search object whose associated asynchronous search you want to cancel.

## See Also

- [func SKSearchCreate(SKIndex!, CFString!, SKSearchOptions) -> Unmanaged<SKSearch>!](1443079-sksearchcreate.md)
  Creates an asynchronous search object for querying an index, and initiates search.
- [func SKSearchFindMatches(SKSearch!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Float>!, CFTimeInterval, UnsafeMutablePointer<CFIndex>!) -> Bool](1448608-sksearchfindmatches.md)
  Extracts search result information from a search object.
- [func SKSearchGetTypeID() -> CFTypeID](1448621-sksearchgettypeid.md)
  Gets the type identifier for Search Kit search objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442083-sksearchcancel)*