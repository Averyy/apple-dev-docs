# init(frameWidth:frameHeight:sourcePixelFormat:)

**Framework**: Video Toolbox  
**Kind**: init  
**Role**: Initializer

Creates a new temporal noise-processor configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, sourcePixelFormat: OSType)
```

```objc
- (instancetype) initWithFrameWidth:(NSInteger) frameWidth frameHeight:(NSInteger) frameHeight sourcePixelFormat:(OSType) sourcePixelFormat;
```

## Discussion

Returns nil if frameWidth, frameHeight, or sourcePixelFormat is unsupported.

## Parameters

- `frameWidth`: Width of source frame in pixels.
- `frameHeight`: Height of source frame in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterconfiguration/init(framewidth:frameheight:sourcepixelformat:))*