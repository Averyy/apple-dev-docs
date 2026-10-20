# Journaling Suggestions updates

**Framework**: Updates  
**Role**: Article

Learn about important changes in Journaling Suggestions.

#### Overview

Browse notable changes in [Journaling Suggestions](../JournalingSuggestions/JournalingSuggestions.md).

#### June 2025

##### iPadOS support

- [Journaling Suggestions](../JournalingSuggestions/JournalingSuggestions.md) supports iPadOS. Suggestions that the system generates on a person’s iPhone sync over iCloud to their iPad.

##### System notifications

- Register for system Journaling Suggestion notifications, which prompt users to reflect on recent moments. Refer to the notification schedule a person picks in Settings using [`JournalingSuggestionsConfiguration`](../JournalingSuggestions/journalingsuggestionsconfiguration.md). When a person taps a notification, the system launches [`JournalingSuggestionsPicker`](../JournalingSuggestions/journalingsuggestionspicker.md) for your app when you implement [`JournalingSuggestionPresentationToken`](../JournalingSuggestions/journalingsuggestionpresentationtoken.md).

##### Event posters

- Receive suggestions of the [`JournalingSuggestion.EventPoster`](../JournalingSuggestions/journalingsuggestion/eventposter.md) type for planned or attended events in Apple Invites.

##### Location and workouts

- Distinguish work-related location suggestions using the [`isWorkLocation`](../JournalingSuggestions/journalingsuggestion/location/isworklocation.md) property, and receive information about the location from MapKit with [`mapKitItemIdentifier`](../JournalingSuggestions/journalingsuggestion/location/mapkititemidentifier.md).
- Refer to the name of a particular workout suggestion with  [`localizedName`](../JournalingSuggestions/journalingsuggestion/workout/details-swift.struct/localizedname.md).

#### June 2024

##### General

- Support for landscape mode in your app.

##### Motion activity

- Capture someone’s run session as well as their mixed running and walking activity sessions with `MovementType`.

##### Media playback

- Describe media content a person listened to. The system provides an instance of this structure to your app when a person chooses a media suggestion in the `JournalingSuggestionsPicker`.
- Collect asset content that includes other media playback sessions from other music or podcast Apps.

##### State of Mind

- Suggest content to people that ask them to describe their state of mind. The system provides an instance of this structure to your app when a person chooses a state of mind suggestion in the `JournalingSuggestionsPicker`.

##### Reflection

- Use reflection prompts in your app with `Reflection`.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/journalingsuggestions)*