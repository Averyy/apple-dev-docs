# Creating movies with modifier tracks

**Framework**: QuickTime File Format

Send data to another media handler instead of presenting media directly.

#### Overview

QuickTime 2.1 added additional functionality for media handlers. By way of modifier tracks, a media handler can send its data to another media handler rather than presenting its media directly. See [`Modifier tracks`](modifier_tracks.md) for a complete discussion of this feature.

To create a movie with modifier tracks, first you create a movie with all the desired tracks, then you create the modifier track. To link the modifier track to the track that it modifies, you use the `AddTrackReference` function as shown in the following listing.

```c
long addedIndex;
AddTrackReference(aVideoTrack, aModifierTrack,
                    kTrackModifierReference, &addedIndex);
```

The reference doesn’t completely describe the modifier track’s relationship to the track it modifies. Instead, the reference simply tells the modifier track to send its data to the specified track. The receiving track doesn’t “know” what it should do with that data. A single track may also be receiving data from more than one modifier track.

To describe how each modifier input should be used, each track’s media also has an input map. The media’s input map describes how the data being sent to each input of a track should be interpreted by the receiving track. After creating the reference, it is necessary to update the receiving track’s media input map. When `AddTrackReference` is called, it returns the index of the reference added. That index is the index of the input that needs to be described in the media input map. If the modifier track created above contains regions to change the shape of the video track, the code shown in the following listing updates the input map appropriately.

```c
QTAtomContainer inputMap;
QTAtom inputAtom;
OSType inputType;
 
 
Media aVideoMedia = GetTrackMedia(aVideoTrack);
GetMediaInputMap (aVideoMedia, &inputMap);
 
QTInsertChild(inputMap, kParentAtomIsContainer, kTrackModifierInput,
        addedIndex, 0,0, nil, &inputAtom);
 
inputType = kTrackModifierTypeClip;
QTInsertChild (inputMap, inputAtom, kTrackModifierType, 1, 0,
        sizeof(inputType), &inputType, nil);
 
SetMediaInputMap(aVideoMedia, inputMap);
QTDisposeAtomContainer(inputMap);
```

The media input map allows you to store additional information for each input. In the preceding example, only the type of the input is specified. In other types of references, you may need to specify additional data.

When a modifier track is playing an empty track edit, or is disabled or deleted, all receiving tracks are notified that the track input is inactive. When an input becomes inactive, it is reset to its default value. For example, if a track is receiving data from a clip modifier track and that input becomes inactive, the shape of the track reverts to the shape it would have if there were no clip modifier track.

## See Also

- [Modifier tracks](modifier_tracks.md)
  Create dynamic movies with modifier tracks that send data to another track.
- [Track references](track_references.md)
  Relate a movie’s tracks to one another with track references.
- [Chapter lists](chapter_lists.md)
  A chapter list provides a set of named entry points into a movie.
- [Streaming media](streaming_media.md)
  Store streaming data in a streaming media track for QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_movies_with_modifier_tracks)*