# name

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The name of the host app.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, readonly) NSString * name;
```

## Parameters

- `name`: A string object that identifies the name of the host app.

## See Also

### Getting the Host Object Details
- [var bundleIdentifier: String](./bundleidentifier.md)
  A unique string that identifies a host app to the system.
- [var timeline: FCPXTimeline?](./timeline.md)
  A pointer to the Final Cut Pro timeline proxy object.
- [var versionString: String](./versionstring.md)
  The version number of the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxhost/name)*