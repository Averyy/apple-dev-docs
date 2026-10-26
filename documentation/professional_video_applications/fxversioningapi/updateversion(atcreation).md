# updateVersion(atCreation:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates the version of the plug-in that was stored when the plug-in was added to the clip.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func updateVersion(atCreation newVersion: UInt32) -> Bool
```

```objc
- (BOOL) updateVersionAtCreation:(UInt32) newVersion;
```

## Mentions

- [Versioning and obsoleting old plug-ins](../../Professional-Video-Applications/versioning-and-obsoleting-old-plug-ins.md)

#### Return Value

If the update was successful, this method returns `YES`; otherwise, `NO`.

#### Discussion

No information about previous backward compatibility is stored, and the plug-in is treated by the host app as if it were created with the specified version number. Updating fails if the specified number is lower than the already-saved version number.

## Parameters

- `newVersion`: The new version number.

## See Also

### Getting and Modifying Plug-in Version Numbers
- [func versionAtCreation() -> UInt32](./versionatcreation%28%29.md)
  Provides the version number of a plug-in that a project uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxversioningapi/updateversion(atcreation:))*