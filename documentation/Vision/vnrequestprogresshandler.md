# VNRequestProgressHandler

**Framework**: Vision  
**Kind**: typealias

A block executed at intervals during the processing of a Vision request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
typealias VNRequestProgressHandler = (VNRequest, Double, (any Error)?) -> Void
```

#### Discussion

Vision may populate the [`results`](vnrequest/results.md) array in the request with partial data, before all results are ready.

> **Note**:  The Vision framework may call the progress handler on a different dispatch queue from the thread on which you initiated the original request, so ensure that your handler can execute asynchronously, in a thread-safe manner.

## Parameters

- `request`: The completed Vision request. The results of the request, if no error occurred, reside in the   array of the request.
- `fractionCompleted`: The fraction of the request that is completed, reported between   and  . If the   property is set, this value is undefined.
- `error`: The error that caused the request to fail, or   if the request completed successfully.

## See Also

- [protocol VNRequestProgressProviding](vnrequestprogressproviding.md)
  A protocol for providing progress information on long-running tasks in Vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Vision/vnrequestprogresshandler)*