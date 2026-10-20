# init(completionHandler:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new 3D body pose request with a completion handler.

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

- `completionHandler`: The block to invoke after the request finishes processing.

## See Also

### Initializing a Request
- [init()](./init%28%29.md)
  Creates a new request with no completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest/init(completionhandler:))*