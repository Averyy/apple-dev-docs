# Creating a subscription

**Framework**: Swift Playgrounds

Create a machine-readable summary of a set of playground books to make them available for others to download.

#### Overview

If you’re writing episodic content in your Swift Playgrounds learning material, or want to space out the releases of your lessons over time, you can build a subscription that guides people through your lessons one by one. To publish your playgrounds, you create and host the subscription data online so people can subscribe to them in Swift Playgrounds.

Swift Playgrounds subscriptions, like podcasts, are a sequence of episodic content arranged in an order that builds knowledge while allowing more advanced learners to skip content. Subscriptions exist on the internet as feeds — downloadable lists of items that apps and websites can deal with. You publish a set of playgrounds as a feed that the Swift Playgrounds app can download, process, and display.

Feeds in Swift Playgrounds are structured as JSON, which many apps and websites use to communicate and share information. It consists primarily of lists, definitions, and raw values like strings and numbers. You use it to build up a feed for your subscription. A simple — yet complete — JSON document looks like this:

```swift
{
    "bookTitle": "Whimsical Swift Syntax",
    "publishDate": 2018,
    "simpleList": ["one", 1, "two", 2]
}
```

The example document isn’t detailed enough to be a real feed for a playground subscription, but it shows the kind of information a feed contains. Although the JSON documents that apps use are typically longer, they follow the same rules of quoting and nesting. For more information about JSON, see [`ECMA-404: The JSON Data Interchange Format`](https://developer.apple.comhttps://www.ecma-international.org/publications/standards/Ecma-404.htm).

Not all JSON documents are feeds. Feeds of JSON documents are informally defined by two characteristics:

- They consist of metadata, like “What’s the name of this feed?”, and a primary list of homogeneous data items.
- They link to, but don’t contain, some media of interest, such as a link to an audio file, a blog post, or a playground.

The feed format used by Swift Playgrounds has these two characteristics:

- Feeds contain some details (metadata) used to name, describe, and identify the subscription.
- Feeds contain a link to each individual playground book in a subscription.

##### Create a Subscription Feed

Create the feed for a subscription by defining top-level metadata about the subscription. The top level of the JSON object that represents the feed must include following keys:

##### Add Documents to the Feed

For each book in your subscription, include an object with the following fields in your feed’s `documents` array:

##### Add Metadata to the Feed Documents

Store additional information and metadata about your feed in the format described below. This information is displayed alongside the book’s preview images to provide details about the book — such as available localizations — before a user downloads it.

For more information, see [`Localizing a Subscription Feed`](localizing-a-subscription-feed.md).

##### Update a Subscription By Adding Items to Its Feed

Subscriptions are expected to be updated over time. The same expectation applies to the feeds distributing your playground subscriptions. To add, remove, or update a subscription, first create a new or updated playground book. Then adjust the JSON feed so it corresponds to the updates you’ve just made.

When you update a playground book, be sure to update the JSON feed that links to the book at the same time. If the feed is out of date, there may be a mismatch between the preview information contained in the feed and the content in the playground books the feed links to.

The example below shows a feed with two playground books that make up the whole series.

```swift
{
    "title": "Whimsical Swift Syntax",
    "subtitle": "A Collection of Swift Lessons",
    "publisherName": "Company Name Inc.",
    "feedIdentifier": "com.example.whimsicalswift",
    "contactURL": "https://support.example.com",
    "formatVersion": "1.0",
    "documents": [
        {
            "title": "The Key Path Not Taken",
            "overviewSubtitle": "Dynamically Choosing Among Key Paths",
            "detailSubtitle": "Because key paths in Swift are applied at runtime, their behavior is dynamic.",
            "description": "Learn to compare key paths and pick the right one.",
            "contentIdentifier": "com.example.whimsicalswift.keypaths",
            "contentVersion": "1.0",
            "url": "keypaths/keypaths.playgroundbook.zip",
            "publishedDate": "2017-11-13T21:13:57+00:00",
            "lastUpdatedDate": "2017-11-13T21:13:57+00:00",
            "thumbnailURL": "keypaths/thumbnail.png",
            "bannerImageURL": "keypaths/banner.png",
            "additionalInformation": [
                {
                    "name": "Languages",
                    "value": "English"
                }
            ],
            "previewImageURLs": [
                "keypaths/preview-1.png"
            ]
        },
        {
            "title": "Structer Things",
            "overviewSubtitle": "Understand Structures by Comparing Them with Classes",
            "detailSubtitle": "Choose between using a structure or a class to model data.",
            "description": "Learn about value semantics and reference semantics.",
            "contentIdentifier": "com.example.whimsicalswift.structures-and-classes",
            "contentVersion": "1.0",
            "url": "structures-and-classes/structures-and-classes.playgroundbook.zip",
            "publishedDate": "2017-11-13T21:13:57+00:00",
            "lastUpdatedDate": "2017-11-13T21:13:57+00:00",
            "thumbnailURL": "structures-and-classes/thumbnail.png",
            "bannerImageURL": "structures-and-classes/banner.png",
            "additionalInformation": [
                {
                    "name": "Languages",
                    "value": "English"
                }
            ],
            "previewImageURLs": [
                "structures-and-classes/preview-1.png"
            ]
        }
    ]
}

```

## See Also

- [Localizing a Subscription Feed](localizing-a-subscription-feed.md)
  Provide multiple localizations of a subscription’s content in a single feed.
- [Publishing a Subscription](publishing-a-subscription.md)
  Make the playground books in a series available online for download and subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/creating-a-subscription)*