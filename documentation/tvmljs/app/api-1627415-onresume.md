# onResume

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is automatically called when the app moves to the foreground.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onResume;
```

#### Discussion

Use the `onResume` attribute to start any required actions when the app moves from the background to the foreground. This attribute must be set to a function that accepts an `options` argument; for example `App.onResume = function (options) {}`. The `options` argument is always set to `null`.

## See Also

- [onError](app/1627353-onerror.md)
  A callback function that is automatically called when an error is sent from the Apple TV.
- [onExit](app/1627419-onexit.md)
  A callback function that is automatically called when the app has been exited.
- [onLaunch](app/1627407-onlaunch.md)
  A callback function that is automatically called when the app has been launched.
- [onSuspend](app/1627431-onsuspend.md)
  A callback function that is automatically called when the app is sent to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627415-onresume)*