# ITLibPlaylistPropertyMaster

**Framework**: iTunes Library  
**Kind**: var  
**Role**: Global Variable

A Boolean value that indicates whether the playlist represents the entire iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.6+ - Deprecated in 27.2 (renamed: ITLibPlaylistPropertyPrimary)

> **Deprecated**: Use [`ITLibPlaylistPropertyPrimary`](./itlibplaylistpropertyprimary.md) instead.

## Declaration

```swift
let ITLibPlaylistPropertyMaster: String
```

```c
extern NSString * const ITLibPlaylistPropertyMaster;
```

## See Also

### Deprecated
- [var isAllItemsPlaylist: Bool](./itlibplaylist/isallitemsplaylist.md)
  Indicates whether the API exposes every item in the playlist.
- [var isMaster: Bool](./itlibplaylist/ismaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylistpropertymaster)*