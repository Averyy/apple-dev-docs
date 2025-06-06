# init(completionHandler:)

**Framework**: Vision  
**Kind**: init

Creates a new Vision request with an optional completion handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(completionHandler: VNRequestCompletionHandler? = nil)
```

#### Discussion

Vision executes the completion handler on the same queue that it executes the request; however, this queue differs from the one where you called [`perform(_:)`](vnimagerequesthandler/perform(_:).md).

## Parameters

- `completionHandler`: The block to invoke after the request finishes processing.

## See Also

- [convenience init()](vnrequest/init.md)
  Creates a new Vision request with no completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/init(completionhandler:))*