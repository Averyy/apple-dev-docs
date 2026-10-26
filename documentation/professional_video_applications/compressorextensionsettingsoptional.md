# CompressorExtensionSettingsOptional

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An interface you use to receive updated values of source media attributes.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
protocol CompressorExtensionSettingsOptional
```

```objc
@protocol CompressorExtensionSettingsOptional
```

#### Overview

When a user updates the source media settings for an encoding job, the Compressor app calls the [`setJobSourceAttributes(_:)`](./compressorextensionsettingsoptional/setjobsourceattributes%28_%29.md) method to pass the updated values to the encoder extension. Use the source media attributes to configure the encoding settings that have values set to automatic.

## Topics

### Setting Source Attributes
- [func setJobSourceAttributes([AnyHashable : Any]!)](./compressorextensionsettingsoptional/setjobsourceattributes%28_%29.md)
  Sets the source media attributes based on the given values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettingsoptional)*