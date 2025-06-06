# Localizing a Subscription Feed

**Framework**: Swift Playgrounds

Provide multiple localizations of a subscription’s content in a single feed.

#### Overview

You can provide localizations of your subscription content by linking to a supplemental JSON object that maps locale IDs to locale-specific feeds.

##### Create the Localization Mapping in Json

Each localization of your subscription’s content requires its own entry in the supplemental JSON object. You create the mapping from a locale ID—a standard format described in [`Locale IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15-SW9)—to the localized feed URL by pairing the two for that locale. You use the locale ID as the key and the localized feed URL as the value for each key-value pair in the JSON object.

For example, you can supply the following locale JSON to support a feed that’s localized to contain English and French versions of a subscription’s content:

```javascript
{
    "en": "en-feed.json",
    "fr": "fr-feed.json"
}
```

The locale ID for the French localization is `fr`, and `fr-feed.json` contains French metadata and the URL for the localized French playground books in the subscription.

##### Share the Localized Json Objects Url

Unlike feeds that aren’t localized, localized feeds download the supplemental JSON object as an extra step to determine locale information before downloading your feed’s content. As a result, you need to use the URL for the supplemental JSON object when sharing your subscription.

![A diagram showing the relationship between the feed URL, the feed JSON, and the intermediate locale JSON that’s only required for localized feeds.](https://docs-assets.developer.apple.com/published/3538c391b8329912ee4ebe05754c6d6f/localizing-a-subscription-feed-1%402x.png)

## See Also

- [Creating a subscription](creating-a-subscription.md)
  Create a machine-readable summary of a set of playground books to make them available for others to download.
- [Publishing a Subscription](publishing-a-subscription.md)
  Make the playground books in a series available online for download and subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/localizing-a-subscription-feed)*