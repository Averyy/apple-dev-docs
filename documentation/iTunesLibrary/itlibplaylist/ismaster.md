# isMaster

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the playlist represents the entire iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.6+ - Deprecated in 27.2

> **Deprecated**: Use [`isPrimary`](./isprimary.md) instead.

## Declaration

```swift
var isMaster: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isMaster) BOOL master;
```

## See Also

### Deprecated
- [var isAllItemsPlaylist: Bool](./isallitemsplaylist.md)
  Indicates whether the API exposes every item in the playlist.
- [let ITLibPlaylistPropertyMaster: String](../itlibplaylistpropertymaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/ismaster)*