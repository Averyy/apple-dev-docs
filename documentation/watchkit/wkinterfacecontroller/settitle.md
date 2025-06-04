# setTitle(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the title of the interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func setTitle(_ title: String?)
```

## Overview

This method sets the string to display in the status bar when this interface controller is onscreen. Set the string to the name of your app or to any other text that provides the user with context about the purpose of the interface controller. You can also configure the title in your storyboard file.

To localize the title, use the value in the `title` parameter as the lookup key for a string in your `Localizable.strings` file. If you do not include a localized set of strings with that key in your Watch app bundle, WatchKit uses the value in `title` directly.

## Parameters

- `title`: A localized string that identifies the current interface to the user. If the string is too long to fit on the screen, it is truncated.

## See Also

- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init()))
- [func awake(withContext: Any?)](awake(withcontext:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:))*