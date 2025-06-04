# init(style:target:action:)

**Framework**: WatchKit  
**Kind**: init

Creates an authorization button for use in SwiftUI.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)
```

#### Discussion

When the user taps the button, the system calls the `action` method on the target.

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](https://developer.apple.com/documentation/SwiftUI/WKInterfaceObjectRepresentable) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `style`: The button’s style. For a list of possible values, see  .
- `target`: The object whose action method is called.
- `action`: A selector identifying the action method called when the user taps the button.

## See Also

- [WKInterfaceAuthorizationAppleIDButton.Style](style.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/style))
  Values that define an authorization button’s style.
- [init(target: Any?, action: Selector)](init(target:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(target:action:)))
  Creates an authorization button for use in SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(style:target:action:))*