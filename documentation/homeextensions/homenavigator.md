# HomeNavigator

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

An object that manages navigation for your extension’s content in the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final class HomeNavigator
```

## Overview

Access the navigator through [`navigator`](./homecontext/navigator.md), and use it to push pages onto the Home app’s navigation stack.

## Topics

### Displaying content
- [func push(some Hashable, title: String?)](./homenavigator/push%28_,title%29.md)
  Pushes a page onto the Home app’s navigation stack.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [protocol HomeExtension](./homeextension.md)
  A type that represents an app extension for the Home app.
- [class HomeContext](./homecontext.md)
  The context in which the Home app launches your extension, including the selected home and accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homenavigator)*