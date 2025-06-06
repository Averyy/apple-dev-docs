# ADClient

**Framework**: iAd  
**Kind**: class

The parent class you use to request an attribution response.

## Declaration

```swift
class ADClient
```

#### Overview

To use this class, fetch the shared client object, [`shared()`](adclient/shared().md). Then call its [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md) method, passing in a block to be called with the result.

## Topics

### Fetching a Shared Client Object
- [class func shared() -> ADClient](adclient/shared.md)
  Gets an instance of ADClient.
### Requesting Ad Attribution
- [func requestAttributionDetails(([String : NSObject]?, (any Error)?) -> Void)](adclient/requestattributiondetails(_:).md)
  Gets an attribution response.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [iAd Changelog](iad-changelog.md)
  Learn what’s new in the Apple Search Ads iAd Attribution API.
- [Setting Up Apple Search Ads Attribution](setting-up-apple-search-ads-attribution.md)
  Retrieve the attribution dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclient)*