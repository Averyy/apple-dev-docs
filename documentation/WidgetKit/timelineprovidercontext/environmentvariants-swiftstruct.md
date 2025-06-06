# TimelineProviderContext.EnvironmentVariants

**Framework**: Widgetkit  
**Kind**: struct

A structure containing all varieties of environments where a widget could appear.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@dynamicMemberLookup
struct EnvironmentVariants
```

#### Overview

When changes occur in environment values that affect display, like [`colorScheme`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/colorScheme), WidgetKit renders your widget’s views. If your widget uses assets that take time to generate or depend on the specific environment they’re rendered in, you can generate those assets in advance based on the new environment values.

For example, in macOS, if the user has a mixture of @1x and @2x displays, the value for [`displayScale`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/displayScale) includes both scales. With these values, you can prepare your content in advance, if needed, to handle either type of display.

## Topics

### Subscripts
- [subscript<T>(WritableKeyPath<EnvironmentValues, T>) -> [T]?](timelineprovidercontext/environmentvariants-swift.struct/subscript(_:).md)
  Returns the widget environment variants for a key path to an environment values instance.
- [subscript<T>(dynamicMember _: WritableKeyPath<EnvironmentValues, T>) -> [T]?](timelineprovidercontext/environmentvariants-swift.struct/subscript(dynamicmember:).md)
  Returns the widget environment variants for a key path to an environment values instance.

## See Also

- [let environmentVariants: TimelineProviderContext.EnvironmentVariants](timelineprovidercontext/environmentvariants-swift.property.md)
  All environment values that might be set when a widget appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct)*