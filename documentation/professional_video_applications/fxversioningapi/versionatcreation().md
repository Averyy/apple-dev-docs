# versionAtCreation()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the version number of a plug-in that a project uses.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func versionAtCreation() -> UInt32
```

```objc
- (unsigned int) versionAtCreation;
```

## Mentions

- [Versioning and obsoleting old plug-ins](https://developer.apple.com/documentation/professional-video-applications/versioning-and-obsoleting-old-plug-ins)
- [Adding parameters to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)

#### Return Value

An integer representation of the version number.

#### Discussion

Typically, a plug-in’s version increments with each release. The exact semantics are up to the plug-in developer.

To support versioning, each plug-in within a bundle defines its current version number as a string value with a `version` key in the plug-in’s entry in the `ProPlugPlugInList` array in the plug-in’s Info.plist.

When a project is first created, the host application remembers the version number of each plug-in used in that project. Later, when the user opens the project, a plug-in can query the value of `versionAtCreation` and then handle any backward-compatibility issues.

## See Also

### Getting and Modifying Plug-in Version Numbers
- [func updateVersion(atCreation: UInt32) -> Bool](./updateversion%28atcreation%29.md)
  Updates the version of the plug-in that was stored when the plug-in was added to the clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxversioningapi/versionatcreation())*