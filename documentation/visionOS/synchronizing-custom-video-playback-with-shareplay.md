# Synchronizing custom video playback with SharePlay

**Framework**: visionOS

Keep a custom video pipeline in sync across devices by coordinating playback in SharePlay.

**Availability**:
- visionOS 27.0+
- Xcode 27.0+

#### Overview

In visionOS, SharePlay lets people share an experience in your app, whether they’re together on a FaceTime call or nearby in the same room. This functionality matters when a video displays something that everyone needs to see at the same time, like a clue appearing on a wall in an escape-room game. Apps that build their own video playback pipeline can support coordinated playback in a SharePlay session by routing playback through an [`AVDelegatingPlaybackCoordinator`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator).

This pipeline has three parts: a renderer, a coordinator, and a synchronizer. The renderer decodes the video and draws its frames. The coordinator shares playback state with the group. The synchronizer controls the playback rate and position, which is how the app plays, pauses, and seeks.

In this sample, participants watch a video together in a shared immersive space. The video plays across the surface of a custom undulating blob that ripples and shifts. When any participant plays, pauses, or seeks, the video updates on every device.

> ❗ **Important**:  This sample is for apps that play media with their own player rather than [`AVPlayer`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avplayer). Apps that play video using `AVPlayer` should use [`AVPlayerPlaybackCoordinator`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator). For a full walkthrough, see [`Supporting coordinated media playback`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/supporting-coordinated-media-playback).

#### Join a Shareplay Session

To watch together, every participant’s device has to join the same SharePlay session and agree on what’s shared. A session starts from a group activity, so the app defines a single [`GroupActivity`](https://developer.apple.comhttps://developer.apple.com/documentation/groupactivities/groupactivity), `SyncCustomVideoPlaybackActivity`, that describes the shared experience. The activity carries `videoName` and `videoExtension`, so every device loads the same file from its own bundle, as seen here:

```swift
nonisolated struct SyncCustomVideoPlaybackActivity: GroupActivity, Transferable {
    static let title = "Sync Custom Video Playback"

    var videoName = "BOT-anist_video"
    var videoExtension = "mov"

    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.type = .watchTogether
        metadata.title = Self.title
        metadata.sceneAssociationBehavior = .none
        return metadata
    }
}
```

The video plays in the immersive space, not in the window people use to join, so the app opts out of the default scene association by setting [`sceneAssociationBehavior`](https://developer.apple.comhttps://developer.apple.com/documentation/groupactivities/sceneassociationbehavior) to `.none`.

When a participant starts the activity, the system delivers a group session to the app on every participant’s device. The app receives the session by observing `SyncCustomVideoPlaybackActivity.sessions()`. When a session arrives, the app initializes the coordinated playback pipeline for the video the activity names, configures the session’s [`SystemCoordinator`](https://developer.apple.comhttps://developer.apple.com/documentation/groupactivities/systemcoordinator) to share the immersive space, then joins the SharePlay session, like this:

```swift
// Await new sessions to arrive.
for await session in SyncCustomVideoPlaybackActivity.sessions() {
    // Create and configure new pipelines for render and coordination.
    guard let playback = await makePlayback(
        videoName: session.activity.videoName,
        videoExtension: session.activity.videoExtension
    ) else {
        continue
    }
    playbackRenderer = playback.renderer
    playbackCoordinator = playback.coordinator

    if let systemCoordinator = await session.systemCoordinator {
        systemCoordinator.configuration.supportsGroupImmersiveSpace = true
        systemCoordinator.configuration.spatialTemplatePreference = .sideBySide
    }

    // Join the session to participate in playback coordination.
    session.join()
    playbackCoordinator?.coordinateWithSession(session)
    groupSession = session
}
```

Passing the session to [`coordinateWithSession(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/coordinatewithsession(_:)) connects the coordinator to the SharePlay session, which carries playback state between this device and the others. Because the app builds the pipeline before it joins, the renderer is ready to apply the first command the coordinator issues.

> **Note**: Simulator has limited support for SharePlay, so playback can take several seconds to start after you tap the Play button.

For more on building SharePlay apps in visionOS, see [`Implementing SharePlay for immersive spaces in visionOS`](https://developer.apple.comhttps://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos) and [`Building a guessing game for visionOS`](https://developer.apple.comhttps://developer.apple.com/documentation/groupactivities/building-a-guessing-game-for-visionos).

#### Read and Decode the Frames

A participant can seek to any point in the video, so the app has to start showing frames from the moment the person chooses rather than from the beginning. The sample’s `VideoSampleSource` opens the bundled video with an [`AVAssetReader`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avassetreader), starts reading at the requested position, and returns the reader and a provider that supplies the video frames one at a time. The code below demonstrates that process:

```swift
// Build a reader, with its sample provider, positioned at the given time.
func makeReaderAndProvider(at startTime: CMTime) async throws -> sending (reader: AVAssetReader, provider: SampleProvider) {
    guard startTime.isNumeric else { throw SampleSourceError.invalidStartTime }

    let videoTracks = try await asset.loadTracks(withMediaType: .video)
    guard let videoTrack = videoTracks.first else { throw SampleSourceError.noVideoTrack }

    let reader = try AVAssetReader(asset: asset)

    let outputSettings: [String: Any] = [
        kCVPixelBufferPixelFormatTypeKey as String:
            kCVPixelFormatType_420YpCbCr8BiPlanarFullRange,
        kCVPixelBufferIOSurfacePropertiesKey as String: [:]
    ]
    let output = AVAssetReaderTrackOutput(
        track: videoTrack,
        outputSettings: outputSettings
    )

    let provider = reader.outputProvider(for: output)

    reader.timeRange = CMTimeRange(start: CMTimeMaximum(.zero, startTime), duration: .positiveInfinity)

    do {
        try reader.start()
    } catch {
        throw reader.error ?? error
    }

    return (reader, provider)
}
```

The output settings request `IOSurface-backed` buffers in a pixel format the renderer can display. Setting [`timeRange`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avassetreader/timerange) lets decoding begin mid-video, and the renderer pulls each frame from the provider with [`next()`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/next()). Returning the reader alongside the provider lets the pump cancel it when it stops pulling frames.

#### Render the Frames in Order

For the video to play smoothly without stale frames, samples reach the [`AVSampleBufferVideoRenderer`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer) in order. The renderer holds a queue of decoded frames, but it doesn’t decide when to show them. An [`AVSampleBufferRenderSynchronizer`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer) owns the timeline the renderer presents the decoded frames against. The `PlaybackRenderer` connects the two when it initializes, registering the video renderer with the synchronizer through [`sampleBufferReceiver(adding:)`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/samplebufferreceiver(adding:)-rxap), which returns the receiver the pump enqueues into, like this:

```swift
self.pump = VideoSamplePump(
    receiver: synchronizer.sampleBufferReceiver(adding: renderer),
    sampleSource: sampleSource,
    synchronizer: synchronizer
)
```

From then on, the pump enqueues frames into that receiver, and the synchronizer’s rate and time determine which frame the renderer presents at each moment. Decoding is continuous work, so `VideoSamplePump` runs it on its own task off the main actor. Starting a new supply of frames replaces the previous one, so `start(at:)` tears down the existing task and clears the queue before it decodes from the new position, as shown here:

```swift
// Starts a new supply of samples at the given time.
func start(at time: CMTime) async -> AsyncStream<SampleSourceStatus> {
    // Replace any existing supply.
    renderTask?.cancel()
    _ = await renderTask?.value
    receiver.flush()

    return AsyncStream { continuation in
        renderTask = Task(name: "render", priority: .userInitiated) { [self] in
            defer { renderTask = nil; continuation.finish() }
            do {
                var (reader, provider) = try await sampleSource.makeReaderAndProvider(at: time)
                defer { reader.cancelReading() }
                while !Task.isCancelled, let sample = try await provider.next() {
                    switch try await receiver.enqueue(sample) {
                    case .enqueued, .enqueuedWithDecodeFailures:
                        continuation.yield(.enqueued)
                    case .cancelledDueToFlush:
                        continuation.yield(.suspended)
                        return
                    case .cancelledDueToFlushRequiredToResume(let error):
                        // Flush and resume enqueuing samples at the current time.
                        let resume = synchronizer.currentTime()
                        let previousRate = synchronizer.rate
                        synchronizer.setRate(0, time: resume)
                        receiver.flush()
                        reader.cancelReading()
                        (reader, provider) = try await sampleSource.makeReaderAndProvider(at: resume)
                        if previousRate > 0 {
                            synchronizer.setRate(previousRate, time: resume)
                        }
                        continuation.yield(.failed(error))
                    case .cancelledDueToError(let error):
                        continuation.yield(.failed(error))
                        return
                    @unknown default:
                        continuation.yield(.suspended)
                        return
                    }
                }
                continuation.yield(Task.isCancelled ? .suspended : .finished)
            } catch is CancellationError {
                continuation.yield(.suspended)
            } catch {
                continuation.yield(.failed(error))
            }
        }
    }
}
```

Frames decode over time rather than all at once, so `start(at:)` returns an [`AsyncStream`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/asyncstream) immediately and reports the supply’s progress on it. The render task keeps decoding in the background, yielding `enqueued` as each frame reaches the queue, `finished` after it enqueues the last frame in the video, `failed` if the reader or receiver reports an error, or `suspended` when another playback command replaces the task. Because the task cancels the old reader as it exits, no frames from the previous position can reach the renderer.

#### Apply Playback Commands

The renderer has to respond to play, pause, and seek commands. This sample’s `PlaybackRenderer` applies each one by setting a rate and a time on the [`AVSampleBufferRenderSynchronizer`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer) it owns, as demonstrated below. The rate is the playback speed, where `0` pauses playback and `1` plays at normal speed, and the time is the position in the video. For example, to begin playback, `applyPlay` starts the pump if nothing is decoding yet, then sets the rate and time the group asked for.

```swift
private func applyPlay(rate: Float, time: CMTime, atHostTime: CMTime) async {
    if let durationSeconds, time.seconds >= durationSeconds {
        return
    }
    if await pump.isDecoding == false {
        synchronizer.setRate(0, time: time)
        let statusStream = await pump.start(at: time)
        observeStatus(statusStream)
    }
    setRate(rate, time: time, atHostTime: atHostTime)
}

private func observeStatus(_ stream: AsyncStream<SampleSourceStatus>) {
    statusTask?.cancel()
    statusTask = Task { @MainActor [weak self] in
        for await status in stream {
            self?.renderStatus = status
        }
    }
}

private func setRate(_ rate: Float, time: CMTime, atHostTime: CMTime? = nil) {
    if let atHostTime {
        synchronizer.setRate(rate, time: time, atHostTime: atHostTime)
    } else {
        synchronizer.setRate(rate, time: time)
    }
    isPlaying = rate > 0
}
```

The pump decides which frames to decode, and the synchronizer decides when to show them. Each decoded frame keeps its timestamp from the video, so the position given to the pump and the time set on the synchronizer have to match, or the synchronizer waits on timestamps that never arrive. The other commands work the same way: `applyPause` sets the rate to zero, while `applySeek` and `applyBuffering` also call `pump.start(at:)` so the pump queues frames at the position about to play.

The coordinator, described in the next section, issues each command: play, pause, seek, or buffer. Play, pause, and seek follow from something a participant does, whereas buffer tells the device that playback is about to start. Each command carries a completion handler that the renderer needs to call after it finishes handling that command, which is how the coordinator knows this device finished responding to it.

Commands can arrive while the renderer is still applying the last one, and applying two at once would leave the synchronizer at the wrong rate or time. So each command has to run to completion before the next one starts. The renderer reads commands from an [`AsyncStream`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/asyncstream) on the main actor, in the order the coordinator issued them, so `handle` finishes one command before the loop pulls the next, as shown here:

```swift
// Commands flow from the coordinator's delegate to the renderer.
enum Command: Sendable {
    case play(rate: Float, time: CMTime, atHostTime: CMTime, completionHandler: @Sendable () -> Void)
    case pause(completionHandler: @Sendable () -> Void)
    case seek(time: CMTime, completionHandler: @Sendable () -> Void)
    case buffer(completionHandler: @Sendable () -> Void)
}

// Apply the coordinated command in a serial order.
func drain(commands: AsyncStream<Command>) {
    self.drainTask?.cancel()
    self.drainTask = Task { @MainActor [weak self] in
        for await command in commands {
            await self?.handle(command)
        }
    }
}

private func handle(_ command: Command) async {
    switch command {
    case let .play(rate, time, atHostTime, completionHandler):
        await applyPlay(rate: rate, time: time, atHostTime: atHostTime)
        completionHandler()
    // ...
    }
}
```

Play, pause, and seek all start with one participant’s action, which the coordinator turns into a command that every device receives.

#### Coordinate Playback Commands

When a participant plays, pauses, or seeks, every device has to carry out that action, and the app has to respond to actions other participants take. The sample defines a `PlaybackCoordinator` that owns an [`AVDelegatingPlaybackCoordinator`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator) and routes every action through it rather than changing playback directly. For example, when a participant plays, the app asks the coordinator for a rate change with [`coordinateRateChange(to:options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateratechange(to:options:)), like this:

```swift
init() {
    let (stream, continuation) = AsyncStream.makeStream(of: Command.self)
    self.commands = stream
    self.continuation = continuation
    let delegate = PlaybackControlDelegate(continuation: continuation)
    self.delegate = delegate
    let coordinator = AVDelegatingPlaybackCoordinator(playbackControlDelegate: delegate)
    // Adopt the group's current rate and time when joining.
    coordinator.transitionToItem(withIdentifier: Self.itemIdentifier, proposingInitialTimingBasedOn: nil)
    self.coordinator = coordinator
}

func coordinatePlay() {
    coordinator.coordinateRateChange(to: 1, options: [])
}
```

Passing a shared identifier to [`transitionToItem(withIdentifier:proposingInitialTimingBasedOn:)`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:)) keeps every device coordinating the same item, so a device joining midway adopts the group’s current rate and time.

Calling `coordinatePlay()` doesn’t immediately start playback. Each device’s `AVDelegatingPlaybackCoordinator` calls its [`AVPlaybackCoordinatorPlaybackControlDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate) with the command to perform, including on the device that made the request, as shown below. The sample’s `PlaybackControlDelegate` isn’t main-actor isolated, so it yields each command onto an [`AsyncStream`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/asyncstream) rather than touching the renderer directly. Playback starts when the renderer drains that command and sets the rate.

```swift
private nonisolated final class PlaybackControlDelegate: NSObject, AVPlaybackCoordinatorPlaybackControlDelegate {
    private let continuation: AsyncStream<Command>.Continuation

    init(continuation: AsyncStream<Command>.Continuation) {
        self.continuation = continuation
    }

    // Yield coordination commands onto the stream for `PlaybackRenderer` to consume.
    private func dispatch(_ command: Command) {
        if case .terminated = continuation.yield(command) {
            switch command {
            case .play(_, _, _, let completionHandler),
                 .pause(let completionHandler),
                 .seek(_, let completionHandler),
                 .buffer(let completionHandler):
                completionHandler()
            }
        }
    }

    func playbackCoordinator(
        _ coordinator: AVDelegatingPlaybackCoordinator,
        didIssue playCommand: AVDelegatingPlaybackCoordinatorPlayCommand,
        completionHandler: @escaping @Sendable () -> Void
    ) {
        dispatch(.play(
            rate: playCommand.rate,
            time: playCommand.itemTime,
            atHostTime: playCommand.hostClockTime,
            completionHandler: completionHandler
        ))
    }
    // ...
}
```

A play command also carries the group’s host clock time, so every device begins from the same moment on a shared clock.

## See Also

- [Building a guessing game for visionOS](../groupactivities/building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [Implementing SharePlay for immersive spaces in visionOS](implementing-shareplay-for-immersive-spaces-in-visionos.md)
  Enable collaborative spatial experiences by using SharePlay to synchronize 3D content among participants.
- [Configure your visionOS app for sharing with people nearby](../groupactivities/configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](../groupactivities/adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [Synchronizing group gameplay with TabletopKit](../tabletopkit/synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/synchronizing-custom-video-playback-with-shareplay)*