# Destination Video

**Framework**: Visionos

Leverage SwiftUI to build an immersive media experience in a multiplatform app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- Xcode 16.0+

#### Overview

Destination Video is a multiplatform video-playback [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) app for iOS, iPadOS, macOS, tvOS, and visionOS. People get a familiar media-browsing experience navigating the libraryʼs content and playing videos they find interesting.

The sample uses the [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) structure in SwiftUI to create an immersive, full-screen browsing experience with rich navigation hierarchy. While the app shares many of its views across platforms, it leverages platform-specific features to create a playback experience native to each platform. For example, it uses the SwiftUI window and scene customization APIs to create a more engaging and natural experience in macOS. This sample also demonstrates how to use [`SwiftData`](https://developer.apple.com/documentation/SwiftData) to persist app data in a SwiftUI app.

In visionOS, the sample demonstrates how to play video within an immersive environment configured with [`Reality Composer Pro`](https://developer.apple.comhttps://developer.apple.com/documentation/visionos#realitykit-and-reality-composer-pro). It also uses the [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) framework to enable shared viewing experiences.

##### Implement Tab Navigation

Destination Video uses tab navigation with the [`sidebarAdaptable`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) style, which optimizes the content browsing experience for each platform. In iPadOS, the [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) with `sidebarAdaptable` style allows people to toggle between the sidebar and tab bar. The full-screen browsing experience of a tab bar brings content to the forefront while the sidebar allows for easy access to deeper navigation hierarchy.

To implement tab navigation, first declare a `TabView` with an explicit selection value using the [`init(selection:content:)`](https://developer.apple.com/documentation/SwiftUI/TabView/init(selection:content:)) initializer. Add tabs within a `TabView` by initializing [`Tab`](https://developer.apple.com/documentation/SwiftUI/Tab) structures. Destination Video uses the [`init(_:systemImage:value:content:)`](https://developer.apple.com/documentation/SwiftUI/Tab/init(_:systemImage:value:content:)) initializer to create each tab, then groups tabs within a [`TabSection`](https://developer.apple.com/documentation/SwiftUI/TabSection) to declare a secondary tab hierarchy in the `TabView`.

```swift
TabView(selection: $selectedTab) {
    Tab("Watch Now", systemImage: "play", value: .watchnow) {
        WatchNowView()
    }

    // More tabs...
    
    TabSection {
        ForEach(Category.collectionsList) { collection in
            Tab(collection.name, systemImage: collection.icon, value: Tabs.collections(collection)) {
                // More tabs...
            }
        }
    } header: {
        Label("Collections", systemImage: "folder")
    }
}
```

You can also enable customization by adding the [`tabViewCustomization(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tabViewCustomization(_:)) modifier to the `TabView` and the [`customizationID(_:)`](https://developer.apple.com/documentation/SwiftUI/TabContent/customizationID(_:)) modifier to each tab. Customization in Destination Video allows people to drag tabs from the sidebar to the tab bar, hide nonessential tabs, and rearrange tabs in the sidebar.

For more information, see [`Enhancing your app’s content with tab navigation`](https://developer.apple.com/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation).

##### Customize Windows in Macos

In macOS, the app supports multiple windows including a main window that shows the video collections and a separate video player window. You can customize the appearance and function of each window to create a more engaging experience.

![A screenshot that shows the tab view in Destination Video for Mac.](https://docs-assets.developer.apple.com/published/311d2092a64eba16fb8e25f0170328fc/Destination-video-mac-windows%402x.png)

The main window displays the app content — collections of videos — in a `TabView` navigation presented as a sidebar. Because the app doesn’t contain any additional toolbar items and the sidebar provides a visual indication of where a person is in the navigation hierarchy, the toolbar isn’t needed and unnecessarily takes up space. This sample removes the toolbar title and background using the [`toolbar(removing:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbar(removing:)) and [`toolbarBackgroundVisibility(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbarBackgroundVisibility(_:for:)) modifiers. This creates a full-window browsing experience for Destination Video running in macOS.

```swift
ContentView()
    // ...
    #if os(macOS)
    .toolbarBackgroundVisibility(.hidden, for: .windowToolbar)
    .toolbar(removing: .title)
    #endif
```

Other window customizations in Destination Video include extending a window’s drag region, participating in a window’s zoom action, and modifying a window’s state restoration behavior. For more information, see [`Customizing window styles and state-restoration behavior in macOS`](https://developer.apple.com/documentation/SwiftUI/Customizing-window-styles-and-state-restoration-behavior-in-macOS).

##### Display Horizontally Scrollable Cards in Tvos

Destination Video presents video cards in a horizontally scrollable list in the Watch Now tab. When a person taps on a video card, the app navigates to a view that shows detailed information about the video. In tvOS, each card implements the [`card`](https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/card) button style. When a person hovers on a card, it fully scales and lifts up.

This sample prevents the scroll view from clipping its content when the card expands using the [`scrollClipDisabled(_:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollClipDisabled(_:)) modifier. Additionally, this sample provides a title for the list by placing the `ScrollView` within a [`Section`](https://developer.apple.com/documentation/SwiftUI/Section) container and passing the title into the [`init(content:header:)`](https://developer.apple.com/documentation/SwiftUI/Section/init(content:header:)) initializer. This allows the title to also lift and move as the card expands and lifts upon when a person hovers on it.

```swift
Section {
    ScrollView(.horizontal, showsIndicators: false) {
        HStack(spacing: Constants.cardSpacing) {
            ForEach(videos) { video in
                // The video card view.
            }
        }
        .buttonStyle(buttonStyle)
        .padding(.leading, Constants.outerPadding)
    }
    .scrollClipDisabled()
} header: {
    // The list title
}

var buttonStyle: some PrimitiveButtonStyle {
    #if os(tvOS)
    .card
    #else
    .plain
    #endif
}
```

For more information about displaying content in tvOS, see [`Creating a tvOS media catalog app in SwiftUI`](https://developer.apple.com/documentation/SwiftUI/Creating-a-tvOS-media-catalog-app-in-SwiftUI).

##### Present an Immersive Space

Building video playback apps for visionOS provides new opportunities to enhance the viewing experience beyond the bounds of the player window. To add a greater level of immersion, this sample presents an immersive space that displays a scene around a person as they watch the video.

![A screenshot that shows the Studio environment in visionOS.](https://docs-assets.developer.apple.com/published/130c209e25f4dbb4ab333f9cc9f91a68/Destination-video-immersive-space%402x.png)

It defines the immersive space in the `DestinationVideo` app structure.

```swift
// Defines an immersive space to present a environment in which to watch the video.
ImmersiveSpace(id: ImmersiveEnvironmentView.id) {
    ImmersiveEnvironmentView()
        .environment(immersiveEnvironment)
        .onAppear {
            contentBrightness = immersiveEnvironment.contentBrightness
            surroundingsEffect = immersiveEnvironment.surroundingsEffect
        }
        .onDisappear {
            contentBrightness = .automatic
            surroundingsEffect = nil
        }
        // Applies a custom tint color for the video passthrough of a person's hands and surroundings.
        .preferredSurroundingsEffect(surroundingsEffect)
}
// Set the content brightness for the immersive space.
.immersiveContentBrightness(contentBrightness)
// Set the immersion style to progressive, so a person can use the Digital Crown to dial in their experience.
.immersionStyle(selection: .constant(.progressive), in: .progressive)
```

The [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) presents an instance of `ImmersiveEnvironmentView`, which maps a texture to the inside of a sphere that it displays around a person. The app presents it using the `.progressive` immersion style, which lets people change the amount of immersion they experience by turning the Digital Crown on the device.

##### Play Video in a Full Window Player

One of the most exciting features of visionOS is its ability to play 3D video along with Spatial Audio, which adds a deeper level of immersion to the viewing experience. Playing 3D content in your app requires that you display [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) full window. When you present the player this way, the system automatically docks it into the ideal viewing position, and presents streamlined playback controls that keep the person’s focus on the content.

![A screenshot that shows a video player in the Studio environment in visionOS.](https://docs-assets.developer.apple.com/published/55a04fef3a7071933a6aecf0bfc0f73f/Destination-video-video-player%402x.png)

> **Note**: In iOS or tvOS, you typically present video in a full-screen presentation using the [`fullScreenCover(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(isPresented:onDismiss:content:)) modifier. This API is available in visionOS; however, the recommended way to present the player for full-window playback is to set it as the root view of your app’s window group.

In iOS or tvOS, you typically present video in a full-screen presentation using the [`fullScreenCover(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(isPresented:onDismiss:content:)) modifier. This API is available in visionOS; however, the recommended way to present the player for full-window playback is to set it as the root view of your app’s window group.

Destination Video’s `ContentView` displays the app’s library by default. It observes changes to the player model’s `presentation` property, which indicates whether the app requests inline or full-window playback. When the presentation state changes to `fullWindow`, the view redraws the UI to display the player view in place of the library.

```swift
struct ContentView: View {
    @Environment(PlayerModel.self) private var player
    #if os(visionOS)
    @Environment(ImmersiveEnvironment.self) private var immersiveEnvironment
    #endif

    var body: some View {
        #if os(visionOS)
        Group {
            switch player.presentation {
            case .fullWindow:
                // Presents the player in a full window and begins playback.
                PlayerView()
                    .immersiveEnvironmentPicker {
                        ImmersiveEnvironmentPickerView()
                    }
                    .onAppear {
                        player.play()
                    }
            default:
                // Shows the app's content library by default.
                DestinationTabs()
            }
        }
        // A custom modifier that manages the presentation and dismissal of the app's immersive space.
        .immersionManager()
        #else
        DestinationTabs()
            // A custom modifier that presents the video player appropriately for the current platform.
            .presentVideoPlayer()
        #endif
    }
}
```

When someone selects the Play Video button on the detail view, the app calls the player model’s `loadVideo(_: presentation:)` method requesting the `fullWindow` presentation option.

```swift
Button {
    /// Load the media item for full-window presentation.
    player.loadVideo(video, presentation: .fullWindow)
} label: {
    Label("Play Video", systemImage: "play.fill")
}
```

After the player model successfully loads the video content for playback, it updates its `presentation` value to `fullWindow`, which causes the app to replace `DestinationTabs` with `PlayerView`.

To dismiss the full-window player in visionOS, people tap the Back button in the player UI. To handle this action, the app’s `PlayerViewControllerDelegate` type defines an [`AVPlayerViewControllerDelegate`](https://developer.apple.com/documentation/AVKit/AVPlayerViewControllerDelegate) object that handles the dismissal.

When the delegate receives this call, it clears the media from the player model and resets the presentation state back to its default value, which results in the Destination Video app redisplaying the `DestinationTabs` view.

##### Configure the Spatial Audio Experience

Media playback apps require common configuration of their capabilities and audio session. In addition to performing the steps outlined in [`Configuring your app for media playback`](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback), Destination Video also adopts new [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) API to customize a person’s Spatial Audio experience.

After the app successfully loads a video for playback, it configures the Spatial Audio experience for the current presentation. For the inline player view, it sets the experience to a small, focused sound stage where the audio originates from the location of the view. When displaying a video full window, it sets the experience to a large, fully immersive sound stage.

```swift
private func configureAudioExperience(for presentation: Presentation) {
    #if os(visionOS)
    do {
        let experience: AVAudioSessionSpatialExperience
        switch presentation {
        case .inline:
            // Set a small, focused sound stage when watching trailers.
            experience = .headTracked(soundStageSize: .small, anchoringStrategy: .automatic)
        case .fullWindow:
            // Set a large sound stage size when viewing full window.
            experience = .headTracked(soundStageSize: .large, anchoringStrategy: .automatic)
        }
        try AVAudioSession.sharedInstance().setIntendedSpatialExperience(experience)
    } catch {
        logger.error("Unable to set the intended spatial experience. \(error.localizedDescription)")
    }
    #endif
}
```

##### Customize an Environment Using Realitykit and Reality Composer Pro

In visionOS, Destination Video provides a custom environment, called Studio.

To optimize the viewing experience in the Studio environment, this sample implements the following:

In visionOS, a person can select the environment in which they watch a video by tapping on the environment picker menu presented by [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController). The Studio environment has light and dark variants. This sample adds them to the list of environments that appear in the environment picker menu using the [`immersiveEnvironmentPicker(content:)`](https://developer.apple.com/documentation/SwiftUI/View/immersiveEnvironmentPicker(content:)) modifier.

```swift
PlayerView()
    .immersiveEnvironmentPicker {
        ImmersiveEnvironmentPickerView()
    }
```

For more information, see [`Building an immersive media viewing experience`](building-an-immersive-media-viewing-experience.md) and [`Enabling video reflections in an immersive environment`](enabling-video-reflections-in-an-immersive-environment.md).

##### Provide a Shared Viewing Experience

One of the best ways to enhance your app’s playback experience is to make that experience shareable with others. You can use the [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) and the [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) frameworks to build [`SharePlay`](https://developer.apple.comhttps://developer.apple.com/shareplay/) experiences that bring people together even when they can’t be in the same location.

The Destination Video app creates an experience where people can watch videos with others across devices and platforms. It defines a group activity called `WatchingActivity` that adopts the [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity) protocol.  When people have a FaceTime call active and they play a video in the full-window player, it becomes eligible for playback for everyone on the call.

The app’s `WatchingCoordinator` actor manages Destination Video’s SharePlay functionality. It observes the activation of new `WatchingActivity` sessions. After a `WatchingActivity` session starts, the `WatchingCoordinator` sets the [`GroupSession`](https://developer.apple.com/documentation/GroupActivities/GroupSession) instance on the player object’s [`AVPlaybackCoordinator`](https://developer.apple.com/documentation/AVFoundation/AVPlaybackCoordinator).

```swift
private typealias WatchingSession = GroupSession<WatchingActivity>
private weak var coordinator: AVPlayerPlaybackCoordinator?

private var liveSession: WatchingSession? {
    didSet {
        guard let liveSession else { return }
        // Set the group session on the AVPlayer object's playback coordinator
        // so it can synchronize playback with other devices.
        coordinator?.coordinateWithSession(liveSession)
    }
}
```

With the player configured to use the group session, when the app loads new videos, they become eligible to share with people in the FaceTime call.

###### Related Samples

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/destination-video)*