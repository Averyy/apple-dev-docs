# ITLibInitOptions

**Framework**: iTunes Library  
**Kind**: enum  
**Role**: Enumeration

These constants describe initialization options for an iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibInitOptions
```

```c
enum ITLibInitOptions : NSUInteger;
```

## Topics

### Init Options
- [ITLibInitOptions.none](./itlibinitoptions/none.md)
  No initialization options apply.
- [ITLibInitOptions.lazyLoadData](./itlibinitoptions/lazyloaddata.md)
  iTunes library data loads upon request, rather than during initialization.
### Initializers
- [init?(rawValue: UInt)](./itlibinitoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [convenience init(apiVersion: String) throws](./itlibrary/init%28apiversion%29-71e74.md)
  Initializes an instance of [`ITLibrary`](./itlibrary.md) that can retrieve media entities.
- [init(apiVersion: String, options: ITLibInitOptions) throws](./itlibrary/init%28apiversion,options%29-9eorg.md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibinitoptions)*