# HomeExtension

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that represents an app extension for the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
protocol HomeExtension
```

## Overview

Create a type that adopts this protocol, mark it with `@main`, and return your content from [`body`](./homeextension/body.md).

## Topics

### Providing content
- [var body: Self.Content](./homeextension/body.md)
  The content that your extension provides to the Home app.
- [associatedtype Content : HomeContent](./homeextension/content.md)
  The type of content that your extension provides.
### Creating an extension
- [init()](./homeextension/init%28%29.md)
  Creates an instance of your extension.
### Starting the extension
- [static func main() throws](./homeextension/main%28%29.md)
  Starts your app extension.

## See Also

### Essentials
- [class HomeContext](./homecontext.md)
  The context in which the Home app launches your extension, including the selected home and accessory.
- [class HomeNavigator](./homenavigator.md)
  An object that manages navigation for your extension’s content in the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeextension)*