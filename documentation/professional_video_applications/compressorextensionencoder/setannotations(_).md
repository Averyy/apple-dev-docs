# setAnnotations(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds annotations to an encoded media file.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setAnnotations(_ annotations: [AnyHashable : Any]!)
```

```objc
- (void) setAnnotations:(NSDictionary *) annotations;
```

## Parameters

- `annotations`: A dictionary of source media annotations.

## See Also

### Setting Encoding Values
- [func setSettings(CompressorExtensionSettingsPtr!)](./setsettings%28_%29.md)
  Sets the current encoding settings based on the given setting values.
- [func setChapters([[AnyHashable : Any]]!)](./setchapters%28_%29.md)
  Sets chapter markers of an encoded file from the contents of the input dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/setannotations(_:))*