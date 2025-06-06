# Creative Sets

**Framework**: Apple Search Ads

Creative Sets is deprecated.

#### Overview

> ❗ **Important**:  As of January 2022, [`Custom Product Pages`](custom-product-pages.md) replaces Creative Sets functionality. The Apple Search Ads API no longer supports Creative Sets and `AdGroupCreativeSets`. Creative Sets APIs return `200OK` responses with an invalid state. Your Creative Sets data remains available through `Get Creative Set-Level Reports` and through the `AdServices` attribution framework for devices running below iOS 15.2. See [`attributionToken()`](https://developer.apple.com/documentation/AdServices/AAAttribution/attributionToken()).

 As of January 2022, [`Custom Product Pages`](custom-product-pages.md) replaces Creative Sets functionality. The Apple Search Ads API no longer supports Creative Sets and `AdGroupCreativeSets`. Creative Sets APIs return `200OK` responses with an invalid state. Your Creative Sets data remains available through `Get Creative Set-Level Reports` and through the `AdServices` attribution framework for devices running below iOS 15.2. See [`attributionToken()`](https://developer.apple.com/documentation/AdServices/AAAttribution/attributionToken()).

 are collections of app screenshots and [`app previews`](https://developer.apple.comhttps://developer.apple.com/app-store/app-previews/) that you  upload to [`App Store Connect`](https://developer.apple.comhttps://developer.apple.com/app-store-connect/). After setting up your app and assets in App Store Connect, you can create and link Creative Sets to ad groups through the API or through the Apple Search Ads UI.

Creative Sets enable you to test ad variations in ad groups and optimize for different keywords, devices, and display sizes.

##### Upload Assets to App Store Connect

Using ceatives in the Apple Search Ads Campaign Management API requires you to upload your app assets to [`App Store Connect`](https://developer.apple.comhttps://developer.apple.com/app-store-connect/). For the API to return asset data, you must meet two important requirements:

- Your app needs a  minimum number of assets. See the `Asset` object, `MediaAppPreviewOrScreenshots`, and `MediaAppPreviewOrScreenshotsDetail` for app asset descriptions.
- The supported language for your campaign must be the same as the one for the [`App Store Connect`](https://developer.apple.comhttps://developer.apple.com/app-store-connect/) territory of your app.

##### Create and Work with Creatives

After you upload your app assets to [`App Store Connect`](https://developer.apple.comhttps://developer.apple.com/app-store-connect/), use `Get App Language, Device Sizes, and Asset Details` to identify supported languages for your app and countries or regions. Then use `Create Ad Group Creative Sets`. You can reassign Creative Sets to another ad group using `Assign Creative Sets to an Ad Group`.

Additional features include:

- Use [`Get App Preview Device Sizes`](get-app-preview-device-sizes.md) to identify available assets for your app and language, grouped by device.
- Use  `Find Ad Group Creative Sets`, `Get a Creative Set Ad Variation`, and `Find Creative Sets` as necessary to locate Creative Sets and ad variations.
- Use `Update Creative Sets` as necessary to make changes to your Creative Set names.
- Change the Creative Set status. See `Update Ad Group Creative Sets`.
- Use `Delete Ad Group Creative Sets` as necessary to remove Creative Sets from an ad group.
- Measure campaign performance using metrics that return through `Get Creative Set-Level Reports`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/creative-sets)*