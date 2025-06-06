# initTouchEvent

**Framework**: Webkitjs  
**Kind**: instm

Initializes a newly created `TouchEvent` object.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
void initTouchEvent(
    optional DOMString type, 
    optional boolean canBubble, 
    optional boolean cancelable, 
    optional DOMWindow? view, 
    optional long detail, 
    optional long screenX, 
    optional long screenY, 
    optional long clientX, 
    optional long clientY, 
    optional boolean ctrlKey, 
    optional boolean altKey, 
    optional boolean shiftKey, 
    optional boolean metaKey, 
    optional TouchList? touches, 
    optional TouchList? targetTouches, 
    optional TouchList? changedTouches, 
    optional float scale, 
    optional float rotation
);
```

#### Discussion

Use this method to programmatically create a `TouchEvent` object.

## Parameters

- `type`: The type of event that occurred.
- `canBubble`: Indicates whether an event can bubble. If  , the event can bubble; otherwise, it cannot.
- `cancelable`: Indicates whether an event can have its default action prevented. If  , the default action can be prevented; otherwise, it cannot.
- `view`: The view (DOM window) in which the event occurred.
- `detail`: Specifies some detail information about the event depending on the type of event.
- `screenX`: The x-coordinate of the event’s location in screen coordinates.
- `screenY`: The y-coordinate of the event’s location in screen coordinates.
- `clientX`: The x-coordinate of the event’s location relative to the window’s viewport.
- `clientY`: The y-coordinate of the event’s location relative to the window’s viewport.
- `ctrlKey`: If  , the control key is pressed; otherwise, it is not.
- `altKey`: If  , the alt key is pressed; otherwise, it is not.
- `shiftKey`: If  , the shift key is pressed; otherwise, it is not.
- `metaKey`: If  , the meta key is pressed; otherwise, it is not.
- `touches`: A collection of   objects representing all touches associated with this event.
- `targetTouches`: A collection of   objects representing all touches associated with this target.
- `changedTouches`: A collection of   objects representing all touches that changed in this event.
- `scale`: The distance between two fingers since the start of an event as a multiplier of the initial distance. The initial value is  . If less than  , the gesture is pinch close (to zoom out). If greater than  , the gesture is pinch open (to zoom in).
- `rotation`: The delta rotation since the start of an event, in degrees, where clockwise is positive and counter-clockwise is negative. The initial value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touchevent/1631943-inittouchevent)*