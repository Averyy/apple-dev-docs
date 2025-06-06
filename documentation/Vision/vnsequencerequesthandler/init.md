# init()

**Framework**: Vision  
**Kind**: init

Initializes a sequence request handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Discussion

Unlike the [`VNImageRequestHandler`](vnimagerequesthandler.md), this initializer accepts no input because image data and auxiliary parameters may change from frame to frame, and are handled dynamically in the request-handling `perform` methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsequencerequesthandler/init())*