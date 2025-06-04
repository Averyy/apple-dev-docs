# WKInterfaceVolumeControl

**Framework**: Watchkit  
**Kind**: class

An interface element that provides control of the audio volume from the watch or a paired iPhone.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class WKInterfaceVolumeControl
```

## Overview

Configure your app’s audio source and the appearance of the volume control in your storyboard file. Use the [`WKInterfaceVolumeControl`](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol) instance to change the volume’s tint color at runtime.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a volume control in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen control.

After selecting the volume control, the user can increase or decrease the audio’s volume using the crown. The system automatically handles changing the audio source’s volume. You cannot access or change the volume programmatically in your app.

Xcode lets you configure your volume control in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Controls Local Volume', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The volume control’s audio source. If checked, the control affects the volume of long-form audio playing on the watch.  If unchecked, it affects the volume of audio playing on the paired iPhone. '}, {'type': 'image', 'identifier': 'spacer'}, {'type': 'text', 'text': ' You must set this value at design time. You cannot change its value programmatically.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Tint Color'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The tint color for the volume control.  By default, the system uses the application’s tint color. '}, {'type': 'image', 'identifier': 'spacer'}, {'type': 'text', 'text': ' The system only applies the tint color to the control’s default state (when the crown is not being used to adjust the volume). '}, {'type': 'image', 'identifier': 'spacer'}, {'type': 'text', 'text': ' You can change this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceVolumeControl/setTintColor(_:)'}, {'type': 'text', 'text': ' method.'}]}] |

## Topics

### Setting the Tint Color
- [func setTintColor(UIColor?)](settintcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/settintcolor(_:)))
  Sets the volume control’s tint color.
### Managing Input from the Digital Crown
- [func focus()](focus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/focus()))
  Sets the volume control as the focus for input from the Digital Crown.
- [func resignFocus()](resignfocus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/resignfocus()))
  Removes focus from the volume control, causing it to stop receiving input from the Digital Crown.
### SwiftUI
- [init(origin: WKInterfaceVolumeControl.Origin)](init(origin:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/init(origin:)))
  Creates a volume control for use in SwiftUI.
- [WKInterfaceVolumeControl.Origin](origin.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/origin))
  The source of the audio managed by the volume control.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
- [Adding a Now Playing View](adding-a-now-playing-view.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view))
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
- [class WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol)*