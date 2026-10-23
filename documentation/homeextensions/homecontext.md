# HomeContext

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

The context in which the Home app launches your extension, including the selected home and accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final class HomeContext
```

#### Overview

You access the context from the environment with `@Environment(\.homeContext)`. The context is available in the SwiftUI environment while the extension is running.

## Topics

### Getting context
- [var accessory: HMAccessory?](./homecontext/accessory.md)
  The accessory that a person selected in the Home app.
- [var home: HMHome?](./homecontext/home.md)
  The home that a person selected in the Home app.
### Working with the navigation stack
- [let navigator: HomeNavigator](./homecontext/navigator.md)
  The navigator for pushing pages onto the Home app’s navigation stack.
- [func dismiss() async](./homecontext/dismiss%28%29.md)
  Asks the Home app to dismiss your extension’s content.
### Reading extension metadata
- [var metadata: [String : String]](./homecontext/metadata.md)
  Additional information that the Home app provides about the content it’s displaying.
- [HomeContext.MetadataKey](./homecontext/metadatakey.md)
  Keys for values in the context’s metadata.
### Completing configuration
- [func reportConfigurationComplete() async](./homecontext/reportconfigurationcomplete%28%29.md)
  Tells the Home app that the accessory’s configuration is complete.
### Debugging
- [var description: String](./homecontext/description.md)
  A textual description of the context, for debugging.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [protocol HomeExtension](./homeextension.md)
  A type that represents an app extension for the Home app.
- [class HomeNavigator](./homenavigator.md)
  An object that manages navigation for your extension’s content in the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext)*