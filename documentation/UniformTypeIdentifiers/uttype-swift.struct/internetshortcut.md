# internetShortcut

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents a Microsoft internet shortcut file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var internetShortcut: UTType { get }
```

## Discussion

The identifier for this type is `com.microsoft.internet-shortcut`.

This type conforms to [`UTTypeData`](../uttypedata.md) and a base type identified by `public.stored-url`.

## See Also

### Internet-specific
- [static var html: UTType](./html.md)
  A type that represents any version of HTML.
- [static var webArchive: UTType](./webarchive.md)
  A type that represents WebKit web archive data.
- [static var internetLocation: UTType](./internetlocation.md)
  A base type that represents an Apple internet location file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/internetshortcut)*