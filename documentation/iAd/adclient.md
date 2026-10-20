# ADClient

**Framework**: iAd  
**Kind**: class  
**Role**: Class

The parent class you use to request an attribution response.

## Declaration

```objc
@interface ADClient : NSObject
```

#### Overview

To use this class, fetch the shared client object, `shared()`. Then call its `requestAttributionDetails(_:)` method, passing in a block to be called with the result.

## Topics

### Instance Methods
- [- requestAttributionDetailsWithBlock:](./adclient/requestattributiondetailswithblock_.md)
### Type Methods
- [+ sharedClient](./adclient/sharedclient.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Essentials
- [iAd Changelog](./iad-changelog.md)
  Learn what’s new in the Apple Search Ads iAd Attribution API.
- [Setting Up Apple Search Ads Attribution](./setting-up-apple-search-ads-attribution.md)
  Retrieve the attribution dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclient)*