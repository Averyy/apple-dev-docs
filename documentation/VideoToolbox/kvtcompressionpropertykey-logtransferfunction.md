# kVTCompressionPropertyKey_LogTransferFunction

**Framework**: Video Toolbox  
**Kind**: var

Indicates that the transfer function or gamma of the content is a log format and identifies the specific log curve. Log curve identifiers include `kCVImageBufferLogTransferFunction_AppleLog` (“com.apple.rec2020.apple-log”) and `kCVImageBufferLogTransferFunction_AppleLog2` (“com.apple.apple-wide-gamut.apple-log”). When the LogTransferFunction is specified for a VTCompressionSession, if source image buffers do not have exactly that LogTransferFunction, encoding will fail.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let kVTCompressionPropertyKey_LogTransferFunction: CFString
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_logtransferfunction)*