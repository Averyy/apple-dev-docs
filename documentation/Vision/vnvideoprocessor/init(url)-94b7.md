# init(url:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a video processor to perform Vision requests against the specified video asset.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(url videoURL: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) videoURL;
```

## Parameters

- `videoURL`: The video asset URL. The specified asset must be a video format supported by AVFoundation.

## See Also

### Creating a Video Processor
- [init(URL: URL)](./init%28url%29-38vj9.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/init(url:)-94b7)*