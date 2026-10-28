# init(style:target:action:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Creates an authorization button for use in SwiftUI.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)
```

```objc
- (instancetype) initWithStyle:(WKInterfaceAuthorizationAppleIDButtonStyle) style target:(id) target action:(SEL) action;
```

## Discussion

When the user taps the button, the system calls the `action` method on the target.

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](../../SwiftUI/wkinterfaceobjectrepresentable.md) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `style`: The button’s style. For a list of possible values, see [`WKInterfaceAuthorizationAppleIDButton.Style`](./style.md).
- `target`: The object whose action method is called.
- `action`: A selector identifying the action method called when the user taps the button.

## See Also

### Initializing for SwiftUI
- [WKInterfaceAuthorizationAppleIDButton.Style](./style.md)
  Values that define an authorization button’s style.
- [init(target: Any?, action: Selector)](./init%28target,action%29.md)
  Creates an authorization button for use in SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(style:target:action:))*