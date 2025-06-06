# init(target:action:)

**Framework**: Watchkit  
**Kind**: init

Creates an authorization button for use in SwiftUI.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
init(target: Any?, action: Selector)
```

#### Discussion

When the user taps the button, the system calls the `action` method on the target.

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](https://developer.apple.com/documentation/SwiftUI/WKInterfaceObjectRepresentable) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `target`: The object whose action method is called.
- `action`: A selector identifying the action method called when the user taps the button.

## See Also

- [init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)](wkinterfaceauthorizationappleidbutton/init(style:target:action:).md)
  Creates an authorization button for use in SwiftUI.
- [WKInterfaceAuthorizationAppleIDButton.Style](wkinterfaceauthorizationappleidbutton/style.md)
  Values that define an authorization button’s style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(target:action:))*