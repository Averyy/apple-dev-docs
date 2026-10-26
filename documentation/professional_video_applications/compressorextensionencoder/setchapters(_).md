# setChapters(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets chapter markers of an encoded file from the contents of the input dictionary.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setChapters(_ chapters: [[AnyHashable : Any]]!)
```

```objc
- (void) setChapters:(NSArray<NSDictionary *> *) chapters;
```

## Parameters

- `chapters`: An array of source media chapter markers.

## See Also

### Setting Encoding Values
- [func setSettings(CompressorExtensionSettingsPtr!)](./setsettings%28_%29.md)
  Sets the current encoding settings based on the given setting values.
- [func setAnnotations([AnyHashable : Any]!)](./setannotations%28_%29.md)
  Adds annotations to an encoded media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/setchapters(_:))*