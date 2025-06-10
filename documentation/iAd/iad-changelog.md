# iAd Changelog

**Framework**: iAd

Learn what’s new in the Apple Search Ads iAd Attribution API.

#### Overview

|  |  |
| --- | --- |
| February 2023 | After February 7, 2023, all requests made to the Apple Search Ads iAd Attribution API will return with a value of `"iad-attribution"` `=` `false`, or errors.  See [`requestAttributionDetails(_:)`](adclient/requestattributiondetails(_:).md). |
| June 2020 | Updated error responses. See [`ADClientError`](adclienterror-swift.struct.md) enumerations. |
| October 2019 | Added `iad-keyword-id` to the attribution dictionary. See Retrieve the Attribution Dictionary in [`Retrieve the Attribution Dictionary`](setting-up-apple-search-ads-attribution#Retrieve-the-Attribution-Dictionary.md). |

> ❗ **Important**:  The Apple Search Ads iAd Attribution API is deprecated. Use the [`AdServices`](https://developer.apple.com/documentation/AdServices) framework for current attribution integration with the [`Apple Search Ads`](https://developer.apple.com/documentation/apple_search_ads) Campaign Management API for devices using iOS 14.3 and later. Attribution isn’t available for downloads and redownloads from devices using iOS 14.2 or earlier.

## See Also

- [Setting Up Apple Search Ads Attribution](setting-up-apple-search-ads-attribution.md)
  Retrieve the attribution dictionary.
- [class ADClient](adclient.md)
  The parent class you use to request an attribution response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/iad-changelog)*