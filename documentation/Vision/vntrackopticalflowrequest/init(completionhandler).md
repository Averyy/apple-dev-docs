# init(completionHandler:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new request that tracks the optical from one image to another, with a system callback on completion.

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

### Creating an Optical Flow
- [init()](./init%28%29.md)
  Creates a new request that tracks the optical from one image to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/init(completionhandler:))*