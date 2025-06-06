# Finding an original media track from a hint track

**Framework**: QuickTime File Format

Use track reference atoms from hint tracks to locate the original media track.

#### Overview

Like any other QuickTime track, hint tracks can contain track reference atoms. Exactly one of these must be of track reference type `'hint'`, and its internal list must contain at least one track ID, which is the track ID of the original media track. Like other track reference atoms, there may be empty references in this list, indicated by a track ID of `0`. For hint tracks that refer to more than one track, the index number (starting at `1`, and including any `0` entries) is used in the media track reference index field in some of the packet data table entry modes.

For example, if you have MPEG-1 video at track ID 11 and MPEG-1 layer 2 audio at track ID 12, and you are creating a RTP hint track that encapsulates these in an MPEG-2 transport, you need to refer to both tracks. You can also assume that there are some empty entries and other track references in your hint track atom reference atom’s list. So it might look like this: `11, 0, 0, 14, 0, 12, 0`. When you are assembling packets from audio and video tracks `11` and `12`, you use their list indexes (`1` and `6`) in the media track ref index field.

If you have only one media track listed in your hint track reference, you may simply use a `0` in the media track ref index field.

## See Also

- [Hint media](hint_media.md)
  Provide information about data units to stream in hint tracks.
- [RTP hint tracks](rtp_hint_tracks.md)
  Allow a streaming server to create RTP streams from a QuickTime movie.
- [Hint track sample description](hint_track_sample_description.md)
  An atom that specifies the data format and location of the hint track sample data.
- [Packetization hint sample data](packetization_hint_sample_data.md)
  An atom that describes the sample data for data using the Real-Time Transport Protocol (RTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/finding_an_original_media_track_from_a_hint_track)*