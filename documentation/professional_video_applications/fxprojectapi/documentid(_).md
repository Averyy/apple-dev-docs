# documentID(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the document ID number of the host’s project.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
func documentID(_ documentID: UnsafeMutablePointer<Int>!) throws
```

```objc
- (BOOL) documentID:(NSUInteger *) documentID error:(NSError * *) error;
```

## Discussion

Use this method to get the document ID number of the host application’s project.

## Parameters

- `documentID`: The document ID.

## See Also

### Getting Project Information from the Host
- [func mediaFolderURL(AutoreleasingUnsafeMutablePointer<NSURL?>!) throws](./mediafolderurl%28_%29.md)
  Provides the security-scoped URL for a plug-in data folder within a project’s media folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprojectapi/documentid(_:))*