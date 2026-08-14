# ADClient

**Framework**: iAd  
**Kind**: class

The parent class you use to request an attribution response.

## Declaration

```swift
@interface ADClient : NSObject
```

#### Overview

To use this class, fetch the shared client object, `shared()`. Then call its `requestAttributionDetails(_:)` method, passing in a block to be called with the result.

## Topics

### Instance Methods
- [- requestAttributionDetailsWithBlock:](adclient/requestattributiondetailswithblock:.md)
### Type Methods
- [+ sharedClient](adclient/sharedclient.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [iAd Changelog](iad-changelog.md)
  Learn what’s new in the Apple Search Ads iAd Attribution API.
- [Setting Up Apple Search Ads Attribution](setting-up-apple-search-ads-attribution.md)
  Retrieve the attribution dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclient)*