# Apple TV Feed

**Framework**: Apple TV Feed  
**Kind**: module

Access the content of the Apple TV Catalog in bulk.

**Availability**:
- AppleTVFeed 1.0+

#### Overview

Apple TV Feed contains the catalog content of Apple TV products in bulk for consumption as feed exports. These bulk exports are appropriate for offline use cases, complementing Apple Media API, which is best for online use. Apple TV Feed includes content metadata for movies, TV shows, TV show seasons, TV show episodes, and sporting events — and it fully refreshes every 24 hours. You access Apple TV Feed using the Apple Media Feed API to [`Requesting a feed export`](requesting-a-feed-export.md) of a data set. To get the information required to authorize your API requests, you need to be a member of the [`Apple Services Performance Partners Program`](https://developer.apple.comhttps://partners.marketingtools.apple.com).

With access to the raw data and the information in this documentation, you can use Apple TV Feed in many ways. For example, if you want to build a discovery engine for Apple TV, you can examine the data and determine endpoint requests to serve such an engine.

Apple TV Feed uses the Parquet format, which is an open source columnar storage file format that optimizes the storage and processing of large datasets. The Parquet format improves query performance and reduces storage costs in scenarios where you need to read or process data selectively. It uses columns and stores the values of each column together, which allows efficient compression and encoding techniques that you can apply specifically to each column. Many large-scale data-processing frameworks, like Hadoop and Spark, use this format.

> **Note**: Although the feed is in Parquet format, this documentation provides data examples in JSON format for illustrative purposes.

#### Use Sample Scripts

The process to access Apple TV Feed is largely the same as for Apple Music Feed. In the [`music-feed-examples`](https://developer.apple.comhttps://github.com/apple/music-feed-examples) public GitHub repository, you can find sample Java and Python scripts that perform the following steps:

- Generate a developer token.
- Use the token to request metadata for the latest feed export for a specific data set.
- Use the token to request links to parts of the data for a feed export.
- Download the feed data to a specified output directory.
- Load the data files in Parquet and run a simple query.

## Topics

### Essentials
- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to the Apple Media Feed API.
- [Requesting a feed export](requesting-a-feed-export.md)
  Create requests for Apple TV Catalog metadata.
- [Interpreting responses](interpreting-responses.md)
  Learn about responses from the Apple Media Feed API to your Apple TV Feed requests.
### Objects
- [object Movie](movie.md)
  The data structure that represents a movie resource.
- [object TvEpisode](tvepisode.md)
  The data structure that represents a TV episode resource.
- [object TvSeason](tvseason.md)
  The data structure that represents a TV season resource.
- [object TvShow](tvshow.md)
  The data structure that represents a TV show resource.
- [object SportingEvent](sportingevent.md)
  The data structure that represents a sporting event resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed)*