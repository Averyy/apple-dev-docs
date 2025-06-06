# init(frame:frameName:groupName:)

**Framework**: Webkit  
**Kind**: init

Initializes the receiver with a frame rectangle, frame name, and group name.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
init!(frame: NSRect, frameName: String!, groupName: String!)
```

#### Return Value

An initialized view object or `nil` if the object couldn’t be created.

#### Discussion

This method is the designated initializer for the `WebView` class.

## Parameters

- `frame`: The frame rectangle for the created view object.
- `frameName`: The web frame’s name. This should not be one of the predefined frame names (see the  nil`.
- `groupName`: An arbitrary identifier used to group related frames. For example, JavaScript running in a frame can access any other frame in the same group. It’s up to the application how it chooses to scope related frames. This parameter can be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/init(frame:framename:groupname:))*