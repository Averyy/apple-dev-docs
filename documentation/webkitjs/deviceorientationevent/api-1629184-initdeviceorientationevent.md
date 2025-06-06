# initDeviceOrientationEvent

**Framework**: Webkitjs  
**Kind**: instm

Initializes a new device orientation event.

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
void initDeviceOrientationEvent(
    optional DOMString type, 
    optional boolean bubbles, 
    optional boolean cancelable, 
    optional unrestricted double alpha, 
    optional unrestricted double beta, 
    optional unrestricted double gamma, 
    optional boolean absolute
);
```

## Parameters

- `type`: The type of event. Pass  .
- `bubbles`: A Boolean value that indicates whether this event is a bubbling event.
- `cancelable`: A Boolean value that indicates whether this event can be canceled.
- `alpha`: The rotation, in degrees, of the device frame around its z-axis.
- `beta`: The rotation, in degrees, of the device frame around its x-axis.
- `gamma`: The rotation, in degrees, of the device frame around its y-axis.
- `compassHeading`: A direction that is measured in degrees relative to magnetic north.
- `compassAccuracy`: The accuracy of the compass data in degrees.

## See Also

- [Safari Web Content Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002051)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/deviceorientationevent/1629184-initdeviceorientationevent)*