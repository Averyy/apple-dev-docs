# sortName

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The name of the artist to use when sorting.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var sortName: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * sortName;
```

## Discussion

If `nil`, iTunes uses [`name`](./name.md) to sort by artist name.

## See Also

### Getting Artist Info
- [var name: String?](./name.md)
  The name of the artist.
- [var persistentID: NSNumber](./persistentid.md)
  The unique identifier of the artist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartist/sortname)*