# ITLibInitOptions

**Framework**: iTunes Library  
**Kind**: enum

These constants describe initialization options for an iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibInitOptions
```

## Topics

### Init Options
- [ITLibInitOptions.none](itlibinitoptions/none.md)
  No initialization options apply.
- [ITLibInitOptions.lazyLoadData](itlibinitoptions/lazyloaddata.md)
  iTunes library data loads upon request, rather than during initialization.
### Initializers
- [init?(rawValue: UInt)](itlibinitoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(apiVersion: String) throws](itlibrary/init(apiversion:).md)
  Initializes an instance of [`ITLibrary`](itlibrary.md) that can retrieve media entities.
- [init(apiVersion: String, options: ITLibInitOptions) throws](itlibrary/init(apiversion:options:).md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibinitoptions)*