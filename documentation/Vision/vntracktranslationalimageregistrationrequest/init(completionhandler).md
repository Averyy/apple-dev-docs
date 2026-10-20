# init(completionHandler:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new request that tracks the translational registration of two images, with a system callback on completion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(completionHandler: VNRequestCompletionHandler? = nil)
```

```objc
- (instancetype) initWithCompletionHandler:(VNRequestCompletionHandler) completionHandler;
```

## Parameters

- `completionHandler`: The callback the system invokes when it completes the request.

## See Also

### Creating a Translational Image
- [init()](./init%28%29.md)
  Creates a new request that tracks the translational registration of two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntracktranslationalimageregistrationrequest/init(completionhandler:))*