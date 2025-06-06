# elapsedTime

**Framework**: Webkitjs  
**Kind**: instp

The duration of the animation, in seconds, since this event was sent, excluding any time the animation is paused. This value is not affected by the value of the CSS -webkit-animation-delay property. If the type of the event is `webkitAnimationStart`, `elapsedTime` is `0`.

**Availability**:
- Safari Desktop 4.0+
- Safari Mobile 2.0+

## Declaration

```swift
readonly attribute double elapsedTime;
```

## See Also

- [animationName](webkitanimationevent/1634262-animationname.md)
  The name of the animation. The value of the CSS -webkit-animation-name property of the animation that caused the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitanimationevent/1633014-elapsedtime)*