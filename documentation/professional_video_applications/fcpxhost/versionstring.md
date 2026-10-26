# versionString

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The version number of the host app.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
var versionString: String { get }
```

```objc
@property (nonatomic, readonly) NSString * versionString;
```

## Parameters

- `versionString`: A string object identifying the version of the host app.

## See Also

### Getting the Host Object Details
- [var bundleIdentifier: String](./bundleidentifier.md)
  A unique string that identifies a host app to the system.
- [var name: String](./name.md)
  The name of the host app.
- [var timeline: FCPXTimeline?](./timeline.md)
  A pointer to the Final Cut Pro timeline proxy object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxhost/versionstring)*