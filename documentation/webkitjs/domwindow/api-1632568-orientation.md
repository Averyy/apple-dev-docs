# orientation

**Framework**: Webkitjs  
**Kind**: instp

Specifies the orientation of the device.

**Availability**:
- Safari Mobile 9.0+

## Declaration

```swift
readonly attribute long orientation;
```

#### Discussion

This property is set to one of the values in [`Table 1`](domwindow/1632568-orientation#1965650.md). For example, if the user starts with the device in portrait orientation and then changes to landscape orientation by turning the device to the right, the window’s `orientation` property is set to `-90`. If the user instead changes to landscape by turning the device to the left, the window’s `orientation` property is set to `90`. The default value is `0`.

| Value | Description |
| --- | --- |
| `0` | Portrait orientation. This is the default value. |
| `-90` | Landscape orientation with the screen turned clockwise. |
| `90` | Landscape orientation with the screen turned counterclockwise. |
| `180` | Portrait orientation with the screen turned upside down. This value is currently not supported on iPhone. |

## See Also

- [ondevicemotion](domwindow/1632048-ondevicemotion.md)
  The event listener that is called when the device motion changes. 
- [ondeviceorientation](domwindow/1628872-ondeviceorientation.md)
  The event listener that is called while the device orientation changes around the x, y, and z axes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/domwindow/1632568-orientation)*