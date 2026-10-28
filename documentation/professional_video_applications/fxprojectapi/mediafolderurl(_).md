# mediaFolderURL(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the security-scoped URL for a plug-in data folder within a project’s media folder.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
func mediaFolderURL(_ mediaURL: AutoreleasingUnsafeMutablePointer<NSURL?>!) throws
```

```objc
- (BOOL) mediaFolderURL:(NSURL * *) mediaURL error:(NSError * *) error;
```

## Discussion

Use this method to get the URL for a plug-in-specific directory within the media folder of a Motion project. The `mediaURL` will be `nil` if the user has not saved the project or the user did not select the “Collect Media” feature when saving. A sandboxed plug-in needs to add the appropriate entitlements to use security-scoped bookmarks to use this URL.

## Parameters

- `mediaURL`: The NSURL of a directory within the media folder of a Motion project.

## See Also

### Getting Project Information from the Host
- [func documentID(UnsafeMutablePointer<Int>!) throws](./documentid%28_%29.md)
  Provides the document ID number of the host’s project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprojectapi/mediafolderurl(_:))*