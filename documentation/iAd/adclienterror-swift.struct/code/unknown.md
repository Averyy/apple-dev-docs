# ADClientError.Code.unknown

**Framework**: iAd  
**Kind**: case

The response from the attribution server has an unknown error.

## Declaration

```swift
case unknown
```

#### Discussion

Wait a few seconds and try again. When you’ve successfully retrieved your attribution data, you don’t need to poll for data again. The values you retrieve don’t change.

## See Also

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
- [static var limitAdTracking: ADClientError.Code](adclienterror-swift.struct/code/limitadtracking.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclienterror-swift.struct/code/unknown)*