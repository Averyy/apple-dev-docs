# currentTime()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the current time, expressed as a rational time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func currentTime() -> CMTime
```

```objc
- (CMTime) currentTime;
```

## Mentions

- [Scheduling media in plug-ins](https://developer.apple.com/documentation/professional-video-applications/scheduling-media-in-plug-ins)
- [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug)

#### Return Value

The current time, expressed as a rational time.

#### Discussion

This is useful when a custom parameter view needs to set a parameter value in response to a user event. Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug).

> ❗ **Important**: Only use `-currentTime` from within methods that are not provided the time by the host. For example, when updating a custom view.

## See Also

### Instance Methods
- [func startAction(Any!)](./startaction%28_%29.md)
  Prepares the host to access parameters.
- [func endAction(Any!)](./endaction%28_%29.md)
  Tells the host application that the plug-in is done accessing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameteractionapi_v4/currenttime())*