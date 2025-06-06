# Using custom sounds for focus movement

**Framework**: UIKit

Customize the sounds users hear when focus moves.

#### Overview

The default focus movement sounds are sufficient for the vast majority of apps. However, there might be times when you want to change the default sound to a custom sound that’s more suited to your app.

##### Add a Custom Sound File to Your App

Drag the custom focus sound file into your Xcode project. Ensure that the app is selected as a target. You can use any sound file that conforms to the standard iOS sound file formats and is less than 30 seconds long. However, be sure that the sounds you create are appropriate for your app. Playing a 20-second sound clip every time the user moves focus won’t result in a good user experience.

![Screenshot that shows targeting the app when adding a sound file.](https://docs-assets.developer.apple.com/published/6dbc5bf5a24185f428cd8d71584f0df2/media-2943426%402x.png)

##### Register Your Sound File

After you add the sound file to your app, you have to register the sound file with the focus environment. Before registering the sound file, you must create an identifier for the sound using [`UIFocusSoundIdentifier`](uifocussoundidentifier.md). The identifier must be unique for the app. After creating an identifier, locate the sound file in your app bundle and register the sound file using [`register(_:forSoundIdentifier:)`](uifocussystem/register(_:forsoundidentifier:).md).

```swift
let myPing = UIFocusSoundIdentifier.init(rawValue: "customPing")
let soundURL = Bundle.main.url(forResource: "ping", withExtension: "aif")!
UIFocusSystem.register(_: soundURL, forSoundIdentifier: myPing)
```

There are a few things to remember when registering your sound file:

- Register the sound file early in your app’s lifecycle. The cost to prepare a sound for playback is nontrivial, so you want the sound to be fully prepared by the time a focus update occurs.
- You can register multiple sound files in your app.
- Register each sound file once. Registering a previously registered sound file results in an error that causes an immediate assertion failure.
- See the [`WWDC 2017 video Focus Interaction in tvOS 11`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2017/224/) for information about which focus sound is played when an item becomes focused.

##### Override the Default Focus Sounds

The [`soundIdentifierForFocusUpdate(in:)`](uifocusenvironment/soundidentifierforfocusupdate(in:).md) function is called when focus changes. The default focus sound is played when this function isn’t implemented. Override the function to play your custom sounds when focus changes.

```swift
override func soundIdentifierForFocusUpdate(in context: UIFocusUpdateContext) -> UIFocusSoundIdentifier? {    
    return myPing
}
```

## See Also

- [func soundIdentifierForFocusUpdate(in: UIFocusUpdateContext) -> UIFocusSoundIdentifier?](uifocusenvironment/soundidentifierforfocusupdate(in:).md)
  Asks the delegate for the identifier of the sound to play when the object gains focus.
- [struct UIFocusSoundIdentifier](uifocussoundidentifier.md)
  An identifier for a focus-related sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/using-custom-sounds-for-focus-movement)*