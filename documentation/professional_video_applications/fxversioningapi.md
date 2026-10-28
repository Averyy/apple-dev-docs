# FxVersioningAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A collection of methods that a host application implements to identify the plug-in version used by a project when it was first created.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
protocol FxVersioningAPI
```

```objc
@protocol FxVersioningAPI
```

## Mentions

- [Versioning and obsoleting old plug-ins](../Professional-Video-Applications/versioning-and-obsoleting-old-plug-ins.md)
- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)

## Overview

This protocol allows a plug-in instance to determine the version of the original instance of the plug-in. For example, if a user creates a project using version 1 of a plug-in, and then updates to version 2, the plug-in determines the old plug-in version and chooses which version to render.

This protocol was first introduced in FxPlug SDK 1.2.1.

## Topics

### Getting and Modifying Plug-in Version Numbers
- [func versionAtCreation() -> UInt32](./fxversioningapi/versionatcreation%28%29.md)
  Provides the version number of a plug-in that a project uses.
- [func updateVersion(atCreation: UInt32) -> Bool](./fxversioningapi/updateversion%28atcreation%29.md)
  Updates the version of the plug-in that was stored when the plug-in was added to the clip.

## See Also

### Legacy plug-ins
- [Migrating FxPlug 3 plug-ins to FxPlug 4](../Professional-Video-Applications/migrating-fxplug-3-plug-ins-to-fxplug-4.md)
  Update existing FxPlug 3 plug-ins to out-of-process FxPlug 4 plug-ins.
- [Versioning and obsoleting old plug-ins](../Professional-Video-Applications/versioning-and-obsoleting-old-plug-ins.md)
  Version plug-ins to add new capabilities, or obsolete them to remove them from the Motion Library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxversioningapi)*