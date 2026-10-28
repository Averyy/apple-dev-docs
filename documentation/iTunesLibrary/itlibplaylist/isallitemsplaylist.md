# isAllItemsPlaylist

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

Indicates whether the API exposes every item in the playlist.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

> **Deprecated**: not useful

## Declaration

```swift
var isAllItemsPlaylist: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isAllItemsPlaylist) BOOL allItemsPlaylist;
```

## Discussion

This property always returns [`true`](../../Swift/true.md).

## See Also

### Deprecated
- [var isMaster: Bool](./ismaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.
- [let ITLibPlaylistPropertyMaster: String](../itlibplaylistpropertymaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/isallitemsplaylist)*