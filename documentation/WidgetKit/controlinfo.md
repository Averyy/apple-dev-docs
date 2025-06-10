# ControlInfo

**Framework**: WidgetKit  
**Kind**: struct

A structure that contains information about user-configured controls.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct ControlInfo
```

## Topics

### Instance Properties
- [let kind: String](controlinfo/kind.md)
  The string specified during creation of the control’s configuration.
- [var pushInfo: ControlPushInfo?](controlinfo/pushinfo.md)
  Push information about a control, if present.
### Instance Methods
- [func configurationIntent<Intent>(of: Intent.Type) -> Intent?](controlinfo/configurationintent(of:).md)
  Gets the associated App Intent.
### Default Implementations
- [Identifiable Implementations](controlinfo/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct StaticControlConfiguration](staticcontrolconfiguration.md)
  The description of a control widget that has no user-configurable options.
- [struct AppIntentControlConfiguration](appintentcontrolconfiguration.md)
  The description of a control widget that uses a custom intent to provide user-configurable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlinfo)*