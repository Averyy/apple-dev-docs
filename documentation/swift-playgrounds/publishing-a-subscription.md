# Publishing a Subscription

**Framework**: Swift Playgrounds

Make the playground books in a series available online for download and subscription.

#### Overview

You publish playgrounds by packaging one or more of them into a subscription feed, then uploading the files for the subscription—the playground books, images, metadata, and subscription feed—to a compatible web host. Once the subscription is online, you can make it available for people to download on their iPads by using a web page or by entering a URL directly in Swift Playgrounds.

##### Check Your Web Host for Compatibility

Uploading files usually involves a , which is a service provider that specializes in making data available online. Almost any web host meets the requirements for putting a playground subscription online. However, the host must support TLS 1.3 encryption.

> **Note**: Popular sites such as GitHub via [`GitHub Pages`](https://developer.apple.comhttps://pages.github.com/), Squarespace, and others offer the required features for hosting subscriptions. Hosts have their own terms and conditions, however, and may charge fees for high download volumes. Make sure you’re aware of and in agreement with these rules before making your feed available publicly.

Popular sites such as GitHub via [`GitHub Pages`](https://developer.apple.comhttps://pages.github.com/), Squarespace, and others offer the required features for hosting subscriptions. Hosts have their own terms and conditions, however, and may charge fees for high download volumes. Make sure you’re aware of and in agreement with these rules before making your feed available publicly.

##### Upload Your Subscriptions Files

You store a subscription’s playgrounds (zipped `.playgroundbook` files) as well as its feed (a JSON file) and supporting resources by uploading them to a web host. Be sure to note the URLs that your web host uses to store each file; you’ll use these to fill in the parts of the feed format described in Subscription Feed Format with URLs customized to your specific web host and your playground subscription. These URLs must match the URLs in the feed JSON.

Some web hosts have a file upload facility that lets you drag and drop a hierarchy of directories and files from your local filesystem. When writing the JSON for a feed, it can be helpful to compare the structure of your feed’s files with the structure of the URLs in the feed.

![A diagram that shows a directory layout of all of the resources—such as images and zipped books—used by the example feed JSON.](https://docs-assets.developer.apple.com/published/fcd45ad03e3672c55e2a3e1b982d2445/publishing-subscriptions-1%402x.png)

##### Publish Your Subscription on the Web

If you have an existing personal, business, or school website, you can add a page to that site linking visitors to your Swift Playgrounds subscriptions.

To add a link to your feed, you’ll need the following information:

- The Swift Playgrounds universal link prefix: `https://developer.apple.com/ul/sp0?url=`.
- The URL for your subscription’s JSON feed; for example: `https://example.com/whimsical-swift/feed.json`.

Combine the two URLs to form a link on your site. The example below shows an HTML link surrounded by a descriptive sentence:

```other
Check out my
<a href="https://developer.apple.com/ul/sp0?url=https://example.com/whimsical-swift/feed.json">
</a>
that whimsically highlights interesting facets of Swift!
```

##### Publish Your Subscription Manually

If you want to distribute your playground in a classroom or workshop environment rather than through a web page, you can instruct learners to enter the URL of your feed manually. In Swift Playgrounds, tap the Add Subscription button and enter the URL for your feed. Manually entered URLs must not include the Swift Playgrounds subscriptions universal link prefix. Instead, use the raw URL from your web host for the feed.

## See Also

- [Creating a subscription](creating-a-subscription.md)
  Create a machine-readable summary of a set of playground books to make them available for others to download.
- [Localizing a Subscription Feed](localizing-a-subscription-feed.md)
  Provide multiple localizations of a subscription’s content in a single feed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/publishing-a-subscription)*