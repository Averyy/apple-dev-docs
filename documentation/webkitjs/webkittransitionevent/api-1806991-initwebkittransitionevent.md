# initWebKitTransitionEvent

**Framework**: WebKit JS  
**Kind**: uid

Initializes a new transition event object.

## Declaration

```swift
void initWebKitTransitionEvent (in DOMString typeArg, in boolean canBubbleArg, in boolean cancelableArg, in DOMString propertyNameArg, in double elapsedTimeArg);
```

#### Overview

You use this method to initialize the value of a `WebKitTransitionEvent` object that is created through the `DocumentEvent` interface. This method can only be invoked before the `WebKitTransitionEvent` object is dispatched via the `dispatchEvent` method (although, it can be invoked multiple times during that phase, if necessary). If it is invoked multiple times, the final invocation takes precedence.

## Parameters

- `typeArg`: The type of event.  Possible values for this argument are described in `Types of Transition Events`. This type of event can bubble and be canceled. Its `propertyName` property is always set.
- `canBubbleArg`: Determines whether the event can bubble. Pass `true` if it can bubble; otherwise, `false`.
- `cancelableArg`: Determines whether the event’s default action can be prevented. Pass `true` if it can be prevented; otherwise, `false`.
- `propertyNameArg`: The name of the CSS property associated with this event.
- `elapsedTimeArg`: The duration of the transition, in seconds, since the event was sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/webkittransitionevent/1806991-initwebkittransitionevent)*