# UIVerticalBarBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A behavior that determines whether the vertical bar is used.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum UIVerticalBarBehavior
```

```c
enum UIVerticalBarBehavior : NSInteger;
```

## Overview

Return this type from [`preferredVerticalBarBehavior`](./uiviewcontroller/preferredverticalbarbehavior.md) to apply the preferred behavior.

## Topics

### Specifying vertical bar behavior
- [UIVerticalBarBehavior.automatic](./uiverticalbarbehavior/automatic.md)
  The system determines whether the vertical bar is rendered.
- [UIVerticalBarBehavior.disabled](./uiverticalbarbehavior/disabled.md)
  The vertical bar is disabled.
### Initializers
- [init?(rawValue: Int)](./uiverticalbarbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring bars on the vertical axis
- [enum UIVerticalBarCompressionBehavior](./uiverticalbarcompressionbehavior.md)
  How bars compress when different types of bars are hosted together and space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiverticalbarbehavior)*