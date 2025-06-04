# WKInterfaceVolumeControl

**Framework**: WatchKit  
**Kind**: class

An interface element that provides control of the audio volume from the watch or a paired iPhone.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class WKInterfaceVolumeControl
```

#### Overview

Configure your app’s audio source and the appearance of the volume control in your storyboard file. Use the [`WKInterfaceVolumeControl`](wkinterfacevolumecontrol.md) instance to change the volume’s tint color at runtime.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a volume control in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen control.

After selecting the volume control, the user can increase or decrease the audio’s volume using the crown. The system automatically handles changing the audio source’s volume. You cannot access or change the volume programmatically in your app.

##### Interface Builder Configuration Options

Xcode lets you configure your volume control in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Controls Local Volume | The volume control’s audio source. If checked, the control affects the volume of long-form audio playing on the watch.  If unchecked, it affects the volume of audio playing on the paired iPhone. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You must set this value at design time. You cannot change its value programmatically. |
| Tint Color | The tint color for the volume control.  By default, the system uses the application’s tint color. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The system only applies the tint color to the control’s default state (when the crown is not being used to adjust the volume). ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can change this value programmatically using the [`setTintColor(_:)`](wkinterfacevolumecontrol/settintcolor(_:).md) method. |

## Topics

### Setting the Tint Color
- [func setTintColor(UIColor?)](wkinterfacevolumecontrol/settintcolor(_:).md)
  Sets the volume control’s tint color.
### Managing Input from the Digital Crown
- [func focus()](wkinterfacevolumecontrol/focus.md)
  Sets the volume control as the focus for input from the Digital Crown.
- [func resignFocus()](wkinterfacevolumecontrol/resignfocus.md)
  Removes focus from the volume control, causing it to stop receiving input from the Digital Crown.
### SwiftUI
- [init(origin: WKInterfaceVolumeControl.Origin)](wkinterfacevolumecontrol/init(origin:).md)
  Creates a volume control for use in SwiftUI.
- [WKInterfaceVolumeControl.Origin](wkinterfacevolumecontrol/origin.md)
  The source of the audio managed by the volume control.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md)
  Provide a view that controls the currently playing audio from your app.
- [PUICAutoLaunchAudioOptOut](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFilePlayer](wkaudiofileplayer.md)
  An object that controls playback of a single audio item.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md)
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md)
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md)
  An object that stores a reference to an audio file and provides metadata information about that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol)*