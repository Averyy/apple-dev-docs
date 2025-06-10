# WebKitAnimationEvent

**Framework**: WebKit JS  
**Kind**: cl

`WebKitAnimationEvent` objects encapsulate information about running animations.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 2.0+

## Declaration

```swift
interface WebKitAnimationEvent
```

#### Overview

Several animation related events are available through the DOM Event system. The start and end of an animation, and the end of each iteration of an animation all generate DOM events. An element can have multiple properties that are animated simultaneously. This simultaneous animation can occur either by setting a single -webkit-animation-name value with keyframes containing multiple properties, or by setting multiple `-webkit-animation-name` values. For the purposes of event dispatching, each CSS `-webkit-animation-name` property specifies a single animation. Therefore, an event is sent for each `-webkit-animation-name` property, not necessarily for each CSS property that is animated.

Each event contains the duration of the animation. This allows the event handler to determine the current iteration of a looping animation or the current position of an alternating animation. This duration does not include time the animation was in the paused play state.

##### 1652505

The `type` property of an animation event can have the following string values:

## Topics

### Accessing Properties
- [animationName](webkitanimationevent/1634262-animationname.md)
  The name of the animation. The value of the CSS -webkit-animation-name property of the animation that caused the event.
- [elapsedTime](webkitanimationevent/1633014-elapsedtime.md)
  The duration of the animation, in seconds, since this event was sent, excluding any time the animation is paused. This value is not affected by the value of the CSS -webkit-animation-delay property. If the type of the event is `webkitAnimationStart`, `elapsedTime` is `0`.
### Initializing Objects
- [initWebKitAnimationEvent](webkitanimationevent/1807040-initwebkitanimationevent.md)
  Initializes a new animation event object.

## Relationships

### Inherits From
- [Event](../tvmljs/event.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkitanimationevent)*