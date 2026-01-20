# Implementing SharePlay for immersive spaces in visionOS

**Framework**: visionOS

Enable collaborative spatial experiences by using SharePlay to synchronize 3D content among participants.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

Immersive spaces in visionOS are unbounded 3D environments that allow you to place content anywhere in someone’s surroundings. With SharePlay, multiple people can collaborate within these spaces, creating synchronized shared experiences for gaming, training, collaboration, and entertainment.

This sample code project uses SharePlay to create a shared spatial experience for an immersive space in visionOS. Participants in a FaceTime call, or using nearby sharing (a peer-to-peer connection between nearby devices), can tap a 3D cube to change its color. All participants in the session see the color changes in real time.

![A screenshot of an immersive space in an Apple Vision Pro showing a start button above a red cube.](https://docs-assets.developer.apple.com/published/ebee7c2518604f9c3a2e49f3e1f36baa/start%402x.png)

This sample code project provides a small-scale app that demonstrates:

- Creating a custom [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity).
- Starting a SharePlay session of your activity type.
- Monitoring for, configuring, and joining active sessions.
- Synchronizing state changes.

> **Note**: SharePlay requires the `Group Activities` capability. For instructions on adding a capability to your project in Xcode, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

For a more in-depth SharePlay sample code project, see [`Building a guessing game for visionOS`](https://developer.apple.com/documentation/GroupActivities/building-a-guessing-game-for-visionos).

##### Define a Custom Group Activity

The sample creates a [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity) that defines the shared experience and allows you to start an activity-related SharePlay session. The activity provides metadata that appears in the system UI when people share an experience.

The sample defines `ChangeColorActivity` to represent the shareable color-changing experience. The title and subtitle appear in the SharePlay invitation and active session UI to help people understand what they’re sharing.

```swift
struct ChangeColorActivity: GroupActivity, Transferable {
    /// Configures the displayed SharePlay activity metadata.
    var metadata: GroupActivityMetadata = {
        var metadata = GroupActivityMetadata()
        metadata.type = .generic
        metadata.title = "Cube Together"
        metadata.subtitle = "Change colors of items in the immersive space with friends."
        return metadata
    }()
}
```

See [`Defining your app’s SharePlay activities`](https://developer.apple.com/documentation/GroupActivities/defining-your-apps-shareplay-activities) for more information.

##### Start a Shareplay Session

The app displays a Start button when someone isn’t part of an active SharePlay sesssion. When a person presses the Start button, the sample calls [`activate()`](https://developer.apple.com/documentation/GroupActivities/GroupActivity/activate()) to configure a session and invite other participants to join the activity.

```swift
  var sharePlayButton: some View {
    Group {
        Button("\(appModel.isSharePlayActive ? "End" : "Start") SharePlay") {
            if appModel.isSharePlayActive {
                appModel.endSession()
            } else {
                Task { @concurrent in
                    do {
                        // Directly start the group activity.
                        if !(try await ChangeColorActivity().activate()) {
                            print("No session was created, or it was handed off to an Apple TV.")
                        }
                    } catch {
                        // No FaceTime call is active, or the session failed to start.
                        print("Failed to create a session: \(error.localizedDescription)")
                    }
                }
            }
        }
    }
}
```

In visionOS, if a person is on a FaceTime call or is nearby sharing with someone, calling `activate()` on the [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity) starts the activity. Otherwise, the system displays the sharing sheet to allow people to start a FaceTime call or a nearby sharing session.

> **Note**: In visionOS, windows and immersive spaces handle SharePlay sessions differently. This sample demonstrates using an immersive space. For information on starting a SharePlay session in a window, see [`Presenting SharePlay activities from your app’s UI`](https://developer.apple.com/documentation/GroupActivities/promoting-shareplay-activities-from-your-apps-ui).

##### Join and Manage the Activity

When someone starts a SharePlay session, the system creates a [`GroupSession`](https://developer.apple.com/documentation/GroupActivities/GroupSession) for the custom activity to synchronize content between devices. To join a started activity, the sample continuously monitors for new `ChangeColorActivity` sessions. When one becomes available, the sample starts observing the session state and creates a `SessionController` to manage the session.

```swift
private func observeGroupSessions() async {
    // When a new `GroupSession` of `ChangeColorActivity` is available, set up a `SessionController` to manage the session and join it.
    for await session in ChangeColorActivity.sessions() {
        let sessionController = await SessionController(session, appModel: self)
        guard let sessionController else {
            continue
        }

        self.sessionController = sessionController

        // Create a task to observe the group session state and clear the
        // session controller when the group session invalidates.
        Task.immediate(name: "session state observation") {
            for await state in session.$state.values {
                guard self.sessionController?.session.id == session.id else {
                    return
                }

                if case .invalidated = state {
                    self.sessionController = nil
                    return
                }
            }
        }
    }
}
```

The sample uses the `GroupSession` of the activity to create a `SessionController`, which handles session setup, participant management, joining the activity, and state synchronization. The session controller sets up the [`GroupSessionMessenger`](https://developer.apple.com/documentation/GroupActivities/GroupSessionMessenger) and [`SystemCoordinator`](https://developer.apple.com/documentation/GroupActivities/SystemCoordinator), and then starts observing messages and participant updates before adding the person to the session.

```swift
init?(_ groupSession: GroupSession<ChangeColorActivity>, appModel: AppModel) async {
   guard let groupSystemCoordinator = await groupSession.systemCoordinator else {
       return nil
   }
   // Keep track of the current session.
   session = groupSession

   // Create a `GroupSessionMessenger` with the provided `GroupSession` 
   // and a reliable delivery mode to keep the color in sync for all participants.
   // Use `.unreliable` for updates that are more important for the system to send and receive quickly rather than be correct.
   messenger = GroupSessionMessenger(session: session, deliveryMode: .reliable)

   // Initialize the update counter to prevent conflicts when multiple participants make changes.
   latestCubeColorUpdateCount = MessageUpdateCount(count: 0, participant: session.localParticipant.id)

   // Coordinates spatial aspects of a SharePlay session.
   systemCoordinator = groupSystemCoordinator

   self.appModel = appModel

   // Observe and sync new color changes.
   observeUpdateColorMessages()
   // Observe new active participants and remove inactive participants.
   observeActiveRemoteParticipants()

   // Ensure support for the group immersive space.
   systemCoordinator.configuration.supportsGroupImmersiveSpace = true
   // Set the spatial template to be side by side to see the cube from the same viewpoint.
   systemCoordinator.configuration.spatialTemplatePreference = .sideBySide

   session.join()
}
```

The `.sideBySide` spatial template ensures all participants share a consistent viewing perspective, which is essential for collaborative 3D experiences.

> ❗ **Important**: Set [`supportsGroupImmersiveSpace`](https://developer.apple.com/documentation/GroupActivities/SystemCoordinator/Configuration-swift.struct/supportsGroupImmersiveSpace) to `true` to see personas in the immersive space. For information about personas in SharePlay, see [`Adding spatial Persona support to an activity`](https://developer.apple.com/documentation/GroupActivities/adding-spatial-persona-support-to-an-activity).

The session controller handles observing when participants join or leave, and brings people up to date if they join late.

```swift
 private func observeActiveRemoteParticipants() {
    Task.immediate(name: "active participant observation") {
        var previousActiveParticipants = Set<Participant>()

        // Iterate through active participants and remove inactive participants.
        for await activeParticipants in session.$activeParticipants.values {
            let currentActiveParticipants = activeParticipants.filter { $0.id != session.localParticipant.id }
            defer {
                previousActiveParticipants = currentActiveParticipants
            }
            // Calculate which participants are new since the last update.
            let newActiveParticipants = currentActiveParticipants.subtracting(previousActiveParticipants)

            if !newActiveParticipants.isEmpty {
                do {
                    // Send the current color state to new participants to bring them up to date.
                    let catchupMessage = UpdateColorMessage(cubeColor: appModel?.color ?? .red, updateCount: latestCubeColorUpdateCount)
                    try await messenger.send(catchupMessage, to: .only(newActiveParticipants))
                } catch {
                    print("Failed to send cube color update message, \(error)")
                }
            }
        }
    }
}
```

For more information, see [`Joining and managing a shared activity`](https://developer.apple.com/documentation/GroupActivities/joining-and-managing-a-shared-activity).

##### Send and Receive Messages to Synchronize State

When someone taps the cube, the sample sets the cube’s color to a random color.

```swift
SpatialTapGesture()
    .onEnded { _ in
        // Select a random color that's different from the current color.
        let randomColor = CubeColor.allCases.filter { $0 != appModel.color }.randomElement() ?? .red
        // Sync the changes to others in the SharePlay session when the tap occurs, if there is one.
        // Only set `syncChanges` to `true` when receiving changes directly from the UI.
        appModel.setColor(to: randomColor, syncChanges: true)
    }
```

When the color of the cube changes, the sample uses [`GroupSessionMessenger`](https://developer.apple.com/documentation/GroupActivities/GroupSessionMessenger) to send messages to the other participants, notifying them of the change.

The app model updates the local color and conditionally syncs the change using the session controller if `syncChanges` is `true` and an active SharePlay session exists. The method uses the `syncChanges` parameter to prevent infinite cycles of sending messages when the local state updates after receiving a message.

```swift
func setColor(to newColor: CubeColor, syncChanges: Bool = false) {
    color = newColor
    // When `syncChanges` is `true`, the change originates from a user interaction that the system needs to sync with other participants.
    // When `syncChanges` is `false`, the change is from another participant and the system applies it locally. 
    // Prevent infinite cycles by not syncing when receiving changes.
    if syncChanges, let sessionController {
        sessionController.syncColorChange(to: color)
    }
}
```

The session controller handles sending and receiving messages between participants in the session. To send and receive custom data types with `GroupSessionMessenger`, the sample creates a `Codable` structure that defines the app-specific information to share among participants.

```swift
struct UpdateColorMessage: Codable, Sendable {
    /// The new color to apply to the cube.
    let cubeColor: CubeColor
    /// The update counter that determines message ordering and prevents conflicts.
    let updateCount: MessageUpdateCount
}
```

> ❗ **Important**: The update count ensures the app can determine which change takes precedence when multiple participants make changes simultaneously.

##### Apply Color Changes

To send the new color change message, the sample creates an `UpdateColorMessage` instance with the new color and incremented update count before sending it with `GroupSessionMessenger`.

```swift
func syncColorChange(to color: CubeColor) {
    latestCubeColorUpdateCount.count += 1
    latestCubeColorUpdateCount.participant = session.localParticipant.id
    
    // Create and send the message with the new color.
    let updateColorMessage = UpdateColorMessage(cubeColor: color, updateCount: latestCubeColorUpdateCount)

    Task {
        do {
            try await messenger.send(updateColorMessage)
        } catch {
            print("Error while sending message: ", error)
        }
    }
}
```

The session controller handles receiving `UpdateColorMessage` instances from other participants during the active SharePlay session. During initialization, the session controller creates a task that responds to incoming messages. When a participant makes a change and the session controller receives the message, the sample locally updates the color, automatically syncing the UI. For example, if a participant changes the color to blue, the other participants see the cube change to blue when the session controller receives the message.

```swift
private func observeUpdateColorMessages() {
    Task.immediate(name: "update color message observation") {
        // Listen for messages for updated colors.
        for await (message, _) in messenger.messages(of: UpdateColorMessage.self) {
            // Only apply updates from messages that are more recent than the latest local counter.
            guard message.updateCount > latestCubeColorUpdateCount else {
                continue
            }
            latestCubeColorUpdateCount = message.updateCount
            // Apply the color change locally.
            appModel?.setColor(to: message.cubeColor)
        }
    }
}
```

For more information on sending and receiving data, see [`Synchronizing data during a SharePlay activity`](https://developer.apple.com/documentation/GroupActivities/synchronizing-data-during-a-shareplay-activity).

## See Also

- [Building a guessing game for visionOS](../GroupActivities/building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [Configure your visionOS app for sharing with people nearby](../GroupActivities/configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](../GroupActivities/adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [Synchronizing group gameplay with TabletopKit](../TabletopKit/synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos)*