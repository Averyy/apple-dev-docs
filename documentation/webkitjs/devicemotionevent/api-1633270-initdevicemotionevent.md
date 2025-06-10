# initDeviceMotionEvent

**Framework**: WebKit JS  
**Kind**: instm

Initializes a new device motion event.

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
void initDeviceMotionEvent(
    optional DOMString type, 
    optional boolean bubbles, 
    optional boolean cancelable, 
    optional Acceleration acceleration, 
    optional Acceleration accelerationIncludingGravity, 
    optional RotationRate rotationRate, 
    optional unrestricted double interval
);
```

## Parameters

- `type`: The type of event. Pass  .
- `bubbles`: Indicates whether this event is a bubbling event.
- `cancelable`: Indicates whether this event can be canceled.
- `acceleration`: The acceleration that the user is giving to the device. The   object has  ,  , and   properties represented as doubles.
- `accelerationIncludingGravity`: The total acceleration of the device, which includes the user acceleration and the gravity. The   object has  ,  , and   properties represented as doubles.
- `rotationRate`: The rotation rate of the device. The   object has  ,  , and   properties represented as doubles.
- `interval`: The interval in milliseconds since the last time this event was fired.

## See Also

- [Safari Web Content Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002051)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/devicemotionevent/1633270-initdevicemotionevent)*