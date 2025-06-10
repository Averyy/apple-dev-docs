# VNRequestProgressProviding

**Framework**: Vision  
**Kind**: protocol

A protocol for providing progress information on long-running tasks in Vision.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol VNRequestProgressProviding : NSObjectProtocol
```

#### Overview

Adopt this protocol for potentially long-running Vision requests to provide information about progress throughout processing. For example, you can use the optional [`progressHandler`](vnrequestprogressproviding/progresshandler.md) to update the user interface, provide a percentage of completion, or process partial results.

> **Note**:  The Vision framework may call the progress handler on a different dispatch queue from the thread on which you initiated the original request, so ensure that your handler can execute asynchronously, in a thread-safe manner.

## Topics

### Tracking Progress
- [var progressHandler: VNRequestProgressHandler](vnrequestprogressproviding/progresshandler.md)
  A block of code executed periodically during a Vision request to report progress on long-running tasks.
- [var indeterminate: Bool](vnrequestprogressproviding/indeterminate.md)
  A Boolean set to true when a request can’t determine its progress in fractions completed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VNRecognizeTextRequest](vnrecognizetextrequest.md)

## See Also

- [typealias VNRequestProgressHandler](vnrequestprogresshandler.md)
  A block executed at intervals during the processing of a Vision request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequestprogressproviding)*