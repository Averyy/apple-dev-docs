# Swift updates

**Framework**: Updates

Learn about important changes to Swift.

#### Overview

Browse notable changes in [`Swift`](https://developer.apple.com/documentation/Swift). For information about Swift language changes, refer to [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/revisionhistory).

#### June 2025

##### Swift Standard Library

- Safely access contiguous regions of memory, like a container’s underlying storage, using [`Span`](https://developer.apple.com/documentation/Swift/Span) and [`RawSpan`](https://developer.apple.com/documentation/Swift/RawSpan). Safely modify that memory using [`MutableSpan`](https://developer.apple.com/documentation/Swift/MutableSpan) and [`MutableRawSpan`](https://developer.apple.com/documentation/Swift/MutableRawSpan). Many collections in the standard library now have a `span` property that provides access to their underlying storage. `Span` has a [`bytes`](https://developer.apple.com/documentation/Swift/Span/bytes) property to access the raw storage when the element type supports it.
- Process Unicode strings efficiently and safely, using [`UTF8Span`](https://developer.apple.com/documentation/Swift/UTF8Span) to access a contiguous region of memory.
- Create fixed-size arrays that have contiguous underlying storage using [`InlineArray`](https://developer.apple.com/documentation/Swift/InlineArray).
- To identify a task during debugging, you can set a name for a detached task using [`init(name:priority:operation:)`](https://developer.apple.com/documentation/Swift/Task/init(name:priority:operation:)-43wmk), and for a task in a task group using [`addTask(name:priority:operation:)`](https://developer.apple.com/documentation/Swift/TaskGroup/addTask(name:priority:operation:)). Access the current task’s name using [`name`](https://developer.apple.com/documentation/Swift/Task/name).
- Start a task immediately using [`immediate(name:priority:executorPreference:operation:)`](https://developer.apple.com/documentation/Swift/Task/immediate(name:priority:executorPreference:operation:)-9bghc).

#### June 2024

##### Swift Standard Library

- Operate on noncontiguous ranges in collections using [`RangeSet`](https://developer.apple.com/documentation/Swift/RangeSet) and [`DiscontiguousSlice`](https://developer.apple.com/documentation/Swift/DiscontiguousSlice).
- Control which executor runs a task using [`TaskExecutor`](https://developer.apple.com/documentation/Swift/TaskExecutor).
- Validate that C strings contain well-formed Unicode text when converting to them to `String` with [`init(validatingCString:)`](https://developer.apple.com/documentation/Swift/String/init(validatingCString:)-992vo) and [`init(validating:as:)`](https://developer.apple.com/documentation/Swift/String/init(validating:as:)-84qr9).
- Preserve more information about thrown errors from [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) and [`AsyncIteratorProtocol`](https://developer.apple.com/documentation/Swift/AsyncIteratorProtocol) using their `Failure` associated type.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/swift)*