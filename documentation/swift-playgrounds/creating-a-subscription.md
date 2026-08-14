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

- **`formatVersion`**: The version of the feed format to which this feed conforms. The current format version is `"1.2"`.
- **`title`**: The name of your subscription.
- **`publisherName`**: The organization publishing the subscription; often an institution or company name.
- **`feedIdentifier`**: A reverse-DNS string for the domain hosting this feed.
- **`contactURL`**: The contact URL you use to get information about, and report problems with, the feed.
- **`documents`**: An array of objects representing the playground books in your feed. For details about the format for the objects in this array, see doc:creating-a-subscription#Add-Documents-to-the-Feed.

##### Add Documents to the Feed

For each book in your subscription, include an object with the following fields in your feed’s `documents` array:

- **`title`**: The name of the playground book.
- **`overviewSubtitle`**: The subtitle of the playground book displayed in overviews. Expand on the name of the book to provide additional context.
- **`detailSubtitle`**: **Optional.** The subtitle of the playground book displayed in detail views. Expand further on the name of the book to provide additional context.
- **`description`**: A description that appears in detail views before a book in the subscription is opened.
- **`difficultyLevel`**: **Optional.** The difficulty level of the material taught in the book. The level must be `"beginner"`, `"intermediate"`, `"expert"`, or `"advanced"`.
- **`attributes`**: **Optional.**  An array of attributes that describe the theme of the content in a playground book. The array can contain up to six values. Values in the array must be one of the following attributes: `"short"`, `"medium"`, `"long"`, `"algorithmic"`, `"appBuilding"`, `"appLike"`, `"art"`, `"astronomy"`, `"audioExperience"`, `"augmentedReality"`, `"biology"`, `"chemistry"`, `"codingBasics"`, `"cryptography"`, `"curriculumBased"`, `"databases"`, `"dataStructuresAndAlgorithms"`, `"designOriented"`, `"economics"`, `"gameBuilding"`, `"gameLike"`, `"geometry"`, `"graphical"`, `"history"`, `"languageArts"`, `"music"`, `"networking"`, `"objectOrientedProgramming"`, `"physics"`, `"premadeForTinkerers"`, `"projectBased"`, `"puzzleSolving"`, `"simulation"`, `"startingPoint"`, `"storyBased"`, `"usesAccessory"`, `"usesCamera"`, `"usesMicrophone"`, `"usesMotion"`, `"usesSoundPredominantly"`.
- **`authorChosenUpNext`**: **Optional.** The `contentIdentifier` key for a recommended document to follow the current document in a learner’s progression.
- **`contentIdentifier`**: A reverse-DNS identifier unique to the book. The identifier must match the `ContentIdentifier` key in the book’s manifest and start with the `feedIdentifier` key of the feed that contains this book. For more information about the `ContentIdentifier` key, see [`Determine Book-Level Information`](structuring-content-for-swift-playgrounds#Determine-Book-Level-Information.md).
- **`contentVersion`**: A version number you increment when you update the book. The version must match the `ContentVersion` key in the book’s manifest. For more information about the `ContentVersion` key, see [`Determine Book-Level Information`](structuring-content-for-swift-playgrounds#Determine-Book-Level-Information.md).
- **`requiredCapabilities`**: **Optional.** An array of device-related features that the book requires to run. A feature is any [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequireddevicecapabilities) value.
- **`supportedDevices`**: **Optional.** An array of strings that identifies the set of devices the book can run on. The possible values are `"iPad"` and `"Mac"`.
- **`sha512`**: **Optional.** The SHA-512 hash of the zipped version of the book. Required when the playground book is hosted on a domain other than the feed.
- **`url`**: A link to your zipped copy of the book’s `.playgroundbook` file.
- **`publishedDate`**: The ISO 8601-formatted date when you first published the book.
- **`lastUpdatedDate`**: The ISO 8601-formatted date when you last updated the book.
- **`thumbnailURL`**: A link to a picture of the cover of the book. Thumbnail images must be 902 x 678 pixels.
- **`bannerImageURL`**: A link to the banner image used to display the book. Banner images must be 1080 x 400 pixels.
- **`additionalInformation`**: An array of objects you use to supply metadata. The format for the objects in this array is described in doc:creating-a-subscription#Add-Metadata-to-the-Feed-Documents.
- **`previewImageURLs`**: An array of URLs to images that highlight parts of the book. Preview images must be 800 x 600 pixels.

##### Add Metadata to the Feed Documents

Store additional information and metadata about your feed in the format described below. This information is displayed alongside the book’s preview images to provide details about the book — such as available localizations — before a user downloads it.

- **`name`**: A metadata key name.
- **`value`**: A metadata key value.
- **`type`**: **Optional.** The type of the value specified by the value field. The type must be `"string"` or `"date"`. The default value is `"string"`. Dates must be ISO 8601-formatted date strings.

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