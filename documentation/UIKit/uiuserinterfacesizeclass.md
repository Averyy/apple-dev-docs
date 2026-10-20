# UIUserInterfaceSizeClass

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the size class of a view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum UIUserInterfaceSizeClass
```

```c
enum UIUserInterfaceSizeClass : NSInteger;
```

## Topics

### Constants
- [UIUserInterfaceSizeClass.unspecified](./uiuserinterfacesizeclass/unspecified.md)
  Indicates the size class hasn’t been specified.
- [UIUserInterfaceSizeClass.compact](./uiuserinterfacesizeclass/compact.md)
  Indicates a compact size class.
- [UIUserInterfaceSizeClass.regular](./uiuserinterfacesizeclass/regular.md)
  Indicates a regular size class.
### Initializers
- [init(UserInterfaceSizeClass?)](./uiuserinterfacesizeclass/init%28_%29.md)
  Creates a size class from the specified SwiftUI size class.
- [init?(rawValue: Int)](./uiuserinterfacesizeclass/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving size class traits
- [var horizontalSizeClass: UIUserInterfaceSizeClass](./uitraitcollection/horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [var verticalSizeClass: UIUserInterfaceSizeClass](./uitraitcollection/verticalsizeclass.md)
  The vertical size class of the trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass)*