# onError

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is automatically called when an error is sent from the Apple TV.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onError;
```

#### Discussion

Use the `onError` attribute to handle any errors sent from the Apple TV. This attribute must be set to the following function: `App.onError = function (message, sourceURL, line) {}`. 

- `message`—The error message.
- `sourceURL`—The URL for the TVMLKit JS file where the error occurred. Defaults to `nil` if the information is not available.
- `line`—The line in the TVMLKit JS file where the error occurred. Defaults to `nil` if the information is not available.

## See Also

- [onExit](app/1627419-onexit.md)
  A callback function that is automatically called when the app has been exited.
- [onLaunch](app/1627407-onlaunch.md)
  A callback function that is automatically called when the app has been launched.
- [onResume](app/1627415-onresume.md)
  A callback function that is automatically called when the app moves to the foreground.
- [onSuspend](app/1627431-onsuspend.md)
  A callback function that is automatically called when the app is sent to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627353-onerror)*