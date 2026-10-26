# imageSize(_:fromParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the dimensions of the image well image when it is at 100-percent scale and has square pixels.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
func imageSize(_ imageSize: UnsafeMutablePointer<CGSize>, fromParameter parameterID: UInt32, at time: CMTime) throws
```

```objc
- (BOOL) imageSize:(CGSize *) imageSize fromParameter:(UInt32) parameterID atTime:(CMTime) time error:(NSError * *) error;
```

#### Discussion

Removes the effects of pixel aspect ratio, fields, proxy resolution scaling, or user scaling, and provides the dimensions of the image well image in image space.

## Parameters

- `imageSize`: The size of the image in image space.
- `parameterID`: The ID of the image parameter for which you want to retrieve size.
- `time`: The time at which you want to get the image size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v7/imagesize(_:fromparameter:at:))*