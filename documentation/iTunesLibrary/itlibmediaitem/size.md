# size

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The size in bytes of the media item on disk.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

> **Deprecated**: Use [`fileSize`](./filesize.md) instead.

## Declaration

```swift
var size: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger size;
```

## See Also

### Deprecated
- [var fileType: Int](./filetype.md)
  The file type of the media item.
- [let ITLibMediaItemPropertyFileType: String](../itlibmediaitempropertyfiletype.md)
  The file type of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitem/size)*