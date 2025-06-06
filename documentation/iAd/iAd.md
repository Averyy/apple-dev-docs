# iAd

**Framework**: iAd  
**Kind**: module

The Apple Search Ads iAd Attribution API is a legacy framework for attributing app data that originates from Apple Search Ads campaigns on iOS devices.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+

#### Overview

> ⚠️ **Warning**:  After February 7, 2023, all requests made to the Apple Search Ads iAd Attribution API will return with a value of `"iad-attribution"` `=` `false`, or errors. See [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md). Use the [`AdServices`](https://developer.apple.com/documentation/AdServices) framework for current attribution integration with the [`Apple Search Ads`](https://developer.apple.com/documentation/apple_search_ads) Campaign Management API for devices using iOS 14.3 and later. Attribution isn’t available for downloads and redownloads from devices using iOS 14.2 or earlier.

 After February 7, 2023, all requests made to the Apple Search Ads iAd Attribution API will return with a value of `"iad-attribution"` `=` `false`, or errors. See [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md). Use the [`AdServices`](https://developer.apple.com/documentation/AdServices) framework for current attribution integration with the [`Apple Search Ads`](https://developer.apple.com/documentation/apple_search_ads) Campaign Management API for devices using iOS 14.3 and later. Attribution isn’t available for downloads and redownloads from devices using iOS 14.2 or earlier.

Attribution data consists of campaign metadata from app ads, such as app downloads and redownloads that result from taps on ads created through the Apple Search Ads user interface or the Apple Search Ads API.

All Apple Search Ads data that Apple collects is subject to the [`Apple Privacy Policy`](https://developer.apple.comhttps://www.apple.com/privacy).

## Topics

### Essentials
- [iAd Changelog](iad-changelog.md)
  Learn what’s new in the Apple Search Ads iAd Attribution API.
- [Setting Up Apple Search Ads Attribution](setting-up-apple-search-ads-attribution.md)
  Retrieve the attribution dictionary.
- [class ADClient](adclient.md)
  The parent class you use to request an attribution response.
### Attribution Errors
- [let ADClientErrorDomain: String](adclienterrordomain.md)
  The error domain that passes to the completion handler.
- [struct ADClientError](adclienterror-swift.struct.md)
  The group of error codes that pass from the attribution response to the completion handler block.
- [ADClientError.Code](adclienterror-swift.struct/code.md)
  The error codes that pass from the attribution response to the completion handler.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Reference symbols from the legacy iAd framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iAd)*