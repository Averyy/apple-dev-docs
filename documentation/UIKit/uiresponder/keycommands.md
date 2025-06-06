# keyCommands

**Framework**: UIKit  
**Kind**: property

The key commands that trigger actions on this responder.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var keyCommands: [UIKeyCommand]? { get }
```

#### Discussion

A responder object that supports hardware keyboard commands can redefine this property and use it to return an array of [`UIKeyCommand`](uikeycommand.md) objects that it supports. Each key command object represents the keyboard sequence to recognize and the action method of the responder to call in response.

The key commands you return from this method are applied to the entire responder chain. When a key combination is pressed that matches a key command object, UIKit walks the responder chain looking for an object that implements the corresponding action method. It calls that method on the first object it finds and then stops processing the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/keycommands)*