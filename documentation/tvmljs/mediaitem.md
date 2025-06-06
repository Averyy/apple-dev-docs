# MediaItem

**Framework**: TVMLKit JS  
**Kind**: cl

A single audio or video item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
interface MediaItem
```

#### Overview

In order to play audio or video, at a minimum, there must be a [`Player`](player.md) object that contains a single [`Playlist`](playlist.md) object which contains a single `MediaItem` object.

## Topics

### Creating Media Items
- [MediaItem](mediaitem/1627412-mediaitem.md)
  Creates a new `MediaItem` object from the information stored in the URL location.
### Rating Media Content
- [contentRatingDomain](mediaitem/1627422-contentratingdomain.md)
  The domain that the rating applies to.
- [contentRatingRanking](mediaitem/1627366-contentratingranking.md)
  The rating for a video item.
- [isExplicit](mediaitem/1627358-isexplicit.md)
  A Boolean value indicating whether the item has explicit lyrics.
### Identifying Media Items
- [artworkImageURL](mediaitem/1627319-artworkimageurl.md)
  The URL path to the artwork that accompanies the media item.
- [description](mediaitem/1627441-description.md)
  The description for a media item.
- [subtitle](mediaitem/1627329-subtitle.md)
  The subtitle for a the media item.
- [title](mediaitem/1627381-title.md)
  The title of the media item.
- [type](mediaitem/1627315-type.md)
  The type of media item.
- [url](mediaitem/1627401-url.md)
  The URL path to the media item.
### Setting Timing Options
- [highlightGroups](mediaitem/1627413-highlightgroups.md)
  An array of highlight groups, with each group containing a list of highlights.
- [interstitials](mediaitem/1627341-interstitials.md)
  An array of `interstitial` objects.
- [resumeTime](mediaitem/1627400-resumetime.md)
  The number of seconds from the beginning of the item at which the item begins playing.
### Supporting FairPlay Streaming
- [loadAssetID](mediaitem/1627392-loadassetid.md)
  A callback function used to load the asset identifier for an item.
- [loadCertificate](mediaitem/1627435-loadcertificate.md)
  A callback function used to load the security certificate for an item.
- [loadKey](mediaitem/1627379-loadkey.md)
  A callback function used to load the security key for an item.

## See Also

- [Playing Media in a Client-Server App](playing_media_in_a_client-server_app.md)
  Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [Player](player.md)
  A media player that displays the UI for playing video and audio in an Apple TV client-server app.
- [Playlist](playlist.md)
  An array of media items to be played in an Apple TV client-server app.
- [Slideshow](slideshow.md)
  An object used to display images on Apple TV in a slideshow format.
- [Browser](browser.md)
  An object used to configure and present a browsable full screen view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/mediaitem)*