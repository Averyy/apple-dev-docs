# onExit

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is automatically called when the app has been exited.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onExit;
```

#### Discussion

Use the `onExit` attribute to complete any actions that need to be cleaned up (for example, releasing any system resources) when the app has been exited. This attribute must be set to a function that accepts an `options` argument; for example `App.onExit = function (options) {}`. The options argument can contain the following keys:

- `reloading`—Set to `true` if the app is exiting as a result of `App.reload()` and is to be relaunched later.

## See Also

- [onError](app/1627353-onerror.md)
  A callback function that is automatically called when an error is sent from the Apple TV.
- [onLaunch](app/1627407-onlaunch.md)
  A callback function that is automatically called when the app has been launched.
- [onResume](app/1627415-onresume.md)
  A callback function that is automatically called when the app moves to the foreground.
- [onSuspend](app/1627431-onsuspend.md)
  A callback function that is automatically called when the app is sent to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627419-onexit)*