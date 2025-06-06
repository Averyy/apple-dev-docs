# sortName

**Framework**: iTunes Library  
**Kind**: property

The name of the artist to use when sorting.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var sortName: String? { get }
```

#### Discussion

If `nil`, iTunes uses [`name`](itlibartist/name.md) to sort by artist name.

## See Also

- [var name: String?](itlibartist/name.md)
  The name of the artist.
- [var persistentID: NSNumber](itlibartist/persistentid.md)
  The unique identifier of the artist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartist/sortname)*