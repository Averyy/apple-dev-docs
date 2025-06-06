# ADClientError.Code

**Framework**: iAd  
**Kind**: enum

The error codes that pass from the attribution response to the completion handler.

## Declaration

```swift
enum Code
```

#### Overview

The group of error codes that pass from the attribution response to the completion handler block when you call the [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md) method.

## Topics

### Error Codes
- [ADClientError.Code.corruptResponse](adclienterror-swift.struct/code/corruptresponse.md)
  The response from the attribution server is corrupt.
- [ADClientError.Code.requestClientError](adclienterror-swift.struct/code/requestclienterror.md)
  The response from the attribution server has an HTTP 4xx status code.
- [ADClientError.Code.requestNetworkError](adclienterror-swift.struct/code/requestnetworkerror.md)
  The communication with the attribution server has a network error.
- [ADClientError.Code.requestServerError](adclienterror-swift.struct/code/requestservererror.md)
  The response from the attribution server has an HTTP 5xx status code.
- [ADClientError.Code.trackingRestrictedOrDenied](adclienterror-swift.struct/code/trackingrestrictedordenied.md)
  The user has a restricted status or has denied tracking for the calling app.
- [ADClientError.Code.missingData](adclienterror-swift.struct/code/missingdata.md)
  The downloaded app has a payload without enough data to perform an attribution check.
- [ADClientError.Code.unsupportedPlatform](adclienterror-swift.struct/code/unsupportedplatform.md)
  The system doesn’t support the platform for the attribution API call.
- [ADClientError.Code.unknown](adclienterror-swift.struct/code/unknown.md)
  The response from the attribution server has an unknown error.
- [static var limitAdTracking: ADClientError.Code](adclienterror-swift.struct/code/limitadtracking.md)
### Initializers
- [init?(rawValue: Int)](adclienterror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let ADClientErrorDomain: String](adclienterrordomain.md)
  The error domain that passes to the completion handler.
- [struct ADClientError](adclienterror-swift.struct.md)
  The group of error codes that pass from the attribution response to the completion handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclienterror-swift.struct/code)*