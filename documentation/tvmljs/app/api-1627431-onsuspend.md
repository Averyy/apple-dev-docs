# onSuspend

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

A callback function that is automatically called when the app is sent to the background.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute function onSuspend;
```

#### Discussion

Use the `onSuspend` attribute to stop any actions when the app moves from the foreground to the background. This attribute must be set to a function that accepts an `options` argument; for example `App.onSuspend = function (options) {}`. The `options` argument is always set to `null`.

## See Also

### Responding to App Life Cycle Events
- [onError](./api-1627353-onerror.md)
  A callback function that is automatically called when an error is sent from the Apple TV.
- [onExit](./api-1627419-onexit.md)
  A callback function that is automatically called when the app has been exited.
- [onLaunch](./api-1627407-onlaunch.md)
  A callback function that is automatically called when the app has been launched.
- [onResume](./api-1627415-onresume.md)
  A callback function that is automatically called when the app moves to the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627431-onsuspend)*