# Preparing sound and subtitle alternate groups for use with Apple devices

**Framework**: QuickTime File Format

Create collections of tracks that all serve the same purpose, where any track in the group can be substituted for another in a movie.

#### Overview

Alternate groups are collections of tracks that all serve the same purpose, where any track in the group can be substituted for another in a movie. Members of the same alternate group have the same identifier value in the alternate group field in the `'tkhd'` (track header) atom; see [`Track reference atoms`](track_reference_atoms.md) for an example of alternate tracks for different languages.

This section provides guidelines for the use of alternate groups in movies to be played on Apple devices.

#### General

For each alternate group:

- The group must contain tracks of only one type; for example, only subtitle tracks or only sound tracks.
- All tracks of the same type must be in a single alternate group.
- One track in the group must be enabled; that is, the Track Enabled flag must be set (`0x0001`) in its track header (`'tkhd'`).
- All other tracks in the group must be disabled.

#### Alternate Subtitle Tracks

For an alternate group that contains multiple subtitle (`'sbtl'`) tracks:

- The player must pick a subtitle track even when subtitle display is turned off.
- If any of the requirements stated in the previous General section does not hold, players may act as though there is no alternate subtitle track information.

As described in [`Subtitle sample data`](subtitle_sample_data.md), a subtitle track can contain any combination of forced (must be displayed) and non-forced (optionally displayed) subtitle samples, including the possibility of a track that contains only forced subtitle samples. Even if a user indicates, directly or indirectly, that no subtitles should be displayed, any available appropriate subtitle track should be enabled so that any forced subtitles in the track can be displayed. A means by which a player can make a default selection among subtitle alternates in the absence of a user selection is covered in Relationships across alternate groups below.

For each language in a subtitle alternate group, subtitle tracks can be configured in either of the following ways:

- Single track: Contains any combination of forced and non-forced (regular) subtitle samples.
- Track pairs: One track contains any combination of forced and non-forced (regular) subtitle samples and has a track reference of type `'forc'` that references the second track, which contains only forced samples, as described in [`Subtitle sample data`](subtitle_sample_data.md).

If the user or player picks the language of a track pair, the player application then selects the appropriate track of the pair. It must select the regular subtitle track if subtitle display is on or the forced-only subtitle track if subtitle display is off.

If a track pair is present in a subtitle alternate group, a player that displays the track languages of subtitle tracks may choose to list the language only once. If a player lists both tracks of the pair, the player should display some kind of distinction between the tracks (for example, including the track names from the `'tnam'` user data in a menu).

#### Alternate Sound Tracks

For an alternate group that contains multiple sound (`'soun'`) tracks:

- If more than one alternate group contains sound tracks, consider the alternate group that contains the enabled sound track to be the primary alternate sound track group. Ignore other alternate groups containing sound tracks.
- If there is more than one enabled sound track, or if there is an enabled sound track and a non-sound track inside the same alternate group, the player may act as though there is no alternate sound track information.
- Players may ignore sound tracks that use codecs that are unavailable.

#### Relationships Across Alternate Groups

An audio alternate group and subtitle alternate group may need to use different languages because the first is the spoken language and the second is the written language and the BCP 47 language tags may differ. If there is not a need to differentiate, use the same language code and optionally extended language tag for tracks in both alternate groups.

Sound tracks can have a track reference of type `'folw'` (for “follows”) to a single subtitle track; this track is the default to select if the sound track is selected. Use of a `'folw'` reference is a fallback in cases where the language tagging cannot be used for some reason (for example, the written language and spoken language use different extended language tags, as with Norwegian).

All subtitle tracks found in a subtitle track alternate group are candidate tracks for any chosen sound track. No facility to restrict the set of available subtitle tracks for a particular selected sound track is currently defined. However, to guide a player’s behavior in making a selection among subtitle alternates in the absence of a user selection or preference, a single subtitle track may be associated with a sound track as follows:

- A sound track may include a `'folw'` (“follows”) track reference to a corresponding subtitle track.
- If a sound track has a `'folw'` track reference to a subtitle track, that referenced subtitle track is the default subtitle track for that sound track.
- Each sound track can have either zero or one `'folw'` track references to a subtitle track.
- If a subtitle track pair is to be made the default, the sound track should have a `'folw'` track reference to the forced subtitle track of the track pair.
- If there is no `'folw'` track reference to a subtitle track, a player most commonly determines the default subtitle track by matching aspects of the audio and subtitle tracks, typically by matching the extended language tag (or language code if there is no language tag) in the set of candidate tracks. If no match is found by language, a player might choose another candidate track based upon a user preference (for example, from a list of preferred languages). Another player might choose the first track in `'trak'` box order in the `'moov'` among the candidate tracks. Another player might have another mechanism to choose the default. Possible fall-back approaches are neither enumerated nor restricted here. Note that selecting no subtitle track may be appropriate.
- If the default matching between audio language tagging and subtitle track language tagging cannot be used, a `'folw'` track reference must be authored in the media file. (For example, Norwegian as spoken uses a different language tag than the two language tags for Norwegian as written.)

## See Also

- [Creating an effect description](creating_an_effect_description.md)
  Tell QuickTime which effect to execute and control how the effect behaves at runtime with an effect description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices)*