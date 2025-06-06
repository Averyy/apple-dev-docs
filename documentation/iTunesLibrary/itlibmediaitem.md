# ITLibMediaItem

**Framework**: iTunes Library  
**Kind**: class

This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibMediaItem
```

#### Overview

Like all media entities, each media item has a unique identifier and a set of properties.

## Topics

### Getting Media Item Info
- [var title: String](itlibmediaitem/title.md)
  The title of the media item.
- [var sortTitle: String?](itlibmediaitem/sorttitle.md)
  The title of the media item to use when sorting.
- [var artist: ITLibArtist?](itlibmediaitem/artist.md)
  Information about the artist that iTunes associates with the media item.
- [var composer: String](itlibmediaitem/composer.md)
  The name of the composer that iTunes associates with the media item.
- [var sortComposer: String?](itlibmediaitem/sortcomposer.md)
  The name to use when sorting by composer.
- [var rating: Int](itlibmediaitem/rating.md)
  The rating of the media item.
- [var isRatingComputed: Bool](itlibmediaitem/isratingcomputed.md)
  A Boolean value that indicates whether iTunes computes the media item’s rating from its album rating.
- [var startTime: Int](itlibmediaitem/starttime.md)
  If nonzero, the actual time playback of the media item starts instead of 0:00 (in milliseconds).
- [var stopTime: Int](itlibmediaitem/stoptime.md)
  If nonzero, the actual time playback of the media item stops versus the total time (in milliseconds).
- [var album: ITLibAlbum](itlibmediaitem/album.md)
  The album of the media item.
- [var genre: String](itlibmediaitem/genre.md)
  The genre of the media item, if any.
- [var kind: String?](itlibmediaitem/kind.md)
  The kind of media item file, such as an MPEG audio file.
- [var mediaKind: ITLibMediaItemMediaKind](itlibmediaitem/mediakind.md)
  The kind of media item.
- [var totalTime: Int](itlibmediaitem/totaltime.md)
  The length of the media item in milliseconds.
- [var trackNumber: Int](itlibmediaitem/tracknumber.md)
  The position of the media item within its album.
- [var category: String?](itlibmediaitem/category.md)
  The podcast category of the media item, if the media item is a podcast.
- [var description: String?](itlibmediaitem/description.md)
  The description of the media item, if it’s a podcast.
- [var contentRating: String?](itlibmediaitem/contentrating.md)
  The content rating of the media item.
- [var lyricsContentRating: ITLibMediaItemLyricsContentRating](itlibmediaitem/lyricscontentrating.md)
  The content rating of the media item’s lyrics.
- [var addedDate: Date?](itlibmediaitem/addeddate.md)
  The date and time that the user added the media item to the iTunes library.
- [var modifiedDate: Date?](itlibmediaitem/modifieddate.md)
  The date and time that iTunes last modified the media item.
- [var bitrate: Int](itlibmediaitem/bitrate.md)
  The bitrate of the media item in kbit/s.
- [var sampleRate: Int](itlibmediaitem/samplerate.md)
  The sample rate of the media item in samples-per-second.
- [var beatsPerMinute: Int](itlibmediaitem/beatsperminute.md)
  The beats-per-minute (BPM) of the media item.
- [var playCount: Int](itlibmediaitem/playcount.md)
  The number of times the user has played the media item.
- [var lastPlayedDate: Date?](itlibmediaitem/lastplayeddate.md)
  The date and time the user last played the media item, or `nil` if the user hasn’t played it.
- [var location: URL?](itlibmediaitem/location.md)
  The location of the media item on disk.
- [var locationType: ITLibMediaItemLocationType](itlibmediaitem/locationtype.md)
  The type of the media item with respect to its location.
- [var hasArtworkAvailable: Bool](itlibmediaitem/hasartworkavailable.md)
  A Boolean value that indicates whether the media item has artwork.
- [var artwork: ITLibArtwork?](itlibmediaitem/artwork.md)
  The artwork of the media item.
- [var comments: String?](itlibmediaitem/comments.md)
  Any comments that iTunes associates with the media item.
- [var isPurchased: Bool](itlibmediaitem/ispurchased.md)
  A Boolean value that indicates whether the user purchased the media item from the iTunes Store.
- [var isDRMProtected: Bool](itlibmediaitem/isdrmprotected.md)
  A Boolean value that indicates whether the media item has digital rights management (DRM) protection.
- [var isVideo: Bool](itlibmediaitem/isvideo.md)
  A Boolean value that indicates whether this media item is a video, such as a TV show, video podcast, or movie.
- [var videoInfo: ITLibMediaItemVideoInfo?](itlibmediaitem/videoinfo.md)
  Video information (such as width and height) about the media item, if it’s a video.
- [var releaseDate: Date?](itlibmediaitem/releasedate.md)
  The release date of the media item.
- [var year: Int](itlibmediaitem/year.md)
  The release year of the media item.
- [var skipCount: Int](itlibmediaitem/skipcount.md)
  The number of times that the user skipped the media item.
- [var skipDate: Date?](itlibmediaitem/skipdate.md)
  The date and time that the user last skipped the media item.
- [var voiceOverLanguage: String?](itlibmediaitem/voiceoverlanguage.md)
  The voice-over language of the media item.
- [var volumeAdjustment: Int](itlibmediaitem/volumeadjustment.md)
  The volume adjustment for the media item, if any.
- [var volumeNormalizationEnergy: Int](itlibmediaitem/volumenormalizationenergy.md)
  The volume normalization energy that iTunes applies to the media item to bring the average or peak amplitude to a target level.
- [var isUserDisabled: Bool](itlibmediaitem/isuserdisabled.md)
  A Boolean value that indicates whether the user disabled the media item.
- [var grouping: String?](itlibmediaitem/grouping.md)
  The grouping of the media item that the user specifies or that iTunes specifies in the file’s metadata.
- [var fileSize: UInt64](itlibmediaitem/filesize.md)
  The size in bytes of this media item on disk.
- [var isCloud: Bool](itlibmediaitem/iscloud.md)
  A Boolean value that indicates whether this media item is an iTunes Match or an iTunes in the Cloud item.
- [var playStatus: ITLibMediaItemPlayStatus](itlibmediaitem/playstatus.md)
  The play status for the media.
- [enum ITLibMediaItemMediaKind](itlibmediaitemmediakind.md)
  These constants specify the possible media kinds of a media item.
- [enum ITLibMediaItemLocationType](itlibmediaitemlocationtype.md)
  These constants specify the location type of a media item.
- [enum ITLibMediaItemLyricsContentRating](itlibmediaitemlyricscontentrating.md)
  These constants specify the possible ratings of media item lyrics.
- [enum ITLibMediaItemPlayStatus](itlibmediaitemplaystatus.md)
  These constants specify the play status of the media item.
### Media Item Properties
- [let ITLibMediaEntityPropertyPersistentID: String](itlibmediaentitypropertypersistentid.md)
  The unique identifier of the media entity.
- [let ITLibMediaItemPropertyAddedDate: String](itlibmediaitempropertyaddeddate.md)
  The date and time the user added the media item to the iTunes library.
- [let ITLibMediaItemPropertyAlbumArtist: String](itlibmediaitempropertyalbumartist.md)
  The name of the artist that iTunes associates with the media item’s album.
- [let ITLibMediaItemPropertyAlbumDiscCount: String](itlibmediaitempropertyalbumdisccount.md)
  The number of discs in the media item’s album.
- [let ITLibMediaItemPropertyAlbumDiscNumber: String](itlibmediaitempropertyalbumdiscnumber.md)
  The disc number in the media item’s album.
- [let ITLibMediaItemPropertyAlbumIsCompilation: String](itlibmediaitempropertyalbumiscompilation.md)
  This property indicates whether the album of the media item is a compilation.
- [let ITLibMediaItemPropertyAlbumIsGapless: String](itlibmediaitempropertyalbumisgapless.md)
  This property indicates whether the media item’s album is gapless.
- [let ITLibMediaItemPropertyAlbumRating: String](itlibmediaitempropertyalbumrating.md)
  The rating of the media item’s album.
- [let ITLibMediaItemPropertyAlbumRatingComputed: String](itlibmediaitempropertyalbumratingcomputed.md)
  This property indicates whether iTunes computes the rating of the media item’s album from the ratings of individual tracks in the album.
- [let ITLibMediaItemPropertyAlbumTitle: String](itlibmediaitempropertyalbumtitle.md)
  The title of the media item’s album.
- [let ITLibMediaItemPropertyAlbumTrackCount: String](itlibmediaitempropertyalbumtrackcount.md)
  The track count of the media item’s album.
- [let ITLibMediaItemPropertyArtistName: String](itlibmediaitempropertyartistname.md)
  The name of the artist that iTunes associates with the media item.
- [let ITLibMediaItemPropertyArtwork: String](itlibmediaitempropertyartwork.md)
  The artwork for the media item.
- [let ITLibMediaItemPropertyBeatsPerMinute: String](itlibmediaitempropertybeatsperminute.md)
  The beats-per-minute (BPM) of the media item.
- [let ITLibMediaItemPropertyBitRate: String](itlibmediaitempropertybitrate.md)
  The bitrate of the media item in kbit/s.
- [let ITLibMediaItemPropertyCategory: String](itlibmediaitempropertycategory.md)
  The podcast category of the media item, if the media item is a podcast.
- [let ITLibMediaItemPropertyComments: String](itlibmediaitempropertycomments.md)
  Any comments that iTunes associates with the media item.
- [let ITLibMediaItemPropertyComposer: String](itlibmediaitempropertycomposer.md)
  The name of the composer that iTunes associates with the media item.
- [let ITLibMediaItemPropertyContentRating: String](itlibmediaitempropertycontentrating.md)
  The extended content rating of the media item.
- [let ITLibMediaItemPropertyDescription: String](itlibmediaitempropertydescription.md)
  A podcast description of the media item, if the media item is a podcast.
- [let ITLibMediaItemPropertyFileSize: String](itlibmediaitempropertyfilesize.md)
  The size in bytes of the media item on disk.
- [let ITLibMediaItemPropertyGenre: String](itlibmediaitempropertygenre.md)
  The genre that iTunes associates with the media item.
- [let ITLibMediaItemPropertyGrouping: String](itlibmediaitempropertygrouping.md)
  The grouping of the media item.
- [let ITLibMediaItemPropertyHasArtwork: String](itlibmediaitempropertyhasartwork.md)
  This property indicates whether the media item has artwork.
- [let ITLibMediaItemPropertyIsDRMProtected: String](itlibmediaitempropertyisdrmprotected.md)
  This property indicates whether the media item has digital rights management (DRM) protection.
- [let ITLibMediaItemPropertyIsPurchased: String](itlibmediaitempropertyispurchased.md)
  This property indicates whether the media item is a purchased media item.
- [let ITLibMediaItemPropertyIsUserDisabled: String](itlibmediaitempropertyisuserdisabled.md)
  This property indicates whether the user disabled the media item.
- [let ITLibMediaItemPropertyIsVideo: String](itlibmediaitempropertyisvideo.md)
  This property indicates whether the media item is a video media item, such as a video podcast or movie.
- [let ITLibMediaItemPropertyKind: String](itlibmediaitempropertykind.md)
  The kind of media item file, such as an MPEG audio file.
- [let ITLibMediaItemPropertyLastPlayDate: String](itlibmediaitempropertylastplaydate.md)
  The date and time the user last played the media item in iTunes, or `nil` if the user hasn’t played the media item.
- [let ITLibMediaItemPropertyLocation: String](itlibmediaitempropertylocation.md)
  The location of the media item on disk.
- [let ITLibMediaItemPropertyLocationType: String](itlibmediaitempropertylocationtype.md)
  The type of the media item with respect to its location.
- [let ITLibMediaItemPropertyLyricsContentRating: String](itlibmediaitempropertylyricscontentrating.md)
  The content rating of the media item’s lyrics.
- [let ITLibMediaItemPropertyMediaKind: String](itlibmediaitempropertymediakind.md)
  The media kind of the media item.
- [let ITLibMediaItemPropertyModifiedDate: String](itlibmediaitempropertymodifieddate.md)
  The date and time that iTunes last modified the media item.
- [let ITLibMediaItemPropertyMovementCount: String](itlibmediaitempropertymovementcount.md)
- [let ITLibMediaItemPropertyMovementName: String](itlibmediaitempropertymovementname.md)
- [let ITLibMediaItemPropertyMovementNumber: String](itlibmediaitempropertymovementnumber.md)
- [let ITLibMediaItemPropertyPlayCount: String](itlibmediaitempropertyplaycount.md)
  The number of times the user has played the media item in iTunes.
- [let ITLibMediaItemPropertyPlayStatus: String](itlibmediaitempropertyplaystatus.md)
  The play status of the media item.
- [let ITLibMediaItemPropertyRating: String](itlibmediaitempropertyrating.md)
  The rating of the media item.
- [let ITLibMediaItemPropertyRatingComputed: String](itlibmediaitempropertyratingcomputed.md)
  This property indicates whether iTunes computes the media item’s rating.
- [let ITLibMediaItemPropertyReleaseDate: String](itlibmediaitempropertyreleasedate.md)
  The release date of the media item.
- [let ITLibMediaItemPropertySampleRate: String](itlibmediaitempropertysamplerate.md)
  The sample rate of the media item in samples-per-second.
- [let ITLibMediaItemPropertySize: String](itlibmediaitempropertysize.md)
  The size in bytes of the media item on disk.
- [let ITLibMediaItemPropertySkipDate: String](itlibmediaitempropertyskipdate.md)
  The date and time that the user last skipped the media item.
- [let ITLibMediaItemPropertySortAlbumArtist: String](itlibmediaitempropertysortalbumartist.md)
  The name of the artist that iTunes associates with the media item’s album, for use when sorting.
- [let ITLibMediaItemPropertySortAlbumTitle: String](itlibmediaitempropertysortalbumtitle.md)
  The title of the media item’s album, for use when sorting.
- [let ITLibMediaItemPropertySortArtistName: String](itlibmediaitempropertysortartistname.md)
  The name of the media item’s artist, for use when sorting.
- [let ITLibMediaItemPropertySortComposer: String](itlibmediaitempropertysortcomposer.md)
  The name of the composer that iTunes associates with the media item, for use when sorting.
- [let ITLibMediaItemPropertySortTitle: String](itlibmediaitempropertysorttitle.md)
  The title of the media item to use when sorting.
- [let ITLibMediaItemPropertyStartTime: String](itlibmediaitempropertystarttime.md)
  If nonzero, the actual time that playback for the media item starts instead of 0:00 (in milliseconds).
- [let ITLibMediaItemPropertyStopTime: String](itlibmediaitempropertystoptime.md)
  If nonzero, the actual time that playback for the media item stops versus the total time (in milliseconds).
- [let ITLibMediaItemPropertyTitle: String](itlibmediaitempropertytitle.md)
  The title of the media item.
- [let ITLibMediaItemPropertyTotalTime: String](itlibmediaitempropertytotaltime.md)
  The length of the media item in milliseconds.
- [let ITLibMediaItemPropertyTrackNumber: String](itlibmediaitempropertytracknumber.md)
  The numerical position of the media item within its album.
- [let ITLibMediaItemPropertyUserSkipCount: String](itlibmediaitempropertyuserskipcount.md)
  The number of times that the user skipped the media item.
- [let ITLibMediaItemPropertyVideoEpisode: String](itlibmediaitempropertyvideoepisode.md)
  The name of the episode, if the media item is an episode of a TV series.
- [let ITLibMediaItemPropertyVideoEpisodeOrder: String](itlibmediaitempropertyvideoepisodeorder.md)
  The order of the episode, if the media item is an episode of a TV series.
- [let ITLibMediaItemPropertyVideoHeight: String](itlibmediaitempropertyvideoheight.md)
  The height in pixels, if the media item is a video.
- [let ITLibMediaItemPropertyVideoIsHD: String](itlibmediaitempropertyvideoishd.md)
  This property indicates whether a video media item is high-definition.
- [let ITLibMediaItemPropertyVideoSeason: String](itlibmediaitempropertyvideoseason.md)
  The corresponding TV season, if the media item is an episode of a TV series.
- [let ITLibMediaItemPropertyVideoSeries: String](itlibmediaitempropertyvideoseries.md)
  The name of the corresponding TV series, if the media item is an episode in a TV series.
- [let ITLibMediaItemPropertyVideoSortSeries: String](itlibmediaitempropertyvideosortseries.md)
  The sorting name of the corresponding TV series, if the media item is an episode in a TV series.
- [let ITLibMediaItemPropertyVideoWidth: String](itlibmediaitempropertyvideowidth.md)
  The width in pixels, if the media item is a video.
- [let ITLibMediaItemPropertyVoiceOverLanguage: String](itlibmediaitempropertyvoiceoverlanguage.md)
  The voice-over language of the media item.
- [let ITLibMediaItemPropertyVolumeAdjustment: String](itlibmediaitempropertyvolumeadjustment.md)
  The volume adjustment for the media item, if any.
- [let ITLibMediaItemPropertyVolumeNormalizationEnergy: String](itlibmediaitempropertyvolumenormalizationenergy.md)
  The volume normalization energy that iTunes applies to the media item to bring the average or peak amplitude to a target level.
- [let ITLibMediaItemPropertyWork: String](itlibmediaitempropertywork.md)
- [let ITLibMediaItemPropertyYear: String](itlibmediaitempropertyyear.md)
  The release year of the media item.
### Deprecated
- [var fileType: Int](itlibmediaitem/filetype.md)
  The file type of the media item.
- [var size: Int](itlibmediaitem/size.md)
  The size in bytes of the media item on disk.
- [let ITLibMediaItemPropertyFileType: String](itlibmediaitempropertyfiletype.md)
  The file type of the media item.

## Relationships

### Inherits From
- [ITLibMediaEntity](itlibmediaentity.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ITLibMediaEntity](itlibmediaentity.md)
  This class describes a media entity, which can be a media item, such as an audio track.
- [class ITLibArtist](itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibArtwork](itlibartwork.md)
  This class represents the artwork for a media item.
- [class ITLibMediaItemVideoInfo](itlibmediaitemvideoinfo.md)
  This class encapsulates the video information of a video media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitem)*