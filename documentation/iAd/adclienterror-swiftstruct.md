# ADClientError

**Framework**: iAd  
**Kind**: struct

The group of error codes that pass from the attribution response to the completion handler block.

## Declaration

```swift
struct ADClientError
```

## Mentions

- [iAd Changelog](iad-changelog.md)

#### Overview

When you call the [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md) method, error codes are passed from the attribution response to the completion handler block.

## Topics

### Error Codes
- [static var corruptResponse: ADClientError.Code](adclienterror-swift.struct/corruptresponse.md)
  The response received from the attribution server was corrupt.
- [static var requestClientError: ADClientError.Code](adclienterror-swift.struct/requestclienterror.md)
  The response received from the attribution server had an HTTP 4xx status code.
- [static var requestNetworkError: ADClientError.Code](adclienterror-swift.struct/requestnetworkerror.md)
  The communication with the attribution server had a network error.
- [static var requestServerError: ADClientError.Code](adclienterror-swift.struct/requestservererror.md)
  The response received from the attribution server had an HTTP 5xx status code.
- [static var trackingRestrictedOrDenied: ADClientError.Code](adclienterror-swift.struct/trackingrestrictedordenied.md)
  The user is restricted or has denied tracking for the calling application.
- [static var missingData: ADClientError.Code](adclienterror-swift.struct/missingdata.md)
  The downloaded app received a payload lacking enough data to perform an attribution check.
- [static var unsupportedPlatform: ADClientError.Code](adclienterror-swift.struct/unsupportedplatform.md)
  The attribution API was called on an unsupported platform.
- [static var limitAdTracking: ADClientError.Code](adclienterror-swift.struct/limitadtracking.md)
- [static var unknown: ADClientError.Code](adclienterror-swift.struct/unknown.md)
- [ADClientError.Code](adclienterror-swift.struct/code.md)
  The error codes that pass from the attribution response to the completion handler.
### Error Characteristics
- [let ADClientErrorDomain: String](adclienterrordomain.md)
  The error domain that passes to the completion handler.
### Type Properties
- [static var errorDomain: String](adclienterror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let ADClientErrorDomain: String](adclienterrordomain.md)
  The error domain that passes to the completion handler.
- [ADClientError.Code](adclienterror-swift.struct/code.md)
  The error codes that pass from the attribution response to the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclienterror-swift.struct)*