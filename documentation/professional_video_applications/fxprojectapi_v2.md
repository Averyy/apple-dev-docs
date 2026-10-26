# FxProjectAPI_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

The method you use to get aspect ratio information about the project in which your plug-in instance is running.

**Availability**:
- FxPlug 4.2.9+

## Declaration

```swift
protocol FxProjectAPI_v2 : FxProjectAPI
```

```objc
@protocol FxProjectAPI_v2 <FxProjectAPI>
```

## Topics

### Getting Project Aspect Ratio from the Host
- [func projectAspectRatio(UnsafeMutablePointer<Float>!) throws](./fxprojectapi_v2/projectaspectratio%28_%29.md)
  Provides the aspect ratio of the host’s project.

## Relationships

### Inherits From
- [FxProjectAPI](./fxprojectapi.md)

## See Also

### Accessing host data
- [protocol FxProjectAPI](./fxprojectapi.md)
  Methods you use to get information about the project in which your plug-in instance is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprojectapi_v2)*