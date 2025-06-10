# WebKitTransitionEvent

**Framework**: WebKit JS  
**Kind**: cl

`WebKitTransitionEvent` objects provide information about CSS transitions specified using the `transition` property. An event is sent at the end of a transition for each CSS property in the transition. Each event contains the name of the CSS property and duration of the transition. You can use these events to perform some action that starts at the end of a transition.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 2.0+

## Declaration

```swift
interface WebKitTransitionEvent
```

#### Overview

For more on CSS transition events, see https://www.w3.org/TR/css3-transitions/#transition-events.

## Topics

### Accessing Properties
- [propertyName](webkittransitionevent/1630487-propertyname.md)
  The name of the CSS property associated with the transition.
- [elapsedTime](webkittransitionevent/1629406-elapsedtime.md)
  The duration of the transition, in seconds, since this event was sent. This value is not affected by the value of the CSS `transition-delay` property.
### Initializing
- [initWebKitTransitionEvent](webkittransitionevent/1806991-initwebkittransitionevent.md)
  Initializes a new transition event object.
### Instance Properties
- [pseudoElement](webkittransitionevent/1632635-pseudoelement.md)
  An abstract element representing the portion of the CSS render tree on which the transition occurs.

## Relationships

### Inherits From
- [Event](../tvmljs/event.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkittransitionevent)*