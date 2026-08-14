# Swift updates

**Framework**: Updates

Learn about important changes to Swift.

#### Overview

Browse notable changes in [`Swift`](https://developer.apple.com/documentation/swift). For information about Swift language changes, refer to [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/revisionhistory).

#### June 2025

##### Swift Standard Library

- Safely access contiguous regions of memory, like a container’s underlying storage, using [`Span`](https://developer.apple.com/documentation/swift/span) and [`RawSpan`](https://developer.apple.com/documentation/swift/rawspan). Safely modify that memory using [`MutableSpan`](https://developer.apple.com/documentation/swift/mutablespan) and [`MutableRawSpan`](https://developer.apple.com/documentation/swift/mutablerawspan). Many collections in the standard library now have a `span` property that provides access to their underlying storage. `Span` has a [`bytes`](https://developer.apple.com/documentation/swift/span/bytes-8rxg) property to access the raw storage when the element type supports it.
- Process Unicode strings efficiently and safely, using [`UTF8Span`](https://developer.apple.com/documentation/swift/utf8span) to access a contiguous region of memory.
- Create fixed-size arrays that have contiguous underlying storage using [`InlineArray`](https://developer.apple.com/documentation/swift/inlinearray).
- To identify a task during debugging, you can set a name for a detached task using [`init(name:priority:operation:)`](https://developer.apple.com/documentation/swift/task/init(name:priority:operation:)-43wmk), and for a task in a task group using [`addTask(name:priority:operation:)`](https://developer.apple.com/documentation/swift/taskgroup/addtask(name:priority:operation:)). Access the current task’s name using [`name`](https://developer.apple.com/documentation/swift/task/name-swift.property).
- Start a task immediately using [`immediate(name:priority:executorPreference:operation:)`](https://developer.apple.com/documentation/swift/task/immediate(name:priority:executorpreference:operation:)-9bghc).

#### June 2024

##### Swift Standard Library

- Operate on noncontiguous ranges in collections using [`RangeSet`](https://developer.apple.com/documentation/swift/rangeset) and [`DiscontiguousSlice`](https://developer.apple.com/documentation/swift/discontiguousslice).
- Control which executor runs a task using [`TaskExecutor`](https://developer.apple.com/documentation/swift/taskexecutor).
- Validate that C strings contain well-formed Unicode text when converting to them to `String` with [`init(validatingCString:)`](https://developer.apple.com/documentation/swift/string/init(validatingcstring:)-992vo) and [`init(validating:as:)`](https://developer.apple.com/documentation/swift/string/init(validating:as:)-84qr9).
- Preserve more information about thrown errors from [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) and [`AsyncIteratorProtocol`](https://developer.apple.com/documentation/swift/asynciteratorprotocol) using their `Failure` associated type.

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