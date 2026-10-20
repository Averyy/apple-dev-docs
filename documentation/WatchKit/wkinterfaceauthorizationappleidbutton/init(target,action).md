# init(target:action:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Creates an authorization button for use in SwiftUI.

**Availability**:
- watchOS 6.0+ - Deprecated in 6.1

> **Deprecated**: Use [`init(style:target:action:)`](./init%28style,target,action%29.md) instead.

## Declaration

```swift
init(target: Any?, action: Selector)
```

```objc
- (instancetype) initWithTarget:(id) target action:(SEL) action;
```

#### Discussion

When the user taps the button, the system calls the `action` method on the target.

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](../../SwiftUI/wkinterfaceobjectrepresentable.md) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `target`: The object whose action method is called.
- `action`: A selector identifying the action method called when the user taps the button.

## See Also

### Initializing for SwiftUI
- [init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)](./init%28style,target,action%29.md)
  Creates an authorization button for use in SwiftUI.
- [WKInterfaceAuthorizationAppleIDButton.Style](./style.md)
  Values that define an authorization button’s style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(target:action:))*