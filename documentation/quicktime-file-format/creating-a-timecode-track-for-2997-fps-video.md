# Creating a timecode track for 29.97 FPS video

**Framework**: QuickTime File Format

Configure a timecode track to specify timecode information for other tracks.

#### Overview

A timecode track specifies timecode information for other tracks. The timecode keeps track of the time codes of the original source of the video and audio. After a movie has been edited, the timecode can be extracted to determine the source tape and the time codes of the frames.

It is important that the timecode track have the same time scale as the video track. Otherwise, the timecode will not tick at the exact same time as the video track.

For each contiguous source tape segment, there is a single timecode sample that specifies the timecode value corresponding to the start of the segment. From this sample, the timecode value can be determined for any point in the segment.

The sample description for a timecode track specifies the timecode system being used (for example, a 30-fps drop frame) and the source information. Each sample is a timecode value.

Since the timecode media handler is a derived from the base media handler, the media information atom starts with a generic media header atom. The timecode atoms would contain the following data values:

```None
Generic media header atom
├── Atom size: 80
├── Atom type: 'gmhd'
├── Generic media information atom
│   ├── Atom size: 24
│   ├── Atom type: 'gmin'
│   ├── Version/Flags: 0
│   ├── Graphics mode: 0x0040
│   ├── Opcolor (red): 0x8000
│   ├── Opcolor (green): 0x8000
│   ├── Opcolor (blue): 0x8000
│   ├── Balance: 0
│   └── Reserved: 0
└── Timecode atom
    ├── Atom size: 48
    └── Atom type | 'tmcd'
    └── Timecode media information atom
        ├── Atom size: 40
        ├── Atom type: 'tcmi'
        ├── Version/Flags: 0
        ├── Text font: 0 (system font)
        ├── Text face: 0 (plain)
        ├── Text size: 12
        ├── Padding: 0
        ├── Text color (red): 0
        ├── Text color (green): 0
        ├── Text color (blue): 0
        ├── Background color (red): 0
        ├── Background color (green): 0
        ├── Background color (blue): 0
        └── Font name: '\pChicago' (Pascal string)
```

The sample table atom contains all the standard sample atoms and has the following data values:

```None
Sample table atom
├── Atom size: 174
├── Atom type: 'stbl' (sample table)
├── Sample description atom
│   ├── Atom size: 74
│   ├── Atom type: 'stsd' (sample description)
│   ├── Version/Flags: 0
│   ├── Number of entries: 1
│   ├── Sample description size[1]: 58
│   ├── Data format[1]: 'tmcd'
│   ├── Reserved[1]: 0
│   ├── Data reference index[1]: 1
│   ├── Flags[1]: 0
│   ├── Flags (timecode)[1]: 7 (drop frame + 24 hour + negative times OK)
│   ├── Time scale[1]: 2997
│   ├── Frame duration[1]: 100
│   ├── Number of frames[1]: 20
│   └── Name atom
│       ├── Atom size: 24
│       ├── Atom type: 'name'
│       ├── String length: 12
│       ├── Language code: 0 (English)
│       └── Name: "my tape name"
├── Time to sample atom
│   ├── Atom size: 24
│   ├── Atom type: 'stts' (time to sample)
│   ├── Version/Flags: 0
│   ├── Number of entries: 1
│   ├── Sample count[1]: 1
│   └── Sample duration[1]: 1
├── Sample to chunk atom
│   ├── Atom size: 28
│   ├── Atom type: 'stsc' (sample to chunk)
│   ├── Version/Flags: 0
│   ├── Number of entries: 1
│   ├── First chunk[1]: 1
│   ├── Samples per chunk[1]: 1
│   └── Sample description ID[1]: 1
├── Sample size atom
│   ├── Atom size: 20
│   ├── Atom type: 'stsz' (sample size)
│   ├── Version/Flags: 0
│   ├── Sample size: 4
│   └── Number of entries: 1
└── Chunk offset atom
    ├── Atom size: 20
    ├── Atom type: 'stco' (chunk offset)
    ├── Version/Flags: 0
    ├── Number of entries: 1
    └── Offset[1]: (offset into file of chunk 1)
```

In the example, let’s assume that the segment’s beginning timecode is 1:15:32.4 (1 hour, 15 minutes, 32 seconds, and 4 frames). The time would be expressed in the data file as `0x010F2004` (`0x01` = 1 hour; `0x0F` = 15 minutes; `0x20` = 32 seconds; `0x04` = 4 frames).

The video and sound tracks must contain a track reference atom to indicate that they reference this timecode track. The track reference is the same for both and is contained in the track atom (at the same level as the track header and media atoms).

This track reference would contain the data values listed in the following table.

| Field | Value |
| --- | --- |
| Atom size | `12` |
| Atom type | `'tref'` |
| Reference type | `'tmcd'` |
| Track ID of referenced track (timecode track) | `3` |

In this example, the video and sound tracks are tracks `1` and `2`. The timecode track is track `3`.

## See Also

- [Timecode sample description](timecode_sample_description.md)
  An atom that defines how to interpret time code media data.
- [Timecode media information atom ('tcmi')](timecode_media_information_atom.md)
  An atom that governs how the timecode text is displayed.
- [Timecode sample data](timecode_sample_data.md)
  An atom that represents timecode sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_a_timecode_track_for_2997_fps_video)*