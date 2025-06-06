# Streaming media

**Framework**: QuickTime File Format

Store streaming data in a streaming media track for QuickTime movies.

#### Overview

QuickTime movies store streaming data in a streaming media track. This media has a media type of `'strm'`.

#### Streaming Media Sample Description

The streaming media sample description contains information that defines how to interpret streaming media data. This sample description is based on the standard sample description header, as described in [`Sample table atom ('stbl')`](sample_table_atom.md).

The streaming media sample description is documented in the QuickTime header file `QTSMovie.h`, as follows:

```c
struct QTSSampleDescription {
    long                            descSize;
    long                            dataFormat;
    long                            resvd1;     /* set to 0*/
    short                           resvd2;     /* set to 0*/
    short                           dataRefIndex;
    UInt32                          version;
    UInt32                          resvd3;     /* set to 0*/
    SInt32                          flags;
                                                /* qt atoms follow:*/
                                    /* long size, long type, some  data*/
                                                /* repeat as necessary*/
};
typedef struct QTSSampleDescription     QTSSampleDescription;
```

The sample format depends on the `dataFormat` field of the `QTSSampleDescription`. The `dataFormat` field can be any value you specify. The currently defined values are `'rtsp'` and `'sdp '`.

If `'rtsp'`, the sample can be just an rtsp URL. It can also be any value that you can put in a `.rtsp` file, as defined at

[`http://streaming.apple.com/qtstreaming/documentation/userdocs/rtsptags.htm`](https://developer.apple.comhttp://streaming.apple.com/qtstreaming/documentation/userdocs/rtsptags.htm)

If `'sdp '`, then the sample is an SDP file. This would be used to receive a multicast broadcast.

## See Also

- [Modifier tracks](modifier_tracks.md)
  Create dynamic movies with modifier tracks that send data to another track.
- [Creating movies with modifier tracks](creating_movies_with_modifier_tracks.md)
  Send data to another media handler instead of presenting media directly.
- [Track references](track_references.md)
  Relate a movie’s tracks to one another with track references.
- [Chapter lists](chapter_lists.md)
  A chapter list provides a set of named entry points into a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/streaming_media)*