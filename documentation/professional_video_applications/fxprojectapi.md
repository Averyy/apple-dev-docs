# FxProjectAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Methods you use to get information about the project in which your plug-in instance is running.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
protocol FxProjectAPI
```

```objc
@protocol FxProjectAPI
```

## Topics

### Getting Project Information from the Host
- [func mediaFolderURL(AutoreleasingUnsafeMutablePointer<NSURL?>!) throws](./fxprojectapi/mediafolderurl%28_%29.md)
  Provides the security-scoped URL for a plug-in data folder within a project’s media folder.
- [func documentID(UnsafeMutablePointer<Int>!) throws](./fxprojectapi/documentid%28_%29.md)
  Provides the document ID number of the host’s project.

## Relationships

### Inherited By
- [FxProjectAPI_v2](./fxprojectapi_v2.md)

## See Also

### Accessing host data
- [protocol FxProjectAPI_v2](./fxprojectapi_v2.md)
  The method you use to get aspect ratio information about the project in which your plug-in instance is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprojectapi)*