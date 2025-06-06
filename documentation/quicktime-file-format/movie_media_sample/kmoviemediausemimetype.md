# kMovieMediaUseMIMEType

**Framework**: QuickTime File Format  
**Kind**: property

Text (not a C string or a pascal string) that indicates the MIME type of the movie import component that should be used to instantiate this media.

#### Overview

This is useful in cases where the data reference may not contain MIME type information. If this atom is not present, the MIME type of the data reference as determined at instantiation time is used. This atom is intended to allow content creators a method for working around MIME type binding problems. It should not typically be required, and should not be included in movie media samples by default.

## See Also

- [kMovieMediaDataReference](movie_media_sample/kmoviemediadatareference.md)
  A data reference type and a data reference.
- [kMovieMediaDefaultDataReferenceID](movie_media_sample/kmoviemediadefaultdatareferenceid.md)
  An identifier for the data reference to use when instantiating the embedded movie for this sample.
- [kMovieMediaAutoPlay](movie_media_sample/kmoviemediaautoplay.md)
  A Boolean that indicates whether or not the embedded movie starts playing immediately after  instantiation.
- [kMovieMediaLoop](movie_media_sample/kmoviemedialoop.md)
  An 8-byte unsigned integer that indicates how the embedded movie should loop.
- [kMovieMediaTitle](movie_media_sample/kmoviemediatitle.md)
  Currently unused.
- [kMovieMediaAltText](movie_media_sample/kmoviemediaalttext.md)
  Text (not a C string or a pascal string) that is displayed to the user when the embedded movie is being instantiated or if the embedded movie cannot be instantiated.
- [kMovieMediaClipBegin](movie_media_sample/kmoviemediaclipbegin.md)
  A record that indicates the time of the embedded movie to use.
- [kMovieMediaClipDuration](movie_media_sample/kmoviemediaclipduration.md)
  A record that indicates the duration of the embedded movie to use.
- [kMovieMediaEnableFrameStepping](movie_media_sample/kmoviemediaenableframestepping.md)
  A Boolean that indicates whether the embedded movie should be considered when performing step operations.
- [kMovieMediaBackgroundColor](movie_media_sample/kmoviemediabackgroundcolor.md)
  A color that is used for filling the background when the movie is being instantiated or when it fails to instantiate.
- [kMovieMediaRegionAtom](movie_media_sample/kmoviemediaregionatom.md)
  A number of atoms, which describe how the Movie Media Handler should resize the embedded movie.
- [kMovieMediaRectangleAtom](movie_media_sample/kmoviemediarectangleatom.md)
  Four atoms that define a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_media_sample/kmoviemediausemimetype)*