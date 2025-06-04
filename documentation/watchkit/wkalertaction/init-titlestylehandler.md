# init(title:style:handler:)

**Framework**: WatchKit  
**Kind**: init

Creates and returns an action object with the specified button information.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(title: String, style: WKAlertActionStyle, handler: @escaping WKAlertActionHandler)
```

#### Return Value

An initialized action object that you can display in an alert.

#### Discussion

Use this method to create a button to display in an action sheet. In an action sheet, specifying an action with the [`WKAlertActionStyle.cancel`](https://developer.apple.com/documentation/watchkit/wkalertactionstyle/cancel) style replaces the standard Cancel button provided by the system.

## Parameters

- `title`: The localized string to use as the button title for the action.
- `style`: The style to apply to the action button. For a list of possible styles and their meanings, see  .
- `handler`: A block containing the code to execute when the user taps the action button. Use this block to perform whatever action is required to perform the associated task. For information about the format of this block, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertaction/init(title:style:handler:))*