# onLaunch

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is automatically called when the app has been launched.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onLaunch;
```

#### Discussion

Use the `onLaunch` attribute to start any required actions (for example, loading the first TVML page) when the app launches. This attribute must be set to a function that accepts an `options` argument; for example `App.onLaunch = function (options) {}`. The options argument can contain the following keys:

- `launchContext`—Determines how the app is launched. Set to `background` to launch the app in the background.
- `location`—Contains the boot TVMLKit JS URL location.
- `reloadData`—The object passed in to `App.reload()` when the app is relaunched.
- User defined keys—Any custom keys that were passed to [`launchOptions`](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/launchoptions).

## See Also

- [onError](app/1627353-onerror.md)
  A callback function that is automatically called when an error is sent from the Apple TV.
- [onExit](app/1627419-onexit.md)
  A callback function that is automatically called when the app has been exited.
- [onResume](app/1627415-onresume.md)
  A callback function that is automatically called when the app moves to the foreground.
- [onSuspend](app/1627431-onsuspend.md)
  A callback function that is automatically called when the app is sent to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627407-onlaunch)*