# UITabAccessory.Environment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Environment
```

```c
enum UITabAccessoryEnvironment : NSInteger;
```

## Topics

### Enumeration Cases
- [UITabAccessory.Environment.inline](./environment/inline.md)
  The environment for when the accessory is laid out inline with the collapsed bottom tab bar.
- [UITabAccessory.Environment.none](./environment/none.md)
  The trait collection is from a view that is not in an active tab accessory environment.
- [UITabAccessory.Environment.regular](./environment/regular.md)
  The environment for when the accessory is laid out either:
- [UITabAccessory.Environment.unspecified](./environment/unspecified.md)
  Indicates the absence of any information about whether or not the trait collection is from a view that is in a tab accessory.
### Initializers
- [init?(rawValue: Int)](./environment/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabaccessory/environment)*